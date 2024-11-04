
 # Aula de manipulação de texto
 # Desafio do dia: Crie um programa que leia o nome completo de uma pessoa e mostre
 # Todas as letras maiusculas, minusculas, quantas letras tem ao todo (sem os espaços)
 # E quantas letras tem apenas o primeiro nome
 
 # Frase.count(''), usamos para contar determinados caracteres.
 # Frase.endswith(''), Verifica se uma string termina com uma determinada sequência.
 # Frase.find(''), usamos para encontrar a posição de determinados caracteres.  
 # Frase.replace('',''), usamos para substituir determinados caracteres.
 # Frase.len(''), usamos para contar quantos caracteres há em uma frase.
 # Frase.split(''), usamos para dividir uma frase em uma lista de palavras.
 # Frase.strip(''), usamos para remover espaços em branco no início e no final da frase.
 # Frase.upper(''), usamos para definir todos os caracteres minusculo.
 # Frase.lower(''), usamos para definir todos os caracteres maiusculo.
 # Frase.capitalize(''), usamos para deixar a primeira letra das frases em maiusculo.
 # Frase.title.(''), caracteres inicias ficam em maiusculo.
 # Frase.isalpha(''), usamos para verificar se a frase é composta apenas por letras
 # Frase.isalnum(''), usamos para verificar se a frase é composta apenas por letras
 # Frase.isdecimal(''), usamos para verificar se a frase é composta apenas por números
 # Frase.isdigit(''), usamos para verificar se a frase é composta apenas por números
 # Frase.isnumeric(''), usamos para verificar se a frase é composta apenas por números

import time

# Solicita o nome completo do usuário
nome_completo = input("Olá 👋 Qual é o seu nome completo? \nR: ").strip()
# Conta o número total de caracteres (incluindo espaços)
numero_caracteres = len(nome_completo)
# Remove espaços em branco do nome completo
nome_sem_espaco = nome_completo.replace(" ", "") # Gabriel Henrique 
# Conta o número de caracteres sem espaços
numero_caracteres_sem_espaco = len(nome_sem_espaco) 
# Verifica o primeiro nome do usuario
primeiro_nome = nome_completo.split(" ")[0]
# Verifica quantos caracteres tem o primeiro nome do usuario
numero_caracteres_primeiro_nome = len(primeiro_nome)

# Apresentação e mensagens personalizadas
print(f"\nOlá {nome_completo}, seja bem-vindo(a)!")
time.sleep(2)
print(f"Sabia que existem diversas maneiras de escrever seu nome? 🤔\n")
time.sleep(2)


# Exibe o nome em maiúsculas
print(f"Uma delas é em maiúsculas: {nome_completo.upper()}")
time.sleep(1)
print(f"E tmb em maiúsculas: {nome_completo.lower()}")
time.sleep(1)
print("Que legal, né? \n")
time.sleep(2)

# Mostra a quantidade de caracteres com e sem espaços
print(f"Seu nome completo possui {numero_caracteres} caracteres (incluindo espaços).")
time.sleep(2)
print(f"Sem os espaços, seu nome fica com {numero_caracteres_sem_espaco} caracteres! \n")
time.sleep(2)

print(f'E para finalizar, somente seu primeiro nome {primeiro_nome} tem {numero_caracteres_primeiro_nome} caracteres😉 \n')
# Despedida
print(f"Obrigado por participar, {primeiro_nome}!🤗")

input("\n Pressione ENTER para sair")