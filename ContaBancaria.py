class ContaBancaria:
    def __init__(self, sald_inicial):
        self.saldo = sald_inicial

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def obter_saldo(self):
        return self.saldo


minha_conta = ContaBancaria(1000)
minha_conta.depositar(500)
minha_conta.sacar(200)
print(minha_conta.obter_saldo())
