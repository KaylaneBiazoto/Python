import pygame
# Instalado pelo terminal usando python3 -m pip install pygame

# Inicializando o mixer PyGame
pygame.mixer.init()

# Iniciando o PyGame
pygame.init()
pygame.mixer.music.load('RexIncognito.mp3')
pygame.mixer.music.play(loops = 0, start = 0.0)

# Espera a musica parar para parar o programa
pygame.event.wait()

