soma = 0
i = 1

# Loop que vai contar de 1 até 1000
while(i <= 1000):
    # Verifica se o número é multiplo de 2 ou 5
    if i % 3 == 0 or i % 5 == 0:
        soma = soma + 1
    i = i + 1
print(f"A soma dos multiplos de 5 ou 3 é igual a {soma}")