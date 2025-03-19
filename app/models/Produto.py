class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def dicionario(self):
        return {"nome": self.nome, "preco": self.preco}