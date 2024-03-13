# Ex 3
# Parte 02/02

print("Vamos descobrir umas curiosidades sobre o que for digitar!")
print("Isso é apenas outra maneira de fazer a mesma brincadeira\n Só que com outro esquema de código")
algo = input('Digite algo: ')

tipos = ["dígito", "letra minúscula", "letra maiúscula", "espaço em branco",
          "letra maiúscula inicial", "alfanumérico", "letra do alfabeto",
          "padrão ASCII", "número decimal", "pode ser exibido"]

for tipo in tipos:
    if tipo == "dígito":
        condicao = algo.isdigit()
    elif tipo == "letra minúscula":
        condicao = algo.islower()
    elif tipo == "letra maiúscula":
        condicao = algo.isupper()
    elif tipo == "espaço em branco":
        condicao = algo.isspace()
    elif tipo == "letra maiúscula inicial":
        condicao = algo.istitle()
    elif tipo == "alfanumérico":
        condicao = algo.isalnum()
    elif tipo == "letra do alfabeto":
        condicao = algo.isalpha()
    elif tipo == "padrão ASCII":
        condicao = algo.isascii()
    elif tipo == "número decimal":
        condicao = algo.isdecimal()
    else:
        condicao = algo.isprintable()

    if condicao:
        print(f"O valor é {tipo}.")
    else:
        print(f"O valor não é {tipo}.")

input("\n Pressione ENTER para sair")