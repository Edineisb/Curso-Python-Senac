class Pessoa:
    def __init__(self, mone):
        self.nome = "nome"

    def apresenta(self):

        print(f"Olá, meu {self.nome} é: Maria")


maria = Pessoa("Maria")
maria.apresenta()
