"""
4- Verificador de Ano Bissexto

Faça um programa que determine se um ano inserido pelo usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos centenários (divisíveis por 100) que não são divisíveis por 400.
"""

import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def verificar_ano_bissexto(ano):
    if ano % 4 == 0:
        if ano % 100 == 0:
            if ano % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


while True:
    limpar_tela()
    try:
        ano = int(input("Digite um ano: "))
    except ValueError:
        print("Entrada inválida. Por favor, insira um número válido.\n\nExemplo: 2020")
        continue
    except KeyboardInterrupt:
        exit()

    if verificar_ano_bissexto(ano):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")

    print("\n\nDeseja sair? (s/n)")
    resposta = input().lower()
    if resposta == "s":
        break
    else:
        continue
