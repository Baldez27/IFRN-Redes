# Solicitando as notas das duas primeiras unidades
nota1 = float(input("Digite a nota da 1ª unidade: "))
nota2 = float(input("Digite a nota da 2ª unidade: "))

# Calculando a média das duas unidades
media = (nota1 + nota2) / 2

# Determinando se o aluno será aprovado ou reprovado
if media >= 6.0:
    print(f"Você foi aprovado com média {media:.1f}.")
elif media < 4.0:
    print(f"Você foi reprovado com média {media:.1f}.")
else:
    print(f"Você está em prova final com média {media:.1f}.")
    # Solicita a nota da prova final
    nota_final = float(input("Digite a nota da prova final: "))
    media_final = (media + nota_final) / 2
    
    # Determina a situação após a prova final
    if media_final >= 5.0:
        print(f"Você foi aprovado na prova final com média final {media_final:.1f}.")
    else:
        print(f"Você foi reprovado na prova final com média final {media_final:.1f}.")
