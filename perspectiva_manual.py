import cv2
import numpy as np

# Imagem original e a tela final que será projetada a transformação
imagem = cv2.imread("imagens/perspectiva_original.jpeg")
LARGURA, ALTURA = 480, 270

pontos_1 = np.float32([[110, 78], [352, 70], [44, 222], [420, 208]])
pontos_2 = np.float32([[0, 0], [LARGURA, 0], [0, ALTURA], [LARGURA, ALTURA]])
# Transformação de perspectiva
matrix = cv2.getPerspectiveTransform(pontos_1, pontos_2)
imagem_corrigida = cv2.warpPerspective(imagem, matrix, (LARGURA, ALTURA))

# Lista de cores para cada círculo (BGR) OpenCV usa BGR, não RGB
cores = [(0, 255, 255), (255, 0, 0), (0, 0, 255), (0, 255, 0)]


# Loop para desenhar os círculos e os números
for i, ponto in enumerate(pontos_1):
    centro_x = int(ponto[0])
    centro_y = int(ponto[1])

    # Desenha o círculo nos vértices
    cv2.circle(imagem, (centro_x, centro_y), 8, cores[i], cv2.FILLED)

    # Configurações do texto/número
    texto = str(i + 1)  # Número que será exibido (1, 2, 3, 4)
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    escala = 0.4
    cor_texto = (0, 0, 0)  # Preto para dar contraste
    espessura = 1

    # Descobre o tamanho do texto para centralizar
    (t_largura, t_altura), _ = cv2.getTextSize(texto, fonte, escala, espessura)

    # Calcula a posição para o texto ficar no centro do círculo
    texto_x = centro_x - t_largura // 2
    texto_y = centro_y + t_altura // 2

    # Desenha o número
    cv2.putText(
        imagem,
        texto,
        (texto_x, texto_y),
        fonte,
        escala,
        cor_texto,
        espessura,
        cv2.LINE_AA,
    )

cv2.imshow("Imagem Original", imagem)
cv2.imshow("Imagem Corrigida", imagem_corrigida)
cv2.waitKey(0)
cv2.destroyAllWindows()
