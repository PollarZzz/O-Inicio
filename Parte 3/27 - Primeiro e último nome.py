# Faça um programa que leia o nome completo do usuario e retorne o primeiro e ultimo nome
# Ex > Gabriel Henrique de Jesus
# Primeiro nome: Gabriel
# Ultimo nome: Jesus

# Modo simplificado, script não trabalhado!
nome = input("Digite seu nome completo?\n").strip().split()

primeiro_nome = nome [0] # Acessa o primeiro elemento da lista nome (Em Python, os índices começam em 0).
ultimo_nome = nome [-1] # Acessa o último elemento da lista nome. O índice -1 indica o último elemento.

print(f"Seu nome completo: {nome}\n Primeiro nome: {primeiro_nome}\n Ultimo nome: {ultimo_nome}")


input("\n Pressione ENTER para sair")