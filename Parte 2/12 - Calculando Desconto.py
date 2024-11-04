# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

produto = float(input('Qual o valor do produto?\nR$'))
deconto = produto - (produto * 5 / 100)

print(f'O preço do produto é de {produto:.2f}\n Descontando 5% fica {deconto:.2f}.')
input("\n Pressione ENTER para sair")