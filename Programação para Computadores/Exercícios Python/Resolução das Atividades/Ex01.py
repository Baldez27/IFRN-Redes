limite = int(input("Digite o limite: "))

soma = 0
i = 1

while i <= limite:
    soma = soma + i
    i = i + 1
    print(soma)

print(soma)



ndiv = 0
div = 1

while div <= 71:
    if 71 % div == 0:
        ndiv = ndiv + 1
    div = div + 1

if ndiv == 2:
    print("71 é primo")