from flask_restful import Resource
from api import api
from ..schemas import produto_schema
from flask import request, make_response, jsonify
from ..entidades import produto
from ..services import produto_service
from flask_jwt_extended import jwt_required

class ProdutoList(Resource):
    #@jwt_required()
    def get(self):
        produtos = produto_service.listar_produtos()
        ps = produto_schema.ProdutoSchema(many=True)
        return make_response(ps.jsonify(produtos), 200)

    #@jwt_required()
    def post(self):
        ps = produto_schema.ProdutoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            velocidade = request.json["velocidade"]
            preco = request.json["preco"]
            descricao = request.json["descricao"]
            disponibilidade = request.json["disponibilidade"]

            novo_produto = produto.Produto(velocidade=velocidade, preco=preco, descricao=descricao, disponibilidade=disponibilidade)
            resultado = produto_service.cadastrar_produto(novo_produto)
            x = ps.jsonify(resultado)
            return make_response(x, 201)

class ProdutoDetail(Resource):
    #@jwt_required()
    def get(self, id):
        produto = produto_service.listar_produto_id(id)
        if produto is None:
            return make_response(jsonify("Produto não foi encontrado"), 404)
        ps = produto_schema.ProdutoSchema()
        return make_response(ps.jsonify(produto), 200)

    #@jwt_required()
    def put(self, id):
        produto_bd = produto_service.listar_produto_id(id)
        if produto_bd is None:
            return make_response(jsonify("Produto não foi encontrado"), 404)
        ps = produto_schema.ProdutoSchema()
        validate = ps.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            velocidade = request.json["velocidade"]
            preco = request.json["preco"]
            descricao = request.json["descricao"]
            disponibilidade = request.json["disponibilidade"]


            novo_produto = produto.Produto(velocidade=velocidade, preco=preco, descricao=descricao, disponibilidade=disponibilidade)
            produto_service.atualiza_produto(produto_bd, novo_produto)
            produto_atualizado = produto_service.listar_produto_id(id)
            return make_response(ps.jsonify(produto_atualizado), 200)

    #@jwt_required()
    def delete(self, id):
        produto_bd = produto_service.listar_produto_id(id)
        if produto_bd is None:
            return make_response(jsonify("Produto não encontrada"), 404)
        produto_service.remove_produto(produto_bd)
        return make_response(jsonify('Produto excluído com sucesso'), 204)

api.add_resource(ProdutoList, '/produto')
api.add_resource(ProdutoDetail, '/produto/<int:id>')