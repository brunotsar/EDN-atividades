"""
2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório.
Exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha.
"""

import requests


def buscar_usuario():
    try:
        resposta = requests.get("https://randomuser.me/api/")
        resposta.raise_for_status()
        dados = resposta.json()
        usuario = dados["results"][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario["email"]
        pais = usuario["location"]["country"]
        return f"Nome: {nome}\nE-mail:{email}\nPaís: {pais}"
    except requests.RequestException as e:
        print(f"Erro ao buscar usuário: {e}")


print(buscar_usuario())
