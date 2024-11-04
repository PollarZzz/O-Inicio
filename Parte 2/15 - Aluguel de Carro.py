# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

import time

print(f'\033[1;32mINICIANDO SISTEMA DE ALUGUEL DE VEICULO...\033[m')
time.sleep(1)
km = float(input('Quantos Kilometros você rodou: '))
time.sleep(1)
dias = float(input('Quantos Dias você alugou: '))
valor_veiculo_dia = 60
valor_veiculo_km = 0.15
preco_total = (dias * valor_veiculo_dia) + (km * valor_veiculo_km)
print(f'\033[1;31mCALCULANDO GASTOS...\033[m')
time.sleep(1)
print(f'O valor a ser pago é de: R${preco_total:.2f}')
input("\n Pressione ENTER para sair")