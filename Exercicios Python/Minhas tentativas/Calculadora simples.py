#Calculadora simples

operação = input('''
Por favor, digite a operação matemática que você gostaria de completar:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

numero_1 = int(input('coloque o primeiro número: '))
numero_2 = int(input('coloque o segundo número: '))

if operação == '+':
    print('{} + {} = '.format(numero_1, numero_2))
    print(numero_1 + numero_2)

elif operação == '-':
    print('{} - {} = '.format(numero_1, number_2))
    print(numero_1 - numero_2)

elif operação == '*':
    print('{} * {} = '.format(numero_1, numero_2))
    print(numero_1 * numero_2)

elif operação == '/':
    print('{} / {} = '.format(numero_1, numero_2))
    print(numero_1 / numero_2)

else:
    print('Você não digitou um operador válido, execute o programa novamente.')

#Primeiro: A variável OPERAÇÃO é uma string que armazena a operação matemática que o usuário deseja realizar. O usuário deve digitar um dos seguintes caracteres: '+', '-', '*', '/'.
#Segundo: As variáveis NUMERO_1 e NUMERO_2 são números inteiros que representam os valores com os quais a operação será realizada. O usuário é solicitado a inserir esses números por meio das funções input() e int().
#Terceiro: A estrutura condicional if-elif-else verifica qual operação foi selecionada pelo usuário com base no valor da variável operacao. Dependendo da operação selecionada, o código executa um bloco de código correspondente.
#Quarto: Se o valor de operacao for '+', o código exibe uma mensagem formatada mostrando a soma dos dois números fornecidos e o resultado da adição.
#Quinto: Se o valor de operacao for '-', o código exibe uma mensagem formatada mostrando a subtração do segundo número do primeiro e o resultado da subtração.
#Seto: Se o valor de operacao for '*', o código exibe uma mensagem formatada mostrando a multiplicação dos dois números e o resultado da multiplicação.
#Setimo: Se o valor de operacao for '/', o código exibe uma mensagem formatada mostrando a divisão do primeiro número pelo segundo e o resultado da divisão.
#Oitavo: Se o valor de operacao não corresponder a nenhum dos operadores válidos, o código exibe a mensagem "Você não digitou um operador válido, execute o programa novamente.".    