# Solicita ao usuário um número de até 4 digitos
numero = int(input("Digite um número de até 4 dígitos: "))

# Verifica se o número está dentro do intervalo
if 0 <= numero <= 9999:
    soma = 0

    # Soma os algarismos do número
    while numero > 0:
        soma = soma + (numero % 10)  #Pega o último dígito e adiciona à soma
        numero = numero // 10  #Remove o último dígito do número

    # Exibe a soma dos algarismos após o fim do loop
    print(f"A soma dos algarismos é {soma}.")
else:
    print("Número inválido. Por favor digite um número entre 0 e 9999.")
