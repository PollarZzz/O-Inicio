# Desafio de um programa que leia o nome de uma cidade e diga se ela começa ou não com nome 'Santos'
# Modo simplificado, script não trabalhado!

cidade = str(input('Qual o nome da sua cidade? \nR:')).strip()

if cidade.startswith("Santo"):
    print("Sua cidade começa com Santo")
else:
    print("Sua cidade não começa com Santo")

input("\n Pressione ENTER para sair")