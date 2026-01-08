class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco


def calcular_valor_total(produto, quantidade):
    return produto.preco * quantidade


produto1 = Produto("Cadeira Infantil", 12.40)
quantidade = 3

print(
    f"Produto: \n{produto1.nome}\nQuantidade: {quantidade} \n\nValor Total: R${calcular_valor_total(produto1, quantidade):.2f}"
)
