import random

# Sorteando um número entre 1 e 100
numero_sorteado = random.randint(1, 100)

# Intervalo inicial
inicio = 1
fim = 100

print("=============== ===============")

print("Tente adivinhar o número sorteado entre 1 e 100. Você tem 4 tentativas.")

print("=============== ===============")

# Realiza até 4 tentativas
tentativa = 1
while tentativa <= 4:
    print(f"Tentativa {tentativa}: O intervalo atual é de {inicio} a {fim}.")
    palpite = int(input("Digite seu palpite: "))
    
    if palpite == numero_sorteado:
        print(f"Parabéns! Você acertou o número {numero_sorteado} na tentativa {tentativa}!")
        break
    elif palpite < numero_sorteado:
        print("O número sorteado é maior.")
        if palpite + 1 > inicio:
            inicio = palpite + 1  # Atualiza o início do intervalo
    else:
        print("O número sorteado é menor.")
        if palpite - 1 < fim:
            fim = palpite - 1  # Atualiza o fim do intervalo
    
    tentativa += 1

# Caso o usuário não acerte em 4 tentativas
if tentativa > 4:
    print(f"Suas tentativas acabaram. O número sorteado era {numero_sorteado}.")
