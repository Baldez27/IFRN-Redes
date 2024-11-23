# Solicita os valores de dia, mês e ano ao usuário
dia = int(input("Digite o dia (1-31): "))
mes = int(input("Digite o mês (1-12): "))
ano = int(input("Digite o ano: "))

# Verifica se o ano é bissexto
if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    bissexto = True
else:
    bissexto = False

# Defini os dias de cada mês, considerando se o ano é bissexto
if bissexto:
    dias_por_mes = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Ano bissexto
else:
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # Ano normal

# Verifica se o mês está dentro do intervalo válido
if mes < 1 or mes > 12:
    print("Erro: mês inválido. Deve ser entre 1 e 12.")
# Verifica se o dia é válido para o mês informado
elif dia < 1 or dia > dias_por_mes[mes - 1]:
    print(f"Erro: o mês {mes} não tem {dia} dias.")
else:
    # Calcula o dia juliano manualmente
    dia_juliano = 0  # Inicializa o acumulador de dias

    # Soma os dias dos meses anteriores
    for i in range(mes - 1):  # Vai de 0 até o mês anterior
        dia_juliano += dias_por_mes[i]

    # Adiciona os dias do mês atual
    dia_juliano += dia

    # Exibi o resultado
    print(f"A data {dia}/{mes}/{ano} corresponde ao dia juliano {dia_juliano}.")
