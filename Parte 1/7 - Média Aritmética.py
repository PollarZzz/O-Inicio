# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

import time

print(f"Olá caro professor está na hora de calcular a média de seu aluno!")
time.sleep(1)
nome = input("Qual o nome do aluno:\n").strip()
time.sleep(1)
semestre_1 = float(input("Entre com a nota do primeiro semestre: "))
time.sleep(1)
semestre_2 = float(input("Entre com a nota do segundo semestre: "))
time.sleep(1)
nota_final = (semestre_1 + semestre_2) / 2

print(f'A nota final do aluno {nome} é de {nota_final}!!')
input("\n Pressione ENTER para sair")