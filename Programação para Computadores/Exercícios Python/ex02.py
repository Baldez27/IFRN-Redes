#Esse código faz a comparação de três valores e os coloca em ordem crescente

# Recebe três números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Ordenação manual dos números
if num1 > num2:
    num1, num2 = num2, num1
if num2 > num3:
    num2, num3 = num3, num2
if num1 > num2:
    num1, num2 = num2, num1

# Imprime os números ordenados
print("Os números em ordem crescente são:", num1, num2, num3)
