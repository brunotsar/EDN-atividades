"""
3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado.
"""

import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def calcular_preco_final(preco: float, desconto: float) -> float:
    desconto = preco * (desconto / 100)
    precoFinal = preco - desconto
    return round(precoFinal, 2)


preco = None
desconto = None

while True:
    limpar_tela()
    try:
        if preco is None:
            preco = float(input("Digite o preço do produto: "))
            if preco <= 0:
                preco = None
                raise ValueError("Preço inválido. Não pode ser negativo ou zero")
        if desconto is None:
            desconto = float(input("Digite o desconto em porcentagem: "))
            if desconto < 0 or desconto > 100:
                desconto = None
                raise ValueError(
                    "Desconto inválido. Não pode ser negativo ou maior que 100%"
                )
    except ValueError as e:
        if "could not convert" in str(e):
            e = "Valor inválido, use números"
        input(f"{e}. Tente novamente.\nAperte ENTER para continuar...")
        continue
    except KeyboardInterrupt:
        exit()
    break

preco_final = calcular_preco_final(preco, desconto)
print(f"Preço final: R${preco_final:.2f}")
