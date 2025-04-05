class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def aprovado(self):    
        if self.nota >= 6:
            print(f"{self.nome} está Aprovado!")
        else:
            print(f"{self.nome} está Reprovado.")

aluno = Aluno("Edinei", 7.5)                
aluno.aprovado()

#Exercício8

class Banco:
    def __init__(self, saldo_ininial):
        self.saldo = saldo_ininial
    
        
        

