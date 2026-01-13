"""
1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais).
"""

import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    try:
        idade = int(input("Digite a idade: "))
    except ValueError:
        input(
            "Idade inválida. Digite um número inteiro válido.\n\nExemplo: 18\n\nAperte Enter para continuar..."
        )
        limpar_tela()
        continue

    if idade < 0 or idade > 160:
        if idade < 0:
            print("\nO programa não foi implementado para viajantes do tempo.")
        else:
            print("\nO programa não foi implementado para dinossauros.")
        input(
            "\nIdade inválida. Digite um número inteiro válido.\n\nExemplo: 18\n\nAperte Enter para continuar..."
        )
        limpar_tela()
        continue
    elif idade <= 12:
        categoria = "Criança"
    elif idade <= 17:
        categoria = "Adolescente"
    elif idade <= 59:
        categoria = "Adulto"
    else:
        categoria = "Idoso"

    print(f"A idade {idade} anos corresponde à categoria {categoria}.")
    break
