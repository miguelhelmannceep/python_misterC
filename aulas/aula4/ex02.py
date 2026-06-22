class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = ""
        self.__idade = 0

        self.set_nome(nome)
        self.set_idade(idade)

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        if nome.strip() != "":
            self.__nome = nome
        else:
            print("Nome não pode ser vazio.")

    def get_idade(self):
        return self.__idade

    def set_idade(self, idade):
        if 0 <= idade <= 120:
            self.__idade = idade
        else:
            print("Idade inválida.")

    def apresentar(self):
        print(f"Nome: {self.__nome}")
        print(f"Idade: {self.__idade}")


p1 = Pessoa("Miguel MBL", 16)
p1.apresentar()

p1.set_nome("")
p1.set_idade(150)
