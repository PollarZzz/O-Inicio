# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random # Função para sortear os alunos
import time # Função para dar tempos entre os comandos


print(f'\033[1;32mINICIANDO SISTEMA SORTEIO...\033[m')
time.sleep(1)
print(f'\033[1;31mSISTEMA INICIADO\033[m')

alunos1 = str(input('Digite o nome do primeiro aluno: '))
alunos2 = str(input('Digite o nome do segundo aluno: '))
alunos3 = str(input('Digite o nome do terceiro aluno: '))

alunos = [alunos1, alunos2, alunos3]
random.shuffle(alunos) # Shuffle faz com que escolha em ordem aleatoria na lista.
print(f'A ordem escolhida foi {alunos}')
