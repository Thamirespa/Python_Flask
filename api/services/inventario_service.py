
from ..models import inventario_model
from api import db
from .cliente_service import listar_cliente_id
from .produto_service import listar_produto_id

def cadastrar_inventario(inventario):
    inventario_bd = inventario_model.Inventario(quantidade=inventario.quantidade)
    for i in inventario.cliente:
        cliente = listar_cliente_id(i)
        inventario_bd.cliente.append(cliente)
    for i in inventario.produto:
        produto = listar_produto_id(i)
        inventario_bd.produto.append(produto)
    db.session.add(inventario_bd)
    db.session.commit()
    return inventario_bd

def listar_inventario():
    inventario = inventario_model.Inventario.query.all()
    return inventario

def listar_inventario_id(id):
    inventario = inventario_model.Inventario.query.filter_by(id=id).first()
    return inventario

def atualiza_inventario(inventario_anterior, inventario_novo):
    inventario_anterior.quantidade = inventario_novo.quantidade
    inventario_anterior.cliente_id = inventario_novo.cliente_id
    inventario_anterior.produto_id = inventario_novo.produto_id
    inventario_anterior.cliente = []
    inventario_anterior.produto = []
    for i in inventario_novo.cliente:
        cliente = listar_cliente_id(i)
        inventario_anterior.cliente.append(cliente)
    for i in inventario_novo.produto:
        produto = listar_produto_id(i)
        inventario_anterior.produto.append(produto)
    db.session.commit()

def remove_inventario(inventario):
    db.session.delete(inventario)
    db.session.commit()