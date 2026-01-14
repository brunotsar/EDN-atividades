"""
1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).
"""

import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def menu():
    limpar_tela()
    print("Escolha uma opção:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")
    print("5 - Sair")
    try:
        escolha = int(input("\nEscolha:"))
        match escolha:
            case 1:
                calculadora("+")
            case 2:
                calculadora("-")
            case 3:
                calculadora("*")
            case 4:
                calculadora("/")
            case 5:
                print("Saindo...")
                exit()
            case _:
                input(
                    "Opção inválida!,escolha de 1 a 5.\nAperte ENTER para continuar..."
                )
                limpar_tela()
                menu()
    except ValueError:
        input(
            "Erro: Entrada inválida!, escolha de 1 a 5.\nAperte ENTER para continuar..."
        )
        limpar_tela()
        menu()
    except KeyboardInterrupt:
        exit()


def calculadora(operacao):
    limpar_tela()
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))

            if operacao == "+":
                resultado = num1 + num2
            elif operacao == "-":
                resultado = num1 - num2
            elif operacao == "*":
                resultado = num1 * num2
            else:
                resultado = num1 / num2

            print(f"Resultado: {resultado}")
            while True:
                escolha = input("Deseja fazer outra operação? (s/n): ")
                if escolha.lower() == "s":
                    limpar_tela()
                    break
                elif escolha.lower() == "n":
                    exit()
                else:
                    print("Opção inválida!, escolha apenas 's' ou 'n'.")
                    continue

        except ZeroDivisionError:
            input(
                "Erro: Divisão por zero!, Tá achando que é alquimista?\nAperte ENTER para continuar..."
            )
            limpar_tela()
            continue
        except ValueError:
            input(
                "Erro: Entrada inválida!, escolha apenas números,Exemplo: 10 ou 10.5.\nAperte ENTER para continuar..."
            )
            limpar_tela()
            continue
        except KeyboardInterrupt:
            exit()


while True:
    menu()
