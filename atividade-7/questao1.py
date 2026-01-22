"""
1 -  Crie um programa que lê um arquivo CSV de  com a biblioteca , calcule e exiba a  e o  da coluna tempo_execucao,
caso e o arquivo não exista ou houver erro na leitura, mostre uma mensagem de erro.
"""

from pathlib import Path

import pandas as pd


def processar_logs_treinamento(arquivoLog):
    destinoDir = Path(__file__).resolve().parent
    try:
        leitor = pd.read_csv(destinoDir / arquivoLog)
        media = leitor["tempo_execucao"].mean()
        desvioPadrao = leitor["tempo_execucao"].std()
        return f"Média: {media:.2f}\nDesvio padrão: {desvioPadrao:.2f}"
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")


arquivo = input("Digite o nome do arquivo: ").strip()
print(processar_logs_treinamento(arquivo))
