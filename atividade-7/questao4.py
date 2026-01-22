"""
4 -   Crie um programa que leia e escreva arquivos no formato , que salve em um dicionário com nome,
idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha.
"""

import json
import os
from pathlib import Path


def limpart_tela():
    os.system("cls" if os.name == "nt" else "clear")


def ler_arquivo_json(nomeArquivo):
    destinoDir = Path(__file__).resolve().parent
    try:
        with open(destinoDir / nomeArquivo, "r", encoding="utf-8") as arquivoJSON:
            dados = json.load(arquivoJSON)
            return dados
    except FileNotFoundError:
        input(f"Arquivo '{nomeArquivo}' não encontrado\nAperte Enter para continuar...")
    except json.JSONDecodeError:
        input(
            f"Erro ao decodificar o arquivo '{nomeArquivo}'\nAperte Enter para continuar..."
        )
    except Exception as e:
        input(
            f"Erro ao ler o arquivo '{nomeArquivo}': {str(e)}\nAperte Enter para continuar..."
        )
    return None


def escrever_arquivo_json(nomeArquivo, dados):
    destinoDir = Path(__file__).resolve().parent
    try:
        with open(destinoDir / nomeArquivo, "w", encoding="utf-8") as arquivoJSON:
            json.dump(dados, arquivoJSON, indent=4, ensure_ascii=False)
            return input("Dados escritos com sucesso\nAperte Enter para continuar...")
    except FileNotFoundError:
        input(f"Arquivo '{nomeArquivo}' não encontrado\nAperte Enter para continuar...")
    except Exception as e:
        input(
            f"Erro ao ler o arquivo '{nomeArquivo}': {str(e)}\nAperte Enter para continuar..."
        )
    return None


dados = {"nome": "João", "idade": 30, "cidade": "São Paulo"}

while True:
    limpart_tela()
    print("Escolha uma opção:")
    print("1 - Ler arquivo")
    print("2 - Escrever arquivo")
    print("3 - Sair")
    opcao = input("Opção: ")

    match opcao:
        case "1":
            nomeArquivo = input("Digite o nome do arquivo: ")
            input(
                f"Dados: {ler_arquivo_json(nomeArquivo)}\nAperte Enter para continuar..."
            )
        case "2":
            nomeArquivo = input("Digite o nome do arquivo: ")
            escrever_arquivo_json(nomeArquivo, dados)
            input("Aperte Enter para continuar...")
        case "3":
            break
        case _:
            input("Opção inválida\nAperte Enter para continuar...")
