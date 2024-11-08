def calcular_troco(valor_conta, valor_pagamento):
    # Calcula o troco
    troco = valor_pagamento - valor_conta

    if valor_pagamento < valor_conta:
        return "Pagamento insuficiente."

    # Valores das Cédulas em reais
    todas_cedulas = [200, 100, 50, 20, 10, 5, 2, 1]

    # Dicionário para armazenar a quantidade de cada cédula
    quantidade_cedulas_troco = {}

    # Calculando a quantidade de cédulas
    for cedula in todas_cedulas:
        quantidade = troco // cedula

        if quantidade > 0:
            quantidade_cedulas_troco[cedula] = quantidade
            troco -= quantidade * cedula

    return quantidade_cedulas_troco

def main():
    # Entrada do valor da conta e do pagamento
    conta = float(input("Digite o valor da conta do Restaurante (R$): "))
    pagamento = float(input("Digite o valor que você vai pagar (R$): "))

    # Chama a função para calcular o troco
    resultado = calcular_troco(conta, pagamento)

    # Verifica se o troco foi calculado ou se o pagamento é insuficiente
    if isinstance(resultado, str):
        print(resultado)
    else:
        print(f"\nO seu troco será: R$ {pagamento - conta:.2f}")
        print("Troco em cédulas:")
        for cedula, quantidade in resultado.items():
            print(f"R${cedula:.2f}: {quantidade} cédula(s)")

if __name__ == "__main__":
    main()
