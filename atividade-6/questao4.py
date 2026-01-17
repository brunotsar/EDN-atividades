"""
4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual,
máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro.
"""

import os

import requests


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def buscar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if moeda == "USDT":
            cotacao = data["USDBRLT"]
        else:
            cotacao = data[f"{moeda}BRL"]
        return (
            float(cotacao["bid"]),
            float(cotacao["high"]),
            float(cotacao["low"]),
            cotacao["create_date"],
        )
    else:
        return None, None, None, None


def lista_moedas():
    url = "https://economia.awesomeapi.com.br/json/all"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        formatado = ", ".join(data.keys())
        return formatado
    else:
        return None


while True:
    limpar_tela()
    print(f"Escolha uma dessas moedas:\n{lista_moedas()}\n")
    print("Digite sair para encerrar o programa")
    moeda = input("Digite a moeda: ")
    if moeda.lower() == "sair":
        break
    valor, maximo, minimo, data = buscar_cotacao(moeda.upper())
    if valor is not None:
        print(f"Cotação atual: {valor}")
        print(f"Máxima: {maximo}")
        print(f"Mínima: {minimo}")
        print(f"Data/hora da última atualização: {data}")
    else:
        print("Moeda não encontrada ou erro na requisição")
    input("Pressione Enter para continuar...")
