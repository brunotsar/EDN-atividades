"""
4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia.
"""

import datetime
import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def calcular_dias_vivo(dataNascimento):
    dataAtual = datetime.date.today()
    diasVivo = (dataAtual - dataNascimento).days
    return diasVivo


while True:
    limpar_tela()
    dataNascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    try:
        dataNascimentoFormatado = datetime.datetime.strptime(
            dataNascimento, "%d/%m/%Y"
        ).date()
        if (
            dataNascimentoFormatado > datetime.date.today()
            and dataNascimentoFormatado < datetime.date(1900, 1, 1)
        ):
            raise ValueError()
    except ValueError:
        print("Formato de data inválido. Use dd/mm/aaaa.")
        continue
    dias_vivo = calcular_dias_vivo(dataNascimentoFormatado)
    print(f"Você está vivo há {dias_vivo} dias.")
    break
