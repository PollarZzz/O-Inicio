# Faça um programa que leia a largura e a altura de uma parede em metros 
# Calcule a sua área e a quantidade de tinta necessária para pintá-la
# Sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input("Quantos metros de largura tem o local:\n"))
alt = float(input("Quantos metros de altura tem o local:\n"))
area = larg * alt
tinta = area / 2
print(f'Sua parede tem {larg:.2f}x{alt:.2f} em uma área de {area:.2f}m².')
print(f'Estima-se que precisara de {tinta:.2f}L de tinta para pintar suas paredes!')
input("\n Pressione ENTER para sair")