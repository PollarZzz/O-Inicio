# Crie um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. 
# Para salários superiores a R$1250,00, calcule um aumento de 10%. 
# Para os inferiores ou iguais, o aumento é de 15%.

import time

print('=-='*10)
print('Calculo de aumento de salario')
print('=-='*10)
time.sleep(1)
print('=-='*10)
salario = float(input('Qual é o seu salario? R$ '))
print('=-='*10)
time.sleep(1)

if salario >= 1251:
    novo = salario + (salario * 10 / 100)
    print(f'Seu salario aumentou de R${salario:.2f} para R${novo:.2f}')
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
    print(f'Seu salario aumentou de R${salario:.2f} para R${novo:.2f}')
input("\n Pressione ENTER para encerrar o programa")
    