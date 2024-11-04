# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

import time

print('=-='*10)
print('CREATOR : POLLARZZZ')
print('=-='*10)
time.sleep(1.5)
r1 = float(input('Digite aqui o primeiro segmento: '))
r2 = float(input('Digite aqui o segundo segmento: '))
r3 = float(input('Digite aqui o terceiro segmento: '))
print('=-='*10)
time.sleep(1.5)
if  r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Somando segmentos')
    time.sleep(1)
    print('Os segmentos PODEM formar um triângulo.')
else:
    print(f'Somando segmentos')
    time.sleep(1)
    print('Os segmentos NÃO PODEM formar um triângulo.')
input("\n Pressione ENTER para encerrar o programa")