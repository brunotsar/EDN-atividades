"""
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:

* Distância percorrida: 300 km
* Combustível gasto: 25 litros
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.
"""

import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


distanciaPercorrida = 0
combustivelGasto = 0

try:
    distanciaPercorrida = float(input("Digite a distância percorrida: "))
    combustivelGasto = float(input("Digite o combustível gasto: "))
except ValueError:
    input(
        "Entrada inválida. Certifique-se de digitar apenas números.\n\nExemplo: \n7.5\n\nConfirme com Enter"
    )
    limpar_tela()
except KeyboardInterrupt:
    exit()


def calcular_consumo(distancia, combustivel):
    consumo = distancia / combustivel
    return round(consumo, 2)


print(
    f"A distância percorrida foi de {distanciaPercorrida} km, \n"
    f"o consumo de combustível foi de {combustivelGasto} litros. \n\n"
    f"O consumo médio do veículo é {calcular_consumo(distanciaPercorrida, combustivelGasto)} km/l"
)
