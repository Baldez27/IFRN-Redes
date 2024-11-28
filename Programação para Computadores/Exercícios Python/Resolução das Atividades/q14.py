n = int(input("Digite um número: "))

if n > 0:
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = (3 * n) + 1
        print(n)
else:
    print("Digite um número positivo.")