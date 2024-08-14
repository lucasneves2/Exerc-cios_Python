#Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
#Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
#Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
#comprar apenas latas de 18 litros;
#comprar apenas galões de 3,6 litros;
#misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

import math

# Solicita o tamanho da área a ser pintada
area_a_ser_pintada = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calcula a quantidade de tinta em litros necessária para a área informada
quantidade_tinta_litros = area_a_ser_pintada / 6 * 1.1  # Adiciona 10% de folga

# Calcula a quantidade de latas e galões necessários
latas = math.ceil(quantidade_tinta_litros / 18)
galoes = math.ceil(quantidade_tinta_litros / 3.6)

# Calcula os preços para cada situação
preco_latas = latas * 80
preco_galoes = galoes * 25

# Encontra a combinação que minimiza o desperdício
latas_mistas = int(quantidade_tinta_litros // 18)
galoes_mistos = math.ceil((quantidade_tinta_litros % 18) / 3.6)
preco_misto = (latas_mistas * 80) + (galoes_mistos * 25)

# Mostra os resultados ao usuário
print(f"Comprando apenas latas de 18 litros:")
print(f"Quantidade de latas: {latas}, Preço: R$ {preco_latas:.2f}")

print(f"\nComprando apenas galões de 3,6 litros:")
print(f"Quantidade de galões: {galoes}, Preço: R$ {preco_galoes:.2f}")

print(f"\nMisturando latas e galões:")
print(f"Quantidade de latas: {latas_mistas}, Quantidade de galões: {galoes_mistos}, Preço: R$ {preco_misto:.2f}")


#O "f" antes das aspas em uma string é utilizado para criar uma f-string (format string) em Python. 
#Uma f-string permite que você insira expressões dentro de strings, onde as expressões são avaliadas 
#e seus resultados são incorporados à string. Isso torna a formatação de strings mais conveniente 
#e legível.