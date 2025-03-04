class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def latir(self):
        print(f"{self.nome} está latindo! Au au!")


cachorro = Cachorro("Rex", 3)
cachorro.latir()
