from api import db


class Cliente(db.Model):
    __tablename__ = "cliente"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    cpf = db.Column(db.String(15))
    telefone = db.Column(db.String(16))
    inventario = db.relationship("Inventario", secondary="cliente_inventario", back_populates="cliente")





