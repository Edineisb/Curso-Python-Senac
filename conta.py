class ContaBancaria:
    def __init__(self, sald_inicial):
        self.saldo = sald_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente!")

    def get_saldo(self):
        return self.saldo


conta = ContaBancaria(1000)
conta.depositar(500)
print(conta.get_saldo())