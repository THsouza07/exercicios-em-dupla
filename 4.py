class Produto:
    def __init__(self, nome, preço, quantidade):
        self.nome = nome
        self.preço = preço
        self.quantidade = quantidade
    if __name__ == "__main__":
        produto1 = Produto("Detergente", "R$2,25", "200")
        produto2 = Produto("Macarrão", "3,00", "130")
        print(produto1.nome, produto1.preço,produto1.quantidade)
        print(produto2.nome, produto2.preço, produto2.quantidade)