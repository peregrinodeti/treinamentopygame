import pygame

pygame.init()
# Constantes para a tela
LARGURA_TELA = 640
ALTURA_TELA = 480
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
# Título da janela
pygame.display.set_caption("Piano Virtual")

# Constantes para as teclas do piano
INICIO_E_TECLAS = 240
ALTURA_TECLA = 280

clock = pygame.time.Clock()
running = True

teclas_info = [
    {"cor": "red", "nota": "DÓ"},
    {"cor": "orange", "nota": "RÉ"},
    {"cor": "yellow", "nota": "MI"},
    {"cor": "green", "nota": "FÁ"},
    {"cor": "pink", "nota": "SOL"},
    {"cor": "purple", "nota": "LÁ"},
    {"cor": "blue", "nota": "SI"},
]

fonte = pygame.font.SysFont("Arial", 40, bold=True, italic=True)

# Inicia o loop principal do jogo
while running:
    pos = pygame.mouse.get_pos()

    # Fundo e detalhes superiores
    pygame.draw.rect(tela, "black", [0, 0, LARGURA_TELA, 240])
    pygame.draw.line(
        tela,
        "white",
        (0, ALTURA_TELA / 2),
        (LARGURA_TELA, ALTURA_TELA / 2),
        50,
    )
    pygame.draw.ellipse(tela, "yellow", (80, 35, 440, 100), 5)

    # Texto do título
    texto_titulo = fonte.render("TEXTO PIANO", True, "white")
    tela.blit(texto_titulo, (180, 60))

    total_teclas = len(teclas_info)

    for i, info in enumerate(teclas_info):
        # Calcula onde a tecla atual começa e onde a próxima deve começar
        inicio_x = int(i * LARGURA_TELA / total_teclas)
        proximo_x = int((i + 1) * LARGURA_TELA / total_teclas)
        largura_tecla_dinamica = proximo_x - inicio_x

        # Desenha o retângulo da tecla com a largura corrigida
        pygame.draw.rect(
            tela,
            info["cor"],
            [inicio_x, INICIO_E_TECLAS, largura_tecla_dinamica, ALTURA_TECLA],
        )

        # Renderiza o texto da nota correspondente
        texto_nota = fonte.render(info["nota"], True, "white")

        # Centraliza o texto automaticamente no meio de cada tecla
        largura_texto = texto_nota.get_width()
        texto_x = inicio_x + (largura_tecla_dinamica - largura_texto) // 2

        tela.blit(texto_nota, (texto_x, 400))

    # Círculos do mouse
    pygame.draw.circle(tela, "white", pos, 5)
    pygame.draw.circle(tela, "black", pos, 3)

    # Observa os eventos de teclado e mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Atualiza a tela com tudo o que foi desenhado acima
    pygame.display.flip()

    # Controla a taxa de quadros (FPS)
    clock.tick(60)

pygame.quit()
