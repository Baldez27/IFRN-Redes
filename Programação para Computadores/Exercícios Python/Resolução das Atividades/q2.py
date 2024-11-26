import math

i = 1
resultado = 1

while(i <= 20):
    resultado = abs(resultado * i) // math.gcd(resultado, i)
    i = i + 1
print(f"O menor número divisivel por todos os numeros de 1 até 20 é {resultado}")