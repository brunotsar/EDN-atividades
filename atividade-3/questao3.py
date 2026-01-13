"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.

"""

import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def converter_temperatura(unidadeOrigem, unidadeDestino):
    while True:
        try:
            valor = float(input(f"Informe o valor da temperatura em {unidadeOrigem}: "))
        except ValueError:
            input(
                "Valor inválido. Por favor, informe um número válido de acordo com a unidade de origem.\n\n Aperte Enter para continuar..."
            )
            continue
        except KeyboardInterrupt:
            exit()
        break
    limpar_tela()
    print(f"A conversão de {valor} {unidadeOrigem} para {unidadeDestino} é:")
    match unidadeOrigem:
        case "Celsius":
            match unidadeDestino:
                case "Fahrenheit":
                    conversao = (valor * 9 / 5) + 32
                    return input(
                        f"{conversao:.2f)}°F\n\nAperte Enter para voltar para o Menu"
                    )
                case "Kelvin":
                    conversao = valor + 273.15
                    return input(
                        f"{conversao:.2f}K\n\nAperte Enter para voltar para o Menu"
                    )
                case "Ambas":
                    fahrenheit = (valor * 9 / 5) + 32
                    kelvin = valor + 273.15
                    return input(
                        f"{fahrenheit:.2f}°F, {kelvin:.2f}K\n\nAperte Enter para voltar para o Menu"
                    )
        case "Fahrenheit":
            match unidadeDestino:
                case "Celsius":
                    conversao = (valor - 32) * 5 / 9
                    return input(
                        f"{conversao:.2f}°C\n\nAperte Enter para voltar para o Menu"
                    )
                case "Kelvin":
                    conversao = (valor + 459.67) * 5 / 9
                    return input(
                        f"{conversao:.2f}K\n\nAperte Enter para voltar para o Menu"
                    )
                case "Ambas":
                    celsius = (valor - 32) * 5 / 9
                    kelvin = celsius + 273.15
                    return input(
                        f"{celsius:.2f}°C, {kelvin:.2f}K\n\nAperte Enter para voltar para o Menu"
                    )
        case "Kelvin":
            match unidadeDestino:
                case "Celsius":
                    conversao = valor - 273.15
                    return input(
                        f"{conversao:.2f}°C\n\nAperte Enter para voltar para o Menu"
                    )
                case "Fahrenheit":
                    conversao = (valor * 9 / 5) - 459.67
                    return input(
                        f"{conversao:.2f}°F\n\nAperte Enter para voltar para o Menu"
                    )
                case "Ambas":
                    celsius = valor - 273.15
                    fahrenheit = (valor * 9 / 5) - 459.67
                    return input(
                        f"{celsius:.2f}°C, {fahrenheit:.2f}°F\n\nAperte Enter para voltar para o Menu"
                    )


def temperatura_destino(unidadeOrigem):
    while True:
        limpar_tela()
        if unidadeOrigem == "Celsius":
            print(f"Gostaria de converter {unidadeOrigem} para:")
            print("1. Fahrenheit")
            print("2. Kelvin")
            print("3. Ambas")
            print("4. Voltar")

            try:
                opcao = int(input("Escolha uma opção: "))
            except ValueError:
                limpar_tela()
                input(
                    "Opção inválida, Digite de 0 a 4, \n\nAperte Enter para continuar..."
                )
                continue
            except KeyboardInterrupt:
                exit()
            match opcao:
                case 1:
                    converter_temperatura(unidadeOrigem, "Fahrenheit")
                    break
                case 2:
                    converter_temperatura(unidadeOrigem, "Kelvin")
                    break
                case 3:
                    converter_temperatura(unidadeOrigem, "Ambas")
                    break
                case 4:
                    break
                case _:
                    print("Opção inválida, Digite de 0 a 4")
                    continue

        elif unidadeOrigem == "Fahrenheit":
            print(f"Gostaria de converter {unidadeOrigem} para:")
            print("1. Celsius")
            print("2. Kelvin")
            print("3. Ambas")
            print("4. Voltar")

            try:
                opcao = int(input("Escolha uma opção: "))
            except ValueError:
                limpar_tela()
                input(
                    "Opção inválida, Digite de 0 a 4, \n\nAperte Enter para continuar..."
                )
                continue
            except KeyboardInterrupt:
                exit()
            match opcao:
                case 1:
                    converter_temperatura(unidadeOrigem, "Celsius")
                case 2:
                    converter_temperatura(unidadeOrigem, "Fahrenheit")
                case 3:
                    converter_temperatura(unidadeOrigem, "Ambas")
                case 4:
                    return "Voltar"
                case _:
                    print("Opção inválida, Digite de 0 a 4")
                    continue

        elif unidadeOrigem == "Kelvin":
            print(f"Gostaria de converter {unidadeOrigem} para:")
            print("1. Celcius")
            print("2. Fahrenheit")
            print("3. Ambas")
            print("4. Voltar")

        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            limpar_tela()
            input("Opção inválida, Digite de 0 a 4, \n\nAperte Enter para continuar...")
            continue
        except KeyboardInterrupt:
            exit()
        match opcao:
            case 1:
                converter_temperatura(unidadeOrigem, "Fahrenheit")
            case 2:
                converter_temperatura(unidadeOrigem, "Kelvin")
            case 3:
                converter_temperatura(unidadeOrigem, "Ambas")
            case 4:
                return "Voltar"
            case _:
                print("Opção inválida, Digite de 0 a 4")
                continue


while True:
    limpar_tela()
    print("Conversor de Temperatura\nEscolha a temperatura de origem:")
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    print("0. Sair")
    try:
        opcao = int(input("Escolha uma opção: "))
    except ValueError:
        limpar_tela()
        input(
            "Opção inválida. Por favor, insira um número de 0 a 3.\n\n Aperte Enter para continuar..."
        )
        continue
    except KeyboardInterrupt:
        exit()
    match opcao:
        case 1:
            temperatura_destino("Celsius")
        case 2:
            temperatura_destino("Fahrenheit")
        case 3:
            temperatura_destino("Kelvin")
        case 0:
            break
        case _:
            limpar_tela()
            input(
                "Opção inválida. Por favor, insira um número de 0 a 3.\n\n Aperte Enter para continuar..."
            )
            continue
