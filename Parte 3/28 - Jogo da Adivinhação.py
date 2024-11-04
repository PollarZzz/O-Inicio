# Condições if e else e biblioteca Random
# Crie um programa que pense em um número inteiro entre 1 e 5
# E peça para que o usuário tente descobrir qual o número o programa está pensando
# Caso o usuário ganhe de a ele os parabens senão avise-o que perdeu.

import time
import random

# Geração de um número aleatório entre 1 e 5
print(f"\033[1;32mINICIANDO O ADIVINHA...\033[m")
time.sleep(1)
print(f"Olá👋 jogador!! Bem vindo ao programa. A regra do jogo são simples e citarei ela para você: ") # Start do jogo
print(f"1. Meu sistema está pensando em um número inteiro entre 1 e 5, basta você adivinha e boom💥 ganhou!!")
print(f"2. Se você errar, o sistema irá te dizer que você perdeu!!")
print(f"Fique atento!! O jogo está começando!!")
time.sleep(2.5)
resposta = int(input("Em qual número estou pensando?\n"))
numero = random.randint(1, 5)
print(f"Aguarde... Estou pensando em um número 🤔")
time.sleep(2)
if resposta == numero:
    print(f"Parabéns jogador!! Você acertou!! O número que eu estava pensando era {numero}!!")
else:
    print(f"Você perdeu!! O número que eu estava pensando era {numero}")
    time.sleep(1)
    print(f"Obrigado por participar.")
input("\n Pressione ENTER para encerrar o programa")