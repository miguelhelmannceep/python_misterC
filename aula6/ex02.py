class Instrumento:
    def tocar(self):
        print("Som genérico")


class Flauta(Instrumento):
    def tocar(self):
        print("Tocando flauta: fiu fiu")


class Tambor(Instrumento):
    def tocar(self):
        print("Tocando tambor: bum bum")


class Guitarra(Instrumento):
    def tocar(self):
        print("Tocando guitarra: trrim trrim")


instrumentos = [Flauta(), Tambor(), Guitarra()]

for instrumento in instrumentos:
    instrumento.tocar()
