#Faça um programa que peça o tamanho de um arquivo para download (em MB) 
#e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download 
#do arquivo usando este link (em minutos).

mb = float(input("Digite o tamanho do arquivo para download (em MB): "))
internet_speed_mbps = float(input("Digite a velocidade do link de Internet (em Mbps): "))

# Convertendo a velocidade para Megabytes por segundo
internet_speed_mbps /= 8

# Calculando o tempo de download em segundos
download_tempo_seconds = mb / internet_speed_mbps

# Convertendo segundos para minutos
download_tempo_minutes = download_tempo_seconds / 60

print(f"O tempo aproximado de download é de {download_tempo_minutes:.2f} minutos.")
