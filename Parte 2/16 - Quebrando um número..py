# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import math

numeber = float(input('Digite um valor: '))
print(f'A porção inteira desse valor é: ', math.trunc(numeber))
input("\n Pressione ENTER para sair")
