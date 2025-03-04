class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def eh_valido(self):
        if (self.lado1 + self.lado2 > self.lado3 and
            self.lado1 + self.lado3 > self.lado2 and
                self.lado2 + self.lado3 > self.lado1):
            print("Os lados formam um triangulo válido.")
        else:
            print("Os lados não formam um triangulo válido.")


triangulo = Triangulo(3, 4, 5)
triangulo.eh_valido()
