class Produto:
    def __init__(self, nome, preco):
        self.__nome = nome
        self.__preco = 0
        self.set_preco(preco)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("O preço não pode ser negativo.")


produto = Produto("Zenbook 14", 4600)
print(produto.get_nome())
print(produto.get_preco())

produto.set_preco(-400)
produto.set_preco(5000)

print(produto.get_preco())
