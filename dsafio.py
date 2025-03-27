# Calculo do bonus com entrada do usuario

nome_usuario =  input("Digite seu nome: ")
salario_usuario = float(input("Digite seu salario: "))
porcentagem_bonus = float(input("Digite a porcentagem do bonus: "))
bonus = salario_usuario * (porcentagem_bonus / 100)
print(f"Olá {nome_usuario}, seu bonus é de: R$ {bonus:.2f}")

# total do salario com bonus
salario_total = salario_usuario + bonus
print(f"Seu salario total é de: R$ {salario_total:.2f}")


