##Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float(input("Informe a sua altura"))
peso_ideal = (72.7*altura) - 58

altura_2 = float(input("Informe a sua altura"))
peso_ideal_2 = (62.1*altura_2) -44.7

print("Seu peso ideal :é", peso_ideal)
print("Seu peso ideal é:", peso_ideal_2)


