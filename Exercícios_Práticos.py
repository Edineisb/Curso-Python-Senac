class computador:
    marca = "Dell"
    processador = "Intel core i7"
    ram = 12

pc1 = computador()
pc2 = computador()

pc2.ram = 16
pc2.marca = "HP"
pc2.processador = "AMD"




class carro:
    def __init__(self,marca,ano, opcional):
        
        self.marca = marca
        self.ano = ano
        self.opcional = opcional
        

carro1 = carro ("Kia", 2020, "sem teto")
carro2 = carro ("Fiat", 2023, "sem teto")    
carro3 = carro ("Ferrari", 2026, "teto solar")


print(f"carro1:{carro1.marca}, {carro1.ano}")
print(f"carro2:{carro2.marca}, {carro2.ano}")
print(f"carro3:{carro3.marca}, {carro3.ano},{carro3.opcional}")

class Carro:
    def __init__(self,marca,ano):
        self.marca = marca
        self.ano = ano

    def exibir__info(self):
        print(f"marca: {self.marca}, ano: {self.ano}") 

carro1 = carro("Fiat", 2020)        
carro1.exxibir_info()


    
    
    




    