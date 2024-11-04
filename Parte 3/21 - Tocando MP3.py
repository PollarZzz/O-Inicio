# Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
 
import time
import pygame

# Inicializa o mixer
pygame.mixer.init()

# Carrega o arquivo de áudio (ajuste o caminho se necessário)
caminho_do_arquivo = "C:\\Users\\PollarZzz\\Documents\\Programas\\Projetos\\Python Módulo 1\\SomEx21.mp3"
pygame.mixer.music.load(caminho_do_arquivo)

# Reproduz o áudio
pygame.mixer.music.play()

# Manter o programa rodando até o som terminar
while pygame.mixer.music.get_busy(): # O loop while garante que o programa continue rodando até que o áudio termine de ser reproduzido.
    pygame.time.Clock().tick(10)