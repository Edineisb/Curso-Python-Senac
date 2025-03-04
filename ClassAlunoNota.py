class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def aprovado(self):
        if self.nota >= 6:
            print(f"{self.nome} está Aprovado!")
        else:
            print(f"{self.nome} está Reprovado.")


aluno = Aluno("João", 7.5)
aluno.aprovado()
