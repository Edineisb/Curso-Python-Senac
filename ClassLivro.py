class Livro:
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def detalhes(self):
        print(f"{self.titulo}, escrito por {self.autor} em {self.ano}")


livro = Livro("1984", "George Orwell", 1949)
livro.detalhes()
