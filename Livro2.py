class Livro:
    def __init__(self,titulo):
        self._titulo = titulo

    def definir_titulo(self, novo_titulo):
        if isinstance(novo_titulo, str) and len(novo_titulo) > 0:
            self._titulo = novo_titulo
        else:
            print("Titulo inválido!")
    def obter_titulo(self):
                return self._titulo

livro = Livro("O Senhor dos Anéis!")

print("Tituloi:", livro.obter_titulo())


livro.definir_titulo("Harry Potter")
print("Novo Titulo::", livro.obter_titulo())

livro.definir_titulo("")

        
        
           
        