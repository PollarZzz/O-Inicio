# Condições if e else:
# Crie um programa que leia o nome do úsuario e se caso estiver um nome biblico em comum    
# Retorne um bom dia e elogie o nome do úsuario!

import time

print(f'\033[1;32mINICIANDO PROGRAMA DE VERIFICAÇÃO BIBLICA...\033[m')
time.sleep(1)
nomes_masc = ["Abraão", "Isaac", "Jacó", "José", "Moisés", "Davi", "Salomão", "Paulo", "Pedro", "Samuel", "Daniel", "Elias", "Ezequiel", "Natanael", "Tiago", "João"]
nomes_femin = ["Maria", "Sara", "Eva", "Raquel", "Rebeca", "Ana", "Miriam", "Ruth", "Débora", "Ester", "Tamar", "Abigail"]
nome = str(input('Qual seu nome? \n'))
if nome == nomes_masc or nomes_femin:
    time.sleep(1)
    print(f"Olá, {nome}👋 Você tem um nome que foi mencionado biblicamente")
else:
    time.sleep(3)
    print(f"Olá, {nome}👋")
input("\n Pressione ENTER para sair")

print(f"Iniciando programa de verificação de média!")
time.sleep(3)
valor1 = float(input('Insira sua nota do primeiro semestre: \n'))
time.sleep(1)
valor2 = float(input('Insira sua nota do segundo semestre: \n'))
resultado = (valor1 + valor2) / 2
time.sleep(1)
if resultado <= 5:
    print(f"Sua média é {resultado:.2f} e você repetiu!")
else:
    print(f"Sua média é {resultado:.2f} e você está aprovado! Parabéns ✔")
input("\n Pressione ENTER para sair")

