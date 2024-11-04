# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print(f"Conversor de centímetros e milímetros!")
medida = float(input('Escreva a distancia (Metros) que deseja consultar: '))
centimetros = medida * 100
milimetros = medida * 1000
print(f"A média de {medida}m correesponde a {centimetros}cm e {milimetros}mm.")
input("\n Pressione ENTER para sair")