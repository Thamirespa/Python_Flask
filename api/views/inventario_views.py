from flask_restful import Resource
from api import api
from ..schemas import inventario_schema
from flask import request, make_response, jsonify
from ..entidades import cliente, inventario
from ..services import inventario_service, cliente_service, produto_service
from flask_jwt_extended import jwt_required

class InventarioList(Resource):
    #@jwt_required()
    def get(self):
        inventario = inventario_service.listar_inventario()
        ps = inventario_schema.InventarioSchema(many=True)
        return make_response(ps.jsonify(inventario), 200)

    #@jwt_required()
    def post(self):
        ps = inventario_schema.InventarioSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:

            quantidade = request.json["quantidade"]
            cliente = request.json["cliente"]
            produto = request.json["produto"]
            novo_inventario = inventario.Inventario(quantidade=quantidade, cliente=cliente, produto=produto)
            resultado = inventario_service.cadastrar_inventario(novo_inventario)
            x = ps.jsonify(resultado)
            return make_response(x, 201)


class InventarioDetail(Resource):

    #@jwt_required()
    def get(self, id):
        inventario = inventario_service.listar_inventario_id(id)
        if inventario is None:
            return make_response(jsonify("inventario não foi encontrado"), 404)
        cs = inventario_schema.InventarioSchema()
        return make_response(cs.jsonify(inventario), 200)

    #@jwt_required()
    def put(self, id):
        inventario_bd = inventario_service.listar_inventario_id(id)
        if inventario_bd is None:
            return make_response(jsonify("inventario não foi encontrado"), 404)
        cs = inventario_schema.InventarioSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:

            quantidade = request.json["quantidade"]
            cliente = request.json["cliente"]
            produto = request.json["produto"]

            novo_inventario = inventario.Inventario(quantidade=quantidade, cliente=cliente, produto=produto)
            inventario_service.atualiza_inventario(inventario_bd, novo_inventario)
            inventario_atualizado = inventario_service.listar_inventario_id(id)
            return make_response(cs.jsonify(inventario_atualizado), 200)

    #@jwt_required()
    def delete(self, id):
        inventario_bd = inventario_service.listar_inventario_id(id)
        if inventario_bd is None:
            return make_response(jsonify("inventarionão encontrado"), 404)
        inventario_service.remove_cliente(inventario_bd)
        return make_response(jsonify('pedido excluído com sucesso'), 204)


api.add_resource(InventarioList, '/inventario')
api.add_resource(InventarioDetail, '/inventario/<int:id>')






