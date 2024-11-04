#  Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
#  O programa deve perguntar ao usuário se ele deseja converter de Celsius para Fahrenheit ou vise-versa.

import time

print(f'\033[1;32mINICIANDO SISTEMA DE CONVERSÃO DE TEMPERATURA...\033[m')
time.sleep(1)
print(f'\033[1;31mSISTEMA INICIADO\033[m')

celcius = float(input("Digite a temperatura em CELSIUS: "))
fahrenheit = celcius * 9 / 5 + 32
time.sleep(1)
print(f'A conversão de {celcius:.2f}ºC é de {fahrenheit:.2f}F.')
input("\n Pressione ENTER para sair")