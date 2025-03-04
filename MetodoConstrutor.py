class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


joao = Pessoa("João", 30)
print(f"Pessoa:{joao.nome}, {joao.idade}")
