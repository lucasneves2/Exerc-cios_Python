#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, 
#sabendo-se que são descontados 
#11% para o Imposto de Renda
#8% para o INSS 
#5% para o sindicato

#faça um programa que nos dê:
#Salário bruto.
#Quanto pagou ao INSS.
#Quanto pagou ao sindicato.
#O salário líquido.
#Calcule os descontos e o salário líquido, conforme a tabela abaixo:

#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$

#Obs.: Salário Bruto - Descontos = Salário Líquido.

# Obter o valor do salário por hora
valor_hora = float( input("Quanto você ganha por hora?"))

# Obter o número de horas trabalhadas no mês
horas_trabalhadas = float( input("Quantas horas você trabalhou no mês?"))

# Calcular o salário bruto
salario_bruto = valor_hora * horas_trabalhadas

# Calcular o valor do Imposto de Renda
ir = salario_bruto * 0.11

# Calcular o valor do INSS
inss = salario_bruto * 0.08

# Calcular o valor do sindicato
sindicato = salario_bruto * 0.05

# Calcular o salário líquido
salario_liquido = salario_bruto - ir - inss - sindicato

# Imprimir os resultados
print("+ Salário Bruto: R$", salario_bruto)
print("- IR (11%): R$", ir)
print("- INSS (8%): R$", inss)
print("- Sindicato (5%): R$", sindicato)
print("= Salário Líquido: R$", salario_liquido)

