from api import db

class Produto(db.Model):
    __tablename__ = "produto"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True,nullable=False)
    velocidade = db.Column(db.String(50), nullable=False)
    preco = db.Column(db.Integer, nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    disponibilidade = db.Column(db.String(200), nullable=False)
    inventario = db.relationship("Inventario", secondary="produto_inventario", back_populates="produto")

