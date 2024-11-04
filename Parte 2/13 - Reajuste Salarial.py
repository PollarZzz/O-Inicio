# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

import time

print(f'SISTEMA DE REAJUSTE SALARIA!')
time.sleep(1)
salario = float(input('Digite o salário do funcionário: R$'))
salario += salario * 0.15
time.sleep(1)
print(f'O novo salário do funcionário é R$ {salario:.2f}.')
input("\n Pressione ENTER para sair")