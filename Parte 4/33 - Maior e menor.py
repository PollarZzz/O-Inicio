# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

import time

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))
time.sleep(1)
print('=-='*10)
    # Verifica que é o maior
if n1 > n2 and n1 > n3:
    print(f'Verificando Qual o Maior Número...')
    time.sleep(1.5)
    print(f'O maior número é {n1}')
if n2 > n1 and n2 > n3:
    print(f'Verificando Qual o Maior Número...')
    print(f'O maior número é {n2}')
if n3 > n1 and n3 > n2:
    print(f'Verificando Qual o Maior Número...')
    time.sleep(1.5)
    print(f'O maior número é {n3}')
else:
    print(f'Verificando Qual o Maior Número...')
    time.sleep(1.5)
    print(f'Não há maior número')
input("\n Pressione ENTER para encerrar o programa")
