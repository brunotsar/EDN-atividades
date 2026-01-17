"""
2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação).
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

import os
import string
import unicodedata


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def remover_acentos(texto: str) -> str:
    return "".join(
        char
        for char in unicodedata.normalize("NFD", texto)
        if unicodedata.category(char) != "Mn"
    )


def identificar_palindromo(palavra: str) -> bool:
    palavra = palavra.lower()
    palavra = remover_acentos(palavra)
    tradutor = str.maketrans("", "", string.punctuation + " ")
    palavra = palavra.translate(tradutor)
    print(f"Palavra original: {palavra}")
    print(f"Palavra invertida: {palavra[::-1]}")
    return palavra == palavra[::-1]


palavra = None
while palavra == "" or palavra is None:
    limpar_tela()
    palavra = input("Digite uma palavra ou frase para verificar se é um palíndromo: ")
    if palavra == "" or palavra.isalnum():
        input(
            "Por favor, digite uma palavra ou frase válida.\nAperte ENTER para continuar..."
        )
        palavra = None

if identificar_palindromo(palavra):
    print("Sim")
else:
    print("Não")
