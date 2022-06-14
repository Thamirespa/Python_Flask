class Inventario():
    def __init__(self, quantidade, cliente, produto):

        self.__quantidade = quantidade
        self.__cliente = cliente
        self.__produto = produto



    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente

    @property
    def produto(self):
        return self.__produto

    @produto.setter
    def produto(self, produto):
        self.__produto = produto