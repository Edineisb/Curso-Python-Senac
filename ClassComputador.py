class Computador:
    def __init__(self, marcar, processador, ram):
        self.marca = marcar
        self.processador = processador
        self.ram = ram


pc1 = Computador("Dell", "Intel", 8)
pc2 = Computador("Dell", "Intel", 8)

pc2.ram = 16

print(f"pc1:{pc1.marca}, {pc1.processador},{pc1.ram}")
print(f"pc2:{pc2.marca}, {pc2.processador},{pc2.ram}")
