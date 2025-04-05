class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        return f"nome: {self.nome}, idade: {self.idade} anos"
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, matricula):
        super().__init__(nome, idade)
        self.matricula = matricula

    def exibir_dados(self):
        return f"{super().exibir_dados()}, matricula: {self.matricula}"
    
pessoa = Pessoa("Edinei Bonfim", 40)
aluno = Aluno("Marcos Souza", 20, "A12345") 

print(pessoa.exibir_dados())
print(aluno.exibir_dados())
        




