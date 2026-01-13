"""
2- Calculadora de IMC

Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

< 18.5: classificacao = "Abaixo do peso"
< 25: classificacao = "Peso normal"
< 30: classificacao = "Sobrepeso"
Para os demais cenários: classificacao = "Obeso"
"""

import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


while True:
    peso = "Nulo"
    altura = "Nulo"
    classificacao = "Nulo"
    try:
        if peso == "Nulo":
            peso = float(input("Digite o peso (em kg): "))
        if altura == "Nulo":
            altura = float(input("Digite a altura (em metros): "))
    except ValueError:
        input(
            "\nIdade inválida. Digite um número inteiro válido.\n\nExemplo: 18\n\nAperte Enter para continuar..."
        )
        limpar_tela()
        continue
    except KeyboardInterrupt:
        exit()

    imc = peso / (altura**2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    else:
        classificacao = "Obeso"

    print(f"\nIMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")
    input("\nAperte Enter para continuar...")
