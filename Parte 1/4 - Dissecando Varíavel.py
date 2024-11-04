# Ex 3
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo
# Primitivo e todas as informações possíveis sobre ele.

# A função isdigit() verifica se um caractere é um dígito.
# A função islower() verifica se um caractere é uma letra minúscula.
# A função isupper() verifica se um caractere é uma letra maiúscula.
# A função isspace() verifica se um caractere é um espaço em branco.
# A função istitle() verifica se um caractere é uma letra maiúscula inicial.
# A função isnum() verifica se o caractere escrito é alfanumérico (Podendo ter letra e número).
# A função isalpha() verifica se um caractere escrito é uma letra do alfabeto (Pode ser maiúscula ou minúscula). 
# A função isascii() verifica se todos os caracteres em uma string estão representados na tabela ASCII (Padrão Americano para Intercâmbio de Informações).
# A função isdecimal() verifica se todos os caracteres em uma string são dígitos decimais.
# A função isprintable() verifica se todos os caracteres em uma string são considerados "imprimíveis".

import time

print("Vamos descobrir umas curiosidades sobre o que for digitar!")
time.sleep(1)
algo = input('Digite algo: ')

print(f'O {algo} é um dígito?',algo.isdigit())
time.sleep(1)
print(f'O {algo} só contem letra minúscula? ',algo.islower())
time.sleep(1)
print(f'O {algo} só contem letra maiúscula? ',algo.isupper())
time.sleep(1)
print(f'O {algo} é um espaço em branco? ',algo.isspace()) # Está dando erro porque input() retorna uma string, mesmo que o usuário apenas pressione Enter. Portanto receberá uma string vazia.
time.sleep(1)
# print(f'O {algo} é um espaço em branco? ',len(algo) == 0) # A função len() para verificar se a string tem comprimento zero. Se a string tiver comprimento zero, a função len() retornará 0.
print(f'O {algo} se inicia com uma letra maiúscula? ',algo.istitle())
time.sleep(1)
print(f'O {algo} é um alfanumérico? ',algo.isalnum())
time.sleep(1)
print(f'O {algo} contem somente letra do alfabeto? ',algo.isalpha())
time.sleep(1)
print(f'O {algo} está no padrão ASCII? ',algo.isascii())
time.sleep(1)
print(f'O {algo} são números decimais? ',algo.isdecimal())
time.sleep(1)
print(f'O {algo} pode ser exibido visualmente na maioria dos terminais e consoles? ',algo.isprintable())
time.sleep(0.5)

input("\n Pressione ENTER para sair")

print(f"Inicindo Segunda Parte do Exercicio!")
time.sleep(1.5)
print("Vamos descobrir umas curiosidades sobre o que for digitar!")
time.sleep(1)
print("Isso é apenas outra maneira de fazer a mesma brincadeira\n Só que com outro esquema de código")
algo = input('Digite algo: ')
time.sleep(1)
tipos = ["dígito", "letra minúscula", "letra maiúscula", "espaço em branco",
          "letra maiúscula inicial", "alfanumérico", "letra do alfabeto",
          "padrão ASCII", "número decimal", "pode ser exibido"]

for tipo in tipos:
    if tipo == "dígito":
        condicao = algo.isdigit()
    elif tipo == "letra minúscula":
        condicao = algo.islower()
    elif tipo == "letra maiúscula":
        condicao = algo.isupper()
    elif tipo == "espaço em branco":
        condicao = algo.isspace()
    elif tipo == "letra maiúscula inicial":
        condicao = algo.istitle()
    elif tipo == "alfanumérico":
        condicao = algo.isalnum()
    elif tipo == "letra do alfabeto":
        condicao = algo.isalpha()
    elif tipo == "padrão ASCII":
        condicao = algo.isascii()
    elif tipo == "número decimal":
        condicao = algo.isdecimal()
    else:
        condicao = algo.isprintable()

    if condicao:
        time.sleep(1)
        print(f"O valor é {tipo}.")
    else:
        time.sleep(1)
        print(f"O valor não é {tipo}.")

input("\n Pressione ENTER para sair")

