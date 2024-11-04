# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

print(f'Conversor de moedas PT (R$) - EUA (U$) - EUR (€)')
valor = float(input("Quanto deseja converter?\nR$"))

euro = valor / 6.15 
dolar = valor / 5.55

print(f'A conversão de R${valor:.2f}\n Dólar: {dolar:.2f}\n Euro: {euro:.2f}')
input("\n Pressione ENTER para sair")