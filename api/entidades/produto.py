class Produto():
    def __init__(self, velocidade, preco, descricao, disponibilidade):
        self.__velocidade = velocidade
        self.__preco = preco
        self.__descricao = descricao
        self.__disponibilidade = disponibilidade

    @property
    def velocidade(self):
        return self.__velocidade

    @velocidade.setter
    def nome(self, velocidade):
        self.__velocidade = velocidade

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def disponibilidade(self):
        return self.__disponibilidade

    @disponibilidade.setter
    def disponibilidade(self, disponibilidade):
        self.__disponibilidade = disponibilidade