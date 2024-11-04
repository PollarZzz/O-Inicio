# Exercício Simples de Olá com o seu nome + Aprimorado após aprender sobre bibliotecas!!
# Ex 1

import emoji

nome = str(input("Olá! Qual seu nome?\n"))

# Boas-vindas personalizadas com emoji
print(f"\nPrazer em conhecê-lo {nome}{emoji.emojize('😉')} seja bem vindo ao Python!!")
input("\n Pressione ENTER para sair")