"""
4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos.
"""

import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def analisar_numeros(numero, pares, impares):
    try:
        numero = int(numero)
    except ValueError:
        input(
            "Entrada inválida. Digite apenas números inteiros.\nAperte ENTER para continuar..."
        )
        limpar_tela()
        return pares, impares

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    return pares, impares


pares = 0
impares = 0

while True:
    numero = input("Digite um número (ou 'sair' para encerrar): ")
    if numero.lower() == "sair":
        break
    pares, impares = analisar_numeros(numero, pares, impares)


print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
