class Funcionario:
    def calcular_salario(self):
        return 0


class Vendedor(Funcionario):
    def __init__(self, salario_fixo, comissao):
        self.salario_fixo = salario_fixo
        self.comissao = comissao

    def calcular_salario(self):
        return self.salario_fixo + self.comissao


class Gerente(Funcionario):
    def __init__(self, salario_fixo, bonus):
        self.salario_fixo = salario_fixo
        self.bonus = bonus

    def calcular_salario(self):
        return self.salario_fixo + self.bonus


vendedor = Vendedor(3000, 670)
gerente = Gerente(6700, 2000)

print("Salário do vendedor:", vendedor.calcular_salario())
print("Salário do gerente:", gerente.calcular_salario())
