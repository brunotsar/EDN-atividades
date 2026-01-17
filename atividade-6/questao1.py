"""
1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário
também escolha o tamanho da senha  para criar senhas seguras automaticamente.
"""

import os
import random
import string


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def gerar_senha(tamanho):
    characters = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(characters) for _ in range(tamanho))
    return senha


while True:
    try:
        tamanhoSenha = int(input("Digite o tamanho da senha: "))
        if tamanhoSenha < 8 or tamanhoSenha > 30:
            raise ValueError("Tamanho inválido")
        else:
            break
    except ValueError:
        input(
            "Entrada inválida. Por favor, digite um número inteiro entre 8 e 30.,\nAperte ENTER para continuar..."
        )
        limpar_tela()
        continue
    break
print("Senha gerada:", gerar_senha(tamanhoSenha))
