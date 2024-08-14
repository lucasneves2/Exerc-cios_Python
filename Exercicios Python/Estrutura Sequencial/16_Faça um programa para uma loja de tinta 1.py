#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
#Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

# Solicita ao usuário o tamanho em metros quadrados da área a ser pintada
area_a_pintar = float(input("Digite o tamanho da área a ser pintada (em metros quadrados): "))

# Calcula a quantidade de litros de tinta necessários
litros_tinta = math.ceil(area_a_pintar / 3)
# Cell e para arredondar para cima os números

# Calcula a quantidade de latas de tinta necessárias
latas_tinta = math.ceil(litros_tinta / 18)

# Calcula o preço total das latas de tinta
preco_total = latas_tinta * 80.00

# Exibe a quantidade de latas de tinta e o preço total
print("Quantidade de latas de tinta a serem compradas:", latas_tinta)
print("Preço total das latas de tinta: R$", preco_total)
