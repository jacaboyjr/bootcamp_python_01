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

CONTANTE_BONUS = 1000

#desafio - Calculo de Bonus com Entrada do Usuário
# Calculo de KPI do bônus de 2025 é de 1000 + salario + bonus
nome_funcionario = input("Digite o nome do funcionário: ")
salario = float(input("Digite o salário do funcionário: "))
porcentagem_bonus = float(input("Digite a porcentagem do bônus: "))
valor_bonus = CONTANTE_BONUS + salario * porcentagem_bonus
print(f"O valor do bônus para {nome_funcionario} é: {valor_bonus:.2f}")
