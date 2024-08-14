#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

bimestre_1 = float( input("Fale a nota do primeiro bimestre") )
bimestre_2 = float( input("Fale a nota do segundo bimestre") )
bimestre_3 = float( input("Fale a nota do terceiro bimestre") )
bimestre_4 = float( input("Fale a nota do quarto bimestre") )

media = (bimestre_1 + bimestre_2 + bimestre_3 + bimestre_4) / 4

print("A média desse estudante foi: ",media)

#Primeiro: Eu criei 4 Variaveis praticamente iguais para conseguir calcular a média
#Segundo: A função FLOAT serve para tranformar um número inteiro ou uma string numérica em um número com casas decimais
#Terceiro: A variavel MEDIA serviu para dividir as quatro variaveis do BIMESTRE e da a média
#Quatro: A função PRINT serviu para imprimir a média