from api import db
from .cliente_model import Cliente
from .produto_model import Produto

cliente_inventario = db.Table('cliente_inventario',
db.Column('cliente_id', db.Integer, db.ForeignKey('cliente.id'), primary_key=True, nullable=False),
db.Column('inventario_id', db.Integer, db.ForeignKey('inventario.id'), primary_key=True, nullable=False)
                            )

class Inventario(db.Model):
    __tablename__ = "inventario"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    cliente = db.relationship(Cliente, secondary="cliente_inventario", back_populates="inventario")
    produto = db.relationship(Produto, secondary="produto_inventario", back_populates="inventario")

produto_inventario = db.Table('produto_inventario',
db.Column('produto_id', db.Integer, db.ForeignKey('produto.id'), primary_key=True, nullable=False),
db.Column('inventario_id', db.Integer, db.ForeignKey('inventario.id'), primary_key=True, nullable=False)
                            )


