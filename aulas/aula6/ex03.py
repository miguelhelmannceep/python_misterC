class Forma:
    def area(self):
        return 0


class Triangulo(Forma):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return (self.base * self.altura) / 2


class Quadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2


formas = [
    Triangulo(12, 6),
    Quadrado(5),
    Triangulo(9, 4),
    Quadrado(8)
]

for forma in formas:
    print("Área:", forma.area())
