# Exercício Simples de Olá com o seu nome + Aprimorado após aprender sobre bibliotecas!!
# Ex 1

import emoji

nome = str(input("Olá! Qual seu nome? "))
resposta = nome

# Boas-vindas personalizadas com emoji
print(f"Prazer em conhecê-lo {resposta}{emoji.emojize('😉')} seja bem vindo ao Python!!")

input("\n Pressione ENTER para sair")
