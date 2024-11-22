# Solicitando dados do usuário
peso = float(input("Digite o peso em kg: "))
altura_cm = float(input("Digite a altura em cm: "))

# Convertendo altura para metros
altura_m = altura_cm / 100

# Calculando o IMC
imc = peso / (altura_m ** 2)
imc = round(imc, 1)  # Arredondar para uma casa decimal

# Determinando o grau de obesidade com base no IMC
if imc < 18.5:
    situacao = "Abaixo do peso"
elif 18.5 <= imc < 24.9:
    situacao = "Peso normal"
elif 25.0 <= imc < 29.9:
    situacao = "Sobrepeso"
elif 30.0 <= imc < 34.9:
    situacao = "Obesidade grau I"
elif 35.0 <= imc < 39.9:
    situacao = "Obesidade grau II"
else:  # IMC >= 40.0
    situacao = "Obesidade grau III"

# Exibindo resultados
print(f"Seu IMC é {imc}")
print(f"Situação: {situacao}")
