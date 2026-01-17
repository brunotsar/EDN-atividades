"""
3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do
CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha.
"""

import os

import requests


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def buscar_endereco(cep):
    try:
        resposta = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        resposta.raise_for_status()
        if "erro" in resposta.json():
            return "CEP não encontrado"
        dados = resposta.json()
        logradouro = dados["logradouro"]
        bairro = dados["bairro"]
        cidade = dados["localidade"]
        estado = dados["uf"]
        return f"Logradouro: {logradouro}\nBairro: {bairro}\nCidade: {cidade}\nEstado: {estado}"
    except requests.HTTPError as e:
        if e.response.status_code == 400:
            return "Informe um CEP válido"
        return f"Erro ao buscar endereço: {e}"


while True:
    limpar_tela()
    print("Digite sair para encerrar o programa")
    cep = input("Digite o CEP: ")
    if cep.lower() == "sair":
        break
    endereco = buscar_endereco(cep)
    print(endereco)
    input("Pressione Enter para continuar...")
