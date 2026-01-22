"""
2 - Crie um programa que cria um arquivo  com nome,idade e cidade de algumas pessoas,
que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário,
caso ocorra um erro ao salvar, mostre uma mensagem de falha.
"""

from pathlib import Path

import pandas as pd


def escrever_csv(nomeArquivo, dados):
    destinoDir = Path(__file__).resolve().parent
    try:
        destinoDir = destinoDir / nomeArquivo
        if destinoDir.suffix == "":
            destinoDir = destinoDir.with_suffix(".csv")
            nomeArquivo = destinoDir
        else:
            nomeArquivo = destinoDir

        df = pd.DataFrame(dados)
        df.to_csv(
            nomeArquivo,
            index=False,
        )
    except Exception as e:
        print(f"Erro ao salvar os dados: {e}")
    return f"Arquivo salvo com sucesso na pasta:\n{destinoDir}"


dados = [
    {"nome": "João", "idade": 25, "cidade": "São Paulo"},
    {"nome": "Maria", "idade": 30, "cidade": "Rio de Janeiro"},
    {"nome": "Pedro", "idade": 22, "cidade": "Belo Horizonte"},
]
nomeArquivo = input("Digite o nome do arquivo: ").strip()
print(escrever_csv(nomeArquivo, dados))
