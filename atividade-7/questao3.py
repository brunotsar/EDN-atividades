"""
3 -  Crie um programa que leia um arquivo  informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela,
caso o arquivo não seja encontrado, mostre uma mensagem de erro.
"""

import csv
from pathlib import Path


def ler_arquivo(nome_arquivo):
    diretorio = Path(__file__).resolve().parent
    try:
        with open(
            diretorio / nome_arquivo, "r", newline="", encoding="utf-8"
        ) as arquivo:
            leitor = csv.reader(arquivo)
            for linha in leitor:
                print(linha)
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")


nomeArquivo = input("Digite o nome do arquivo: ")
ler_arquivo(nomeArquivo)
