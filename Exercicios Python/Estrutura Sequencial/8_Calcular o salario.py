#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

valor_hora = float( input("Quanto você ganha por hora?") )
horas_trabalhadas = float( input("Quantas horas você trabalhou?") )

pagamento = valor_hora * horas_trabalhadas
print("Você trabalhou por", horas_trabalhadas,"horas")
print("O valor da hora trabalhada é de R$", valor_hora)
print("O pagamento deve ser recebido é de: R$", pagamento)

#Primeiro: A variavel VALOR_HORA serviu para a pessoa digitar quanto ela ganha por hora
#Segundo: A variavel HORAS_TRABALHADAS serviu para a pessoa digitar quantas horas ela trabalha
#Terceiro: A variavel pagamento serviu para multiplicar a varialvel VALOR_HORA pela a variavel HORAS_TRABALHADAS
#Quarto: A primeira função PRINT serviu para imprimir as suas horas trabalhadas
#Quinto: A segunda função PRINT serviu para imprimir o quanto você ganha por hora
#Sexto: a terceira função PRINT serviu para imprimir o quanto você deve receber no pagamento