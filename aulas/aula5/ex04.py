class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def apresentar(self):
        print("Aluno")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Matrícula: {self.matricula}")
        print("-" * 20)


class Professor(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def apresentar(self):
        print("Professor")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Salário: R$ {self.salario:.2f}")
        print("-" * 20)


pessoas = [
    Aluno("Miguel", 16, "67000"),
    Professor("Diego", 67, 1000),
    Aluno("Jonesy", 17, "200000"),
    Professor("Pichau", 56, 10000)
]

for pessoa in pessoas:
    pessoa.apresentar()
