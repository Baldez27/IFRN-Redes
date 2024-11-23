# Solicitando o ano ao usuário
ano = int(input("Digite um ano: "))

# Esse código verifica se o ano é bissexto
# Um ano é bissexto se for divisível por 400 ou por 4 (mas não por 100).

if (ano % 400 == 0):  # Caso 1: Divisível por 400, é sempre bissexto
    print(f"O ano {ano} é bissexto.")
elif (ano % 4 == 0 and ano % 100 != 0):  
    # Caso 2: Divisível por 4, mas não por 100, também é bissexto
    print(f"O ano {ano} é bissexto.")
else:
    # Caso contrário, o ano não é bissexto
    print(f"O ano {ano} não é bissexto.")
