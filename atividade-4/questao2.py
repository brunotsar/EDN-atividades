"""
2 - Criar um código que registre as notas de alunos e calcular a média da turma.
"""

import os


def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")


def calcular_media_notas():
    notas = []
    while True:
        try:
            nota = input(
                f"Digite uma nota de 0 a 10 (ou 'fim' para encerrar) Nota {len(notas) + 1}: "
            )
        except KeyboardInterrupt:
            exit()
        if nota.lower() == "fim":
            break
        try:
            nota = float(nota)
            if nota < 0 or nota > 10:
                input(
                    "Nota inválida! Digite um número entre 0 e 10.\nDigite ENTER para continuar..."
                )
                limpar_tela()
            else:
                notas.append(nota)
        except ValueError:
            input(
                "Nota inválida! Digite um número entre 0 e 10.\nDigite ENTER para continuar..."
            )
            limpar_tela()

    if len(notas) == 0:
        print("Nenhuma nota foi registrada.")
    else:
        media = sum(notas) / len(notas)
        print(f"A média dentre {len(notas)} notas é: {media:.2f}")


calcular_media_notas()
