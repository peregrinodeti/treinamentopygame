import pygame

pygame.init()
# Constantes para a tela
LARGURA_TELA = 640
ALTURA_TELA = 480
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
# Título da janela
pygame.display.set_caption("Piano Virtual")

clock = pygame.time.Clock()
running = True

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
    fonte = pygame.font.SysFont("Arial", 40, bold=True, italic=True)
    texto = fonte.render("TEXTO PIANO", True, "white")
    tela.blit(texto, [(180), (60)])

    # Atualiza a tela com tudo o que foi desenhado acima
    pygame.display.flip()

    # Controla a taxa de quadros (FPS)
    clock.tick(60)

pygame.quit()
