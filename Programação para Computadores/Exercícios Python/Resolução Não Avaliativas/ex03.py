#Esse código diz se um número é ou não um polídromo

valor = int(input("Digite um número: "))

unidade = valor % 10
n1 = valor // 10

dezena = valor % 10
n2 = valor // 10

centena = valor % 10
n3 = valor // 10

numero_invertido = n1 * 10 + unidade
numero_invertido = n2 * 10 + centena
numero_invertido = n3 * 10 + dezena

if valor == numero_invertido:
    print("Polidromo")
else:
    print("Não é políndromo")





texto = input("Digite algo: ")
if texto == texto[::-1]:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")