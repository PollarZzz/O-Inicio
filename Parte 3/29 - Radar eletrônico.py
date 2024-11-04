# Condições if e else:
# Crie um programa que aplique uma multa ao motorista se caso ele estive acima de 80km/h
# E avise-o que para cada km ultrapasado do limite de velocidade custara 7,00R$

import time

velocidade = float(input("Em que velocidade você passou no radar? \n"))
print("Caso ultrapasse os 80Km/h o senhor(a) será multado em R$7,00 para cada Km acima do limite!!")
time.sleep(1)
if velocidade >= 80:
    print("Calculando velocidade...")
    time.sleep(2)
    print("Você está acima do limite de velocidade")
    time.sleep(1)
    print("Aplicando Multa...")
    time.sleep(1)
    multa = (velocidade -80) * 7
    print(f"Multa aplicada.\n Saldo devedor em seu nome: R${multa:.2f}")
else:
    print("Você está dentro do limite de velocidade, continue assim. Boa viagem!! 👋")
input("\n Pressione ENTER para encerrar o programa")