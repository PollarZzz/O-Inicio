# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import time
import random

print(f'\033[1;32mINICIANDO SISTEMA SORTEIO...\033[m')
time.sleep(1)
print(f'\033[1;31mSISTEMA INICIADO\033[m')

alunos1 = str(input('Digite o nome do primeiro aluno: '))
alunos2 = str(input('Digite o nome do segundo aluno: '))
alunos3 = str(input('Digite o nome do terceiro aluno: '))

alunos = [alunos1, alunos2, alunos3]
embaralhemento = random.choice(alunos)
print(f'O aluno escolhido foi {embaralhemento}!')
input("\n Pressione ENTER para sair")