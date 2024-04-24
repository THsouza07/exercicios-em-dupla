class Livro:
    def __init__(self, titulo, autor, num_paginas):
        self.titulo = titulo
        self.autor = autor
        self.num_paginas = num_paginas

    def mostrar_informacoes(self):
        print("Titulo:", self.titulo)
        print("Autor:", self.autor)
        print("Número de páginas:", self.num_paginas)  

    def calcular_palavras_por_pagina(self):
        return 325
    def solicitar_informacoes_livro():
        titulo = input("insira o titulo do livro: ")
        autor = input("insira o nome do autor do livro: ")
        num_paginas = input("insira o numero de paginas do livro: ")
        return Livro(titulo, autor, num_paginas)
    def main():
        livro = "solicitar_informacoes_livro"()
        livro. mostrar_informacoes()    
        palavras_por_paginas = livro.calcular_palavras_por_paginas()
        print("Quantidade de palavras por página:", "palavras_por_pagina")

    if __name__ == "__main__":
        main()      
