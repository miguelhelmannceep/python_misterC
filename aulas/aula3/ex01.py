class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


produto1 = Produto("Camiseta MBL Prendeu Matou", 94.14)
produto2 = Produto("Blusa MBL onça", 299.14)

print("Produto 1:")
print("Nome:", produto1.nome)
print("Preço:", produto1.preco)

print("\nProduto 2:")
print("Nome:", produto2.nome)
print("Preço:", produto2.preco)
