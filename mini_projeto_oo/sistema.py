class Funcionario:
    def __init__(self, nome, matricula, salario_fixo):
        self.__nome = nome
        self.__matricula = matricula
        self.set_salario_fixo(salario_fixo)

    def get_nome(self):
        return self.__nome

    def get_matricula(self):
        return self.__matricula

    def get_salario_fixo(self):
        return self.__salario_fixo

    def set_salario_fixo(self, salario_fixo):
        if salario_fixo >= 0:
            self.__salario_fixo = salario_fixo
        else:
            print("O valor do salário deve ser igual ou superior a zero.")
            self.__salario_fixo = 0

    def calcular_salario(self):
        pass

    def exibir(self):
        print(
            f"Nome: {self.get_nome()} | "
            f"Matricula: {self.get_matricula()} | "
            f"Tipo: {self.__class__.__name__} | "
            f"Salario: R$ {self.calcular_salario():.2f}"
        )


class CLT(Funcionario):
    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.get_salario_fixo()


class Vendedor(Funcionario):
    def __init__(self, nome, matricula, salario_fixo, vendas):
        super().__init__(nome, matricula, salario_fixo)
        self.__vendas = vendas

    def get_vendas(self):
        return self.__vendas

    def set_vendas(self, vendas):
        if vendas >= 0:
            self.__vendas = vendas

    def calcular_salario(self):
        return self.get_salario_fixo() + (self.__vendas * 0.10)


class Gerente(Funcionario):
    BONUS = 1500

    def __init__(self, nome, matricula, salario_fixo):
        super().__init__(nome, matricula, salario_fixo)

    def calcular_salario(self):
        return self.get_salario_fixo() + self.BONUS


funcionario1 = CLT("Endrick", "001", 3500)
funcionario2 = Vendedor("Fabricio", "002", 4000, 15000)
funcionario3 = Gerente("Renan", "003", 10000)

funcionarios = [funcionario1, funcionario2, funcionario3]

for funcionario in funcionarios:
    funcionario.exibir()
