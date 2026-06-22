import cv2
import numpy as np

import pygame

# Inicialização do Pygame e do módulo de fontes
pygame.init()
pygame.font.init()

# Constantes para a tela
LARGURA, ALTURA = 480, 270
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Seleção de Pontos para Perspectiva")

# Configuração da Fonte
fonte = pygame.font.SysFont("Arial", 14, bold=True)

# Carregamento de recursos
CAMINHO_IMAGEM = "imagens/perspectiva_original.jpeg"
imagem_original = cv2.imread(CAMINHO_IMAGEM)
imagem_pygame = pygame.image.load(CAMINHO_IMAGEM)

# Estado da aplicação
vertices = np.zeros((4, 2), dtype=np.float32)
contador = 0
transformacao_realizada = False

# Lista de cores para cada círculo (RGB)
cores = [
    (255, 255, 0),  # 1º Ponto: Amarelo
    (0, 0, 255),  # 2º Ponto: Azul
    (255, 0, 0),  # 3º Ponto: Vermelho
    (0, 255, 0),  # 4º Ponto: Verde
]

clock = pygame.time.Clock()
running = True


def aplicar_perspectiva(pontos_origem: np.ndarray) -> None:
    """Calcula e exibe a transformação de perspectiva."""
    # Mapeamento do destino baseado na ordem esperada dos cliques
    pontos_destino = np.float32(
        [
            [0, 0],  # Superior Esquerdo
            [LARGURA, 0],  # Superior Direito
            [0, ALTURA],  # Inferior Esquerdo
            [LARGURA, ALTURA],  # Inferior Direito
        ]
    )

    # Gera a matriz de transformação
    matrix = cv2.getPerspectiveTransform(pontos_origem, pontos_destino)

    # Aplica o warp na imagem original do OpenCV
    imagem_corrigida = cv2.warpPerspective(
        imagem_original, matrix, (LARGURA, ALTURA)
    )

    # Abre a janela nativa do OpenCV com o resultado
    cv2.imshow("Imagem Corrigida", imagem_corrigida)


# Laço Principal
while running:

    # Observa os eventos de teclado e mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and contador < 4:
            # Captura a posição exata do clique
            vertices[contador] = event.pos
            contador += 1

    # Limpa a tela com uma cor de fundo antes de desenhar
    tela.fill("black")
    tela.blit(imagem_pygame, (0, 0))

    # Desenha os círculos e os números centralizados dentro deles
    for i in range(contador):
        x = int(vertices[i][0])
        y = int(vertices[i][1])

        # Desenha o círculo (raio 8 para dar espaço ao número)
        pygame.draw.circle(tela, cores[i], (x, y), 8)

        # Renderiza o número em texto preto para dar contraste com as cores de fundo
        texto_superficie = fonte.render(str(i + 1), True, (0, 0, 0))

        # Alinha o centro do retângulo do texto com o centro do clique
        texto_retangulo = texto_superficie.get_rect(center=(x, y))

        # Desenha o texto na tela
        tela.blit(texto_superficie, texto_retangulo)

    # Processa a perspectiva uma única vez após capturar os 4 pontos
    if contador == 4 and not transformacao_realizada:
        aplicar_perspectiva(vertices)
        transformacao_realizada = True

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
cv2.destroyAllWindows()
