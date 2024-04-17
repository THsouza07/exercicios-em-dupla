class Pessoa:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura
if __name__ == "__main__":
    pessoa1 = Pessoa("Thiago", "17 anos", "1,76")
    print(pessoa1.nome, pessoa1.idade, pessoa1.altura)        