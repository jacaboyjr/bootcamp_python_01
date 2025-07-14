# Execicio 01 - Crie um programa que o usuário digite seu nome e retorna o numero de caracteres do nome.
'''nome = input("Digite seu nome: ")
print(f"Seu nome tem {len(nome)} caracteres.")


# Execicio 02 - Crie um programa que o usuário digite seu nome e retorne o nome em letras maiúsculas.
nome = input("Digite seu nome: ")
print(f"Seu nome em maiúsculas é: {nome.upper()}")

#soma
valor_01 = float(input("Digite o primeiro valor: "))
valor_02 = float(input("Digite o segundo valor: "))
soma = valor_01 + valor_02
print(f"A soma dos dois valores é: {soma}")
'''
#desafio - Calculo de Bonus com Entrada do Usuário
# Calculo de KPI do bônus de 2025 é de 1000 + salario + bonus
nome_funcionario = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))
porcentagem_bonus = float(input("Digite a porcentagem do bônus: "))
valor_bonus = salario * (porcentagem_bonus / 100)
kpi_bonus = 1000 + salario + valor_bonus
print(f"O valor do bônus é {valor_bonus:.2f}")
print(f"O KPI do bônus de 2025 para {nome_funcionario} é: {kpi_bonus:.2f}")
