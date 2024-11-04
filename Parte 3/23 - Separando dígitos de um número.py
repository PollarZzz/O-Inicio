# Crie um programa que mostre na tela os determinados valores
# 1 > Unidade
# 2 > Dezena
# 3 > Centena
# 4 > Milhar
# Modo simplificado, script não trabalhado!
numero = int(input('Digite um valor: '))

unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10

print(f'O resultado em unidade: {unidade} \n O resultado em dezena: {dezena} \n O resultado em centena: {centena} \n O resultado em milhar: {milhar}')

input("\n Pressione ENTER para sair")