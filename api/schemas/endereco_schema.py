from api import ma
from ..models import endereco_model
from marshmallow import fields



class EnderecoSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = endereco_model.Endereco
        load_instance = True
        fields = ("id", "rua", "numero", "complemento", "cep", "bairro", "cidade", "estado")

    rua = fields.String(required=True)
    numero = fields.String(required=True)
    complemento = fields.String(required=True)
    cep = fields.String(required=True)
    bairro = fields.String(required=True)
    cidade = fields.String(required=True)
    estado = fields.String(required=True)
    estado = fields.String(required=True)



