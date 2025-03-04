class aluno:
    def __init__(self, nome, idade, curso):
        self.nome = nome
        self.idade = idade
        self.curso = curso


aluno1 = aluno("loão", 18, "curso Engenharia")
aluno2 = aluno("Maria", 22, "curso Medicina")

print(f"aluno1:{aluno1.nome}, {aluno1.idade}, {aluno1.curso}")
print(f"aluno2:{aluno2.nome}, {aluno2.idade}, {aluno2.curso}")
