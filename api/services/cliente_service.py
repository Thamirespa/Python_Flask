from ..models import cliente_model
from api import db
from .endereco_service import listar_endereco_id
from .produto_service import listar_produto_id

def cadastrar_cliente(cliente):
    cliente_bd = cliente_model.Cliente(nome=cliente.nome, email=cliente.email, cpf=cliente.cpf, telefone=cliente.telefone)
    db.session.add(cliente_bd)
    db.session.commit()
    return cliente_bd

def listar_clientes():
    clientes = cliente_model.Cliente.query.all()
    return clientes

def listar_cliente_id(id):
    cliente = cliente_model.Cliente.query.filter_by(id=id).first()
    return cliente

def atualiza_cliente(cliente_anterior, cliente_novo):
    cliente_anterior.nome = cliente_novo.nome
    cliente_anterior.email = cliente_novo.email
    cliente_anterior.cpf = cliente_novo.cpf
    cliente_anterior.telefone = cliente_novo.telefone
    db.session.commit()

def remove_cliente(cliente):
    db.session.delete(cliente)
    db.session.commit()