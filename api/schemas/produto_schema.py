from api import ma
from ..models import produto_model
from marshmallow import fields
from ..schemas import inventario_schema

class ProdutoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = produto_model.Produto
        load_instance = True
        fields = ("id", "velocidade", "preco", "descricao", "disponibilidade")

    velocidade = fields.String(required=True)
    preco = fields.Integer(required=True)
    descricao = fields.String(required=True)
    disponibilidade = fields.String(required=True)

