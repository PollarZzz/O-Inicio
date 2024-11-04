# Ex 05
# Calcule a raiz quadrada de um número
# Parte 1/3

print('Vamos calcular algumas raizes quadradas!!\n ')

operacao = int(input('Raiz quadrada de: '))
total = operacao ** (1/2)
print(f'O resultado da Raiz Quadrada de {operacao} é {total}')


# Ex 05
# Calcule a raiz cúbica de um número
# Parte 2/3


print('Vamos calcular algumas raizes cúbicas!!\n ')

operacao = int(input('Qual a Raiz Cúbica de: '))
total = operacao ** (1/3)

print(f'A raiz cúbica de {operacao} é {total}')

input("\n Pressione ENTER para sair")


# Ex 05
# Calculando resultado de operações básicas (soma, subtração, multiplicação, divisão)
# Parte 3/3


print("Vamos calcular o resultado da soma, da subtração e da da mutiplicação.\n ")
n1 = int(input('Digite o primeiro valor númerico: '))
n2 = int(input('Digite o segundo valor númerico: '))

soma = n1 + n2
subtracao = n1 - n2
multiplicacao = n1 * n2
divisao = n1 / n2
divisao_inteira = n1 // n2
resto_da_divisao = n1 % n2

print(f'O resultado da soma é: {soma}.\nO resultado da subtração é: {subtracao}.\nO resultado da mutiplicação é {multiplicacao}!!')

input("\n Pressione ENTER para sair")
