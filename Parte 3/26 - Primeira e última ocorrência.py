# Faça um programa que leia uma frase e mostre
# 1 > Quantas vezes aparece a letra "A"
# 2 > Em que posição ela aparece a primeira vez
# 3 > Em que posição ela aparece a ultima vez
# 4 > Adicionar um strip para não contabilizar espaços antes nem depois da frase

import time

print(f'\033[1;32mINICIANDO SISTEMA CONTABILIZADOR DE LETRAS (A)...\033[m')
time.sleep(1)
frase = input('Digite a frase de seu interesse:\n').strip()

# Converte a frase toda para minúsculas para facilitar a contagem
# frase_minuscula = frase.lower()

# Conta as ocorrências da letra 'a'
contagem = frase.count('a' or 'A')

# Encontra a primeira e a última ocorrência da letra 'a'
primeira_letra = frase.find('a' or 'A') + 1
ultima_letra = frase.rfind('a' or 'A') + 1

# A função find() retorna o índice da primeira ocorrência da letra 'a'
# Se a letra não for encontrada, a função retorna -1.
# Por isso, adicionamos 1 para que a resposta seja a posição da letra, e não o índice.
# A função find() é case-sensitive, ou seja, ela diferencia maiúsculas e minúsculas.
# Por isso, usamos a expressão 'a' or 'A' para que a função
# ignore a diferença entre maiúsculas e minúsculas.

print(f'Na sua frase há:\n {contagem} letras A \n Primeira posição: {primeira_letra} \n Ultima posição: {ultima_letra}.')
input("\n Pressione ENTER para sair")