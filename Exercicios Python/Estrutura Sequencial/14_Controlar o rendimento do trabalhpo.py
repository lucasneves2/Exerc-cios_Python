#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

peso = float(input("Digite o peso dos peixes em quilos"))

limite = 50.0  # Limite estabelecido pelo regulamento
excesso = 0.0  # Inicializa a variável excesso
multa_por_quilo = 4.00  # Valor da multa por quilo excedente
multa = 0.0  # Inicializa a variável multa

if peso > limite:
   excesso = peso - limite
   excesso * multa_por_quilo

print("Peso dos peixes", peso, "quilos")   

if excesso > 0:
   print("Excesso de peso: ", peso, "quilos")
   print("Valor da multa a ver pago: R$", multa)

else:   
   print("Dentro do limite de peso, não há multa a ser pago")