 # Desenvolva um programa que pergunte a distância de uma viagem em Km. 
 # Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
 # E R$0,45 parta viagens mais longas.
 
import time

print('Calculo de viagem por Km rodado')
time.sleep(1)
distancia = float(input('Quantos Km até seu destino final? \n'))
time.sleep(1)
if  distancia <= 200:
    print('Calculando o valor da passagem...')
    time.sleep(2)
    preco = distancia * 0.50
    print(f'O valor da passagem é de R${preco:.2f}.')
    print('Tenha uma boa viagem 👋')
else:
    preco = distancia * 0.45
    print('Calculando o valor da passagem...')
    time.sleep(2)
    print(f'O valor da passagem é de R${preco:.2f}')
    print('Tenha uma boa viagem 👋')
input("\n Pressione ENTER para encerrar o programa")