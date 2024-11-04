# Crie um programa que me diga se o número em que o usuário digitou é par ou impar
# Modo simplificado, script não trabalhado!

import time

num = int(input('Digite um número: '))
time.sleep(1)
if num % 2 == 0:
    print('O número é par')
else:
    print('O número é impar')
input("\n Pressione ENTER para encerrar o programa")