class livro:
    def __init__(self, titulo, autor, ano_publicacao) -> None:
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
    def descricao(self):
        return f"Titulo:  {self.titulo}, autor: {self.autor}, ano de publicaçao: {self.ano_publicacao}"
livro1 = livro("Batata", "batatinha", 2023)
livro2 = livro("atata", "taata", 2023)

print(livro1.descricao())
print(livro2.descricao())
    