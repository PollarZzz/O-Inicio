# Ex 3
# Parte 01/02

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

print("Vamos descobrir umas curiosidades sobre o que for digitar!")
algo = input('Digite algo: ')

print(f'O {algo} é um dígito?',algo.isdigit())
print(f'O {algo} só contem letra minúscula? ',algo.islower())
print(f'O {algo} só contem letra maiúscula? ',algo.isupper())
print(f'O {algo} é um espaço em branco? ',algo.isspace()) # Está dando erro porque input() retorna uma string, mesmo que o usuário apenas pressione Enter. Portanto receberá uma string vazia.
# print(f'O {algo} é um espaço em branco? ',len(algo) == 0) # A função len() para verificar se a string tem comprimento zero. Se a string tiver comprimento zero, a função len() retornará 0.
print(f'O {algo} se inicia com uma letra maiúscula? ',algo.istitle())
print(f'O {algo} é um alfanumérico? ',algo.isalnum())
print(f'O {algo} contem somente letra do alfabeto? ',algo.isalpha())
print(f'O {algo} está no padrão ASCII? ',algo.isascii())
print(f'O {algo} são números decimais? ',algo.isdecimal())
print(f'O {algo} pode ser exibido visualmente na maioria dos terminais e consoles? ',algo.isprintable())

input("\n Pressione ENTER para sair")