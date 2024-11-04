# Crie um programa que solicita e verifica se o usuario tem "Silva" em alguma parte do nome
# Modo simplificado, script não trabalhado!

nome_completo = str(input("Qual o seu nome completo?\n")).strip()

if nome_completo.find('Silva'):
    print("Você tem Silva no nome portanto pertence a família Silva!")
else:
    print("Você não é da família Silva!")
    
    input("\n Pressione ENTER para sair")