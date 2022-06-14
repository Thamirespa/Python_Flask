from flask_restful import Resource
from api import api
from ..schemas import cliente_schema
from flask import request, make_response, jsonify
from ..entidades import cliente
from ..services import cliente_service, inventario_service
from flask_jwt_extended import jwt_required

class ClienteList(Resource):
    #@jwt_required()
    def get(self):
        clientes = cliente_service.listar_clientes()
        cs = cliente_schema.ClienteSchema(many=True)
        return make_response(cs.jsonify(clientes), 200)

    #@jwt_required()
    def post(self):
        cs = cliente_schema.ClienteSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            email = request.json["email"]
            cpf = request.json["cpf"]
            telefone = request.json["telefone"]
            novo_cliente = cliente.Cliente(nome=nome, email=email, cpf=cpf, telefone=telefone)
            resultado = cliente_service.cadastrar_cliente(novo_cliente)
            x = cs.jsonify(resultado)
            return make_response(x, 201)


class ClienteDetail(Resource):

    #@jwt_required()
    def get(self, id):
        cliente = cliente_service.listar_cliente_id(id)
        if cliente is None:
            return make_response(jsonify("cliente não foi encontrado"), 404)
        cs = cliente_schema.ClienteSchema()
        return make_response(cs.jsonify(cliente), 200)

    #@jwt_required()
    def put(self, id):
        cliente_bd = cliente_service.listar_cliente_id(id)
        if cliente_bd is None:
            return make_response(jsonify("Cliente não foi encontrado"), 404)
        cs = cliente_schema.ClienteSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            nome = request.json["nome"]
            email = request.json["email"]
            cpf = request.json["cpf"]
            telefone = request.json["telefone"]
            novo_cliente = cliente.Cliente(nome=nome, email=email, cpf=cpf, telefone=telefone)
            cliente_service.atualiza_cliente(cliente_bd, novo_cliente)
            cliente_atualizado = cliente_service.listar_cliente_id(id)
            return make_response(cs.jsonify(cliente_atualizado), 200)

    #@jwt_required()
    def delete(self, id):
        cliente_bd = cliente_service.listar_cliente_id(id)
        if cliente_bd is None:
            return make_response(jsonify("Cliente não encontrado"), 404)
        cliente_service.remove_cliente(cliente_bd)
        return make_response(jsonify('Cliente excluído com sucesso'), 204)


api.add_resource(ClienteList, '/cliente')
api.add_resource(ClienteDetail, '/cliente/<int:id>')






