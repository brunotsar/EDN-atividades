"""
2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""


class Produto:
    def __init__(self, nome, valor, desconto):
        self.nome = nome
        self.valor = valor
        self.desconto = desconto


def calcular_desconto(produto):
    desconto = produto.valor * produto.desconto / 100
    preco_final = produto.valor - desconto
    return round(preco_final, 2)


camiseta = Produto("Camiseta", 50.00, 20)
preco_final = calcular_desconto(camiseta)
print(f"Produto: {camiseta.nome}")
print(f"Preço original: R$ {camiseta.valor:.2f}")
print(f"Desconto: {camiseta.desconto}%")
print(f"Preço final: R$ {preco_final}")
