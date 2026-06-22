class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def extrato(self):
        print("Titular:", self.titular)
        print("Saldo:", self.saldo)


conta = ContaBancaria("Miguel Helmann", 67000000)

conta.depositar(500000)
conta.sacar(200000)
conta.sacar(1500000)

conta.extrato()
