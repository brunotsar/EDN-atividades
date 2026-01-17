"""
1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada
"""

import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    return valor_conta * (porcentagem_gorjeta / 100)


valorConta = None
porcentagemGorjeta = None
while True:
    limpar_tela()
    try:
        if valorConta is None:
            valorConta = float(input("Digite o valor total da conta: "))
        if porcentagemGorjeta is None:
            porcentagemGorjeta = float(
                input("Digite a porcentagem da gorjeta desejada: ")
            )
            if porcentagemGorjeta < 0 or porcentagemGorjeta > 100:
                porcentagemGorjeta = None
                raise ValueError(
                    "Porcentagem da gorjeta não pode ser negativa ou maior que 100%"
                )
        break
    except ValueError as e:
        if "could not convert" in str(e):
            e = "Use números numéricos"
        input(f"Entrada inválida.{e}.\nAperte Enter para continuar...")
        continue
    except KeyboardInterrupt:
        exit()

gorjeta = calcular_gorjeta(valorConta, porcentagemGorjeta)
print(f"O valor da gorjeta é: {gorjeta:.2f}")
