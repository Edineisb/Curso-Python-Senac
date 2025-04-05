class Funcionario:
     def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

        def exibir_info(self):
            print(f"Nome: {self.nome}")
            print(f"Salario: R$ {self.salario}")

class Gerente(Funcionario):
    def __init__(self, nome, salario, departamento):
        super().__init__(nome, salario)
        self.departamento = departamento
     
     
    
                   
     
    


    
                  