"""
1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.
"""

taxaDoDol = 5.37
taxaDoEuro = 6.25


def converter_moeda(valorEmReais, escolha):
    if escolha == 1:
        dolares = valorEmReais / taxaDoDol
        return round(dolares, 2)
    else:
        euros = valorEmReais / taxaDoEuro
        return round(euros, 2)


while True:
    try:
        valorEmReais = float(input("Digite o valor que você tem agora:"))
    except ValueError:
        print(
            "\nValor inválido, tente novamente. \n\nSiga o exemplo abaixo:\n100.00\n\n"
        )
        continue
    break

print("_______________________________________")
print(
    f"\nSaldo em conta: \nR$ {valorEmReais:.2f} \n\nConversões: \nDólares: ${converter_moeda(valorEmReais, 1)} \nEuros: €{converter_moeda(valorEmReais, 2)}"
)
