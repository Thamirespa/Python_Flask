from api import ma
from ..models import inventario_model
from marshmallow import fields
from ..schemas import cliente_schema
from ..schemas import produto_schema



class InventarioSchema(ma.SQLAlchemyAutoSchema):

    cliente = ma.Nested(cliente_schema.ClienteSchema, many=True, only=('id', 'nome'))
    produto = ma.Nested(produto_schema.ProdutoSchema, many=True, only=('id', 'velocidade'))
    class Meta:
        model = inventario_model.Inventario
        load_instance = True
        fields = ("id", "quantidade", "cliente", "produto")
    quantidade = fields.Integer(required=True)
    cliente = fields.Integer(required=True)
    produto = fields.Integer(required=True)




