class Filme:
    def __init__(self, Titulo, Genero, Duração):
        self.Titulo = Titulo
        self.Genero = Genero
        self.Duração = Duração


filme1 = Filme("Covil de Ladrões", "Ação", 120)

filme1.Titulo = "Covil de Ladrões2"
filme1.Duração = 148

print(f"{filme1.Titulo}")
print(f"{filme1.Genero}")
print(f"{filme1.Duração}")
