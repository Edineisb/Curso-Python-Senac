class Funcionario:
    def __init__(self, nome, cargo, salario):
        self.nome = nome
        self.cargo = cargo
        self.salario = salario

    def aumentar_salario(self, porcentagem):
        aumento = self.salario * (porcentagem / 100)
        self.salario += aumento
        print(
            f"Salário aumentado em {porcentagem}%. Novo salário: R$ {self.salario:.2f}")


funcionario = Funcionario("Ana", "Gerente", 5000)
funcionario.aumentar_salario(10)
