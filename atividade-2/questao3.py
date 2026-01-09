"""
3- Calculadora de Média Escolar
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.
"""

import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


nota1 = "vazio"
nota2 = "vazio"
nota3 = "vazio"

while nota1 == "vazio" or nota2 == "vazio" or nota3 == "vazio":
    try:
        if nota1 == "vazio":
            nota1 = float(input("Digite a primeira nota: "))
        if nota2 == "vazio":
            nota2 = float(input("Digite a segunda nota: "))
        if nota3 == "vazio":
            nota3 = float(input("Digite a terceira nota: "))
    except ValueError:
        input(
            "Entrada inválida. Certifique-se de digitar apenas números.\n\nExemplo: \n7.5\n\nConfirme com Enter"
        )
        limpar_tela()
    except KeyboardInterrupt:
        exit()


def calcular_media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return round(media, 2)


print(
    f"O aluno obteve as notas: \n{nota1}, \n{nota2}, \n{nota3}. \n\nA média final é {calcular_media(nota1, nota2, nota3)}"
)
