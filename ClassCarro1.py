class carro:
    def __init__(self, marca, ano, opcional):
        self.marca = marca
        self.ano = ano
        self.opcional = opcional


carro1 = carro("Kia", 2020, "sem teto solar")
carro2 = carro("Fiat", 2023, "sem teto solar")
carro3 = carro("Ferrari", 2026, "com teto solar")


print(f"carro1:{carro1.marca},{carro1.ano},")
print(f"carro2:{carro2.marca},{carro2.ano},")
print(f"carro3:{carro3.marca},{carro3.ano},{carro3.opcional}")
