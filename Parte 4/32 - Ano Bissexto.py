# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
# Extra: Que seja capaz de analisar o ano atual caso usuário queira ver.

import datetime
import time

ano = int(input('Digite o ano que deseja analisar ou coloque 0 para o ano atual: \n'))
if ano == 0:
    ano = datetime.datetime.now().year
if ano % 4 == 0 and ano != 100 or ano % 400 == 0:
# Se o ano for divisivel por 4 der 0 ele executa o if | (Representação: != Igual ou Diferente)
# Ele tem que ser divisivel por 4 e não pode ser diferente de 0 (100) ou 400 
    print('Verificando calendário...')
    time.sleep(1.5)
    print('Verificação concluida com sucesso! ✔')
    time.sleep(1)
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano} não é bissexto')
input("\n Pressione ENTER para encerrar o programa")