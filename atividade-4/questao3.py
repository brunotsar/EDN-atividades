"""
3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número.
"""

import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def verificar_seguranca_senha(senha):
    if len(senha) < 8:
        input(
            "A senha deve ter pelo menos 8 caracteres.\nAperte Enter para continuar..."
        )
        limpar_tela()
        return False
    if not any(char.isdigit() for char in senha):
        input(
            "A senha deve conter pelo menos um número.\nAperte Enter para continuar..."
        )
        limpar_tela()
        return False
    return True


while True:
    senha = input("Digite sua senha: ")
    if senha.lower() == "sair":
        print("Operação cancelada.")
        exit()
    if verificar_seguranca_senha(senha):
        print("Senha válida!")
        break
