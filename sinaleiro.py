import time

import pygame

pygame.init()
# Constantes para a tela
LARGURA_TELA = 640
ALTURA_TELA = 480
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
# Título da janela
pygame.display.set_caption("Sinaleiro")

clock = pygame.time.Clock()
running = True

verde = pygame.image.load("imagens/verde.png")
amarelo = pygame.image.load("imagens/amarelo.png")
vermelho = pygame.image.load("imagens/vermelho.png")


# Inicia o loop principal do jogo
while running:
    # Nesse ponto dento desse laço é colocado o jogo para rodar,
    # ou seja, o que deve acontecer a cada frame

    # Observa os eventos de teclado e mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Limpa a tela com uma cor de fundo antes de desenhar
    tela.fill("black")

    tela.blit(verde, (0, 0))
    pygame.display.update()
    time.sleep(1)

    tela.blit(amarelo, (0, 0))
    pygame.display.update()
    time.sleep(1)

    tela.blit(vermelho, (0, 0))
    pygame.display.update()
    time.sleep(1)

    # Atualiza a tela com tudo o que foi desenhado acima
    pygame.display.flip()

    # Controla a taxa de quadros (FPS)
    clock.tick(60)

pygame.quit()
