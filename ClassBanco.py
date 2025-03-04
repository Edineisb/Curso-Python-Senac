class Banco:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f"Deposito de R${valor:.2f} realizado.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado.")
        else:
            print("Saldo insuficiente!")

    def mostrar_saldo(self):
        print(f"Saldo atual: R$ {self.saldo:.2f}")


conta = Banco()
conta.depositar(100)
conta.sacar(50)
conta.mostrar_saldo()
