class ContaBancaria:
    def __init__(self, titular):
        self.__titular = titular
        self.__saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print("Depósito realizado.")
        else:
            print("Valor inválido.")

    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido.")
        elif valor > self.__saldo:
            print("Saldo insuficiente.")
        else:
            self.__saldo -= valor
            print("Saque realizado.")

    def get_saldo(self):
        return self.__saldo

    def extrato(self):
        print(f"Titular: {self.__titular}")
        print(f"Saldo: R$ {self.__saldo:.2f}")


conta = ContaBancaria("Miguel Pieri Helmann")

conta.depositar(2500)
conta.sacar(500)
conta.sacar(1500)

conta.extrato()
