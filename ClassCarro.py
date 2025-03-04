class carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano


meu_carro = carro("Toyota", "Corolla", 2025)


print(f"{meu_carro.marca}")
print(f"{meu_carro.modelo}")
print(f"{meu_carro.ano}")
