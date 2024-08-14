#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

n1 = int(input('1o Número inteiro: '))
n2 = int(input('2o Número inteiro: '))
n3 = float(input('Número real: '))

print ('Soma:', ((2*n1) * (n2/2)))
print ('Produto:', (3 * n1) + n3)
print ('Cubo:', n3**3)

#Primeiro: A variavel N1 serviu para a pessoa informar o primeiro número inteiro
#Segundo: A variavel N2 serviu para a pessoa informar o segundo número inteiro
#Terceiro: A variavel N3 serviu para a pessoa informar o número real
#Quatro: A primeira função PRINT serviu para multiplicar a variavel N1 por 2 depois multiplicar a variavel N2 dividida por 2
#Quinto: A segundo função PRINT serviu para multiplicar a variavel N1 por 3 e somar com a variavel N3
#Sexto: A terceira função PRINT serviu para elevar a função N3 por 3