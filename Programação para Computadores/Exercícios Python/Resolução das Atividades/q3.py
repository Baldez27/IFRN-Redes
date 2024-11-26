somaQuadrados = 0
quadradosSoma = 0
n = 1
n1 = 1
soma = 0

#A soma dos quadrados
while (n <= 100):
    somaQuadrados += (n ** 2)
    # É a mesma coisa que: somaquadrados = somaquadrados + (n ** 2)
    n = n + 1

# O quadrado das somas
while (n1 <= 100):
    soma += n1

    if (n1 == 100):
        quadradosSoma = soma ** 2
    n1 = n1 + 1
diferenca = somaQuadrados - quadradosSoma

print("A diferença é de: ", diferenca)