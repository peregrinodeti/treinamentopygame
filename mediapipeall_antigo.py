import cv2
import mediapipe as mp
import pygame
import pygame.display
from pygame import mixer

pygame.init()

largura_tela = 630
altura_tela = 480
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("MEU PYANO - POR ANDRÉ BONETTO")

som_do = mixer.Sound("sons/do.mp3")
som_re = mixer.Sound("sons/re.mp3")
som_mi = mixer.Sound("sons/mi.mp3")
som_fa = mixer.Sound("sons/fa.mp3")
som_sol = mixer.Sound("sons/sol.mp3")
som_la = mixer.Sound("sons/la.mp3")
som_si = mixer.Sound("sons/si.mp3")

inicio_y_teclas = 240
largura_tecla = 90
altura_tecla = 280

inicio_x_do = 0
inicio_x_re = 90
inicio_x_mi = 180
inicio_x_fa = 270
inicio_x_sol = 360
inicio_x_la = 450
inicio_x_si = 540

fonte = pygame.font.SysFont("Arial", 40, bold=True, italic=True)


mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

cap = cv2.VideoCapture("video_para_testar_mediapipe.mp4")
# cap = cv2.VideoCapture(0)

with mp_pose.Pose(
    min_detection_confidence=0.5, min_tracking_confidence=0.5
) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        mp_drawing.draw_landmarks(
            image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS
        )

        cv2.imshow("MediaPipe", image)
        # cv2.imshow('Original', frame)

        try:
            landmarks = results.pose_landmarks.landmark
            # x_pose = landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].x
            # y_pose = landmarks[mp_pose.PoseLandmark.LEFT_FOOT_INDEX.value].y

            x_pose = landmarks[mp_pose.PoseLandmark.NOSE.value].x
            y_pose = landmarks[mp_pose.PoseLandmark.NOSE.value].y

            pos = ((x_pose * largura_tela), (y_pose * altura_tela))
            print(pos)

            pygame.draw.rect(tela, "black", [0, 0, largura_tela, 240])
            pygame.draw.line(tela, "white", (0, 240), (640, 240), 50)

            pygame.draw.rect(
                tela,
                "red",
                [inicio_x_do, inicio_y_teclas, largura_tecla, altura_tecla],
            )
            pygame.draw.rect(
                tela,
                "orange",
                [inicio_x_re, inicio_y_teclas, largura_tecla, altura_tecla],
            )
            pygame.draw.rect(
                tela,
                "yellow",
                [inicio_x_mi, inicio_y_teclas, largura_tecla, altura_tecla],
            )
            pygame.draw.rect(
                tela,
                "green",
                [inicio_x_fa, inicio_y_teclas, largura_tecla, altura_tecla],
            )
            pygame.draw.rect(
                tela,
                "pink",
                [inicio_x_sol, inicio_y_teclas, largura_tecla, altura_tecla],
            )
            pygame.draw.rect(
                tela,
                "purple",
                [inicio_x_la, inicio_y_teclas, largura_tecla, altura_tecla],
            )
            pygame.draw.rect(
                tela,
                "blue",
                [inicio_x_si, inicio_y_teclas, largura_tecla, altura_tecla],
            )

            pygame.draw.ellipse(tela, "yellow", (80, 35, 440, 100), 5)

            if pos[0] < inicio_x_re and pos[1] > inicio_y_teclas:
                som_do.play()
                pygame.draw.rect(
                    tela,
                    "black",
                    [
                        inicio_x_do,
                        inicio_y_teclas,
                        largura_tecla,
                        altura_tecla,
                    ],
                )

            if (pos[0] > inicio_x_re and pos[0] < inicio_x_mi) and pos[
                1
            ] > inicio_y_teclas:
                som_re.play()
                pygame.draw.rect(
                    tela,
                    "black",
                    [
                        inicio_x_re,
                        inicio_y_teclas,
                        largura_tecla,
                        altura_tecla,
                    ],
                )

            if (pos[0] > inicio_x_mi and pos[0] < inicio_x_fa) and pos[
                1
            ] > inicio_y_teclas:
                som_mi.play()
                pygame.draw.rect(
                    tela,
                    "black",
                    [
                        inicio_x_mi,
                        inicio_y_teclas,
                        largura_tecla,
                        altura_tecla,
                    ],
                )

            if (pos[0] > inicio_x_fa and pos[0] < inicio_x_sol) and pos[
                1
            ] > inicio_y_teclas:
                som_fa.play()
                pygame.draw.rect(
                    tela,
                    "black",
                    [
                        inicio_x_fa,
                        inicio_y_teclas,
                        largura_tecla,
                        altura_tecla,
                    ],
                )

            if (pos[0] > inicio_x_sol and pos[0] < inicio_x_la) and pos[
                1
            ] > inicio_y_teclas:
                som_sol.play()
                pygame.draw.rect(
                    tela,
                    "black",
                    [
                        inicio_x_sol,
                        inicio_y_teclas,
                        largura_tecla,
                        altura_tecla,
                    ],
                )

            if (pos[0] > inicio_x_la and pos[0] < inicio_x_si) and pos[
                1
            ] > inicio_y_teclas:
                som_la.play()
                pygame.draw.rect(
                    tela,
                    "black",
                    [
                        inicio_x_la,
                        inicio_y_teclas,
                        largura_tecla,
                        altura_tecla,
                    ],
                )

            if pos[0] > inicio_x_si and pos[1] > inicio_y_teclas:
                som_si.play()
                pygame.draw.rect(
                    tela,
                    "black",
                    [
                        inicio_x_si,
                        inicio_y_teclas,
                        largura_tecla,
                        altura_tecla,
                    ],
                )

            pygame.draw.circle(tela, "white", (pos), 5)
            pygame.draw.circle(tela, "black", (pos), 3)

            texto = fonte.render("MEU PYANO", True, "white")
            tela.blit(texto, [(180), (60)])
            texto_do = fonte.render("DÓ", True, "white")
            tela.blit(texto_do, [(10), (400)])
            texto_re = fonte.render("RÉ", True, "white")
            tela.blit(texto_re, [(105), (400)])
            texto_mi = fonte.render("MI", True, "white")
            tela.blit(texto_mi, [(200), (400)])
            texto_fa = fonte.render("FÁ", True, "white")
            tela.blit(texto_fa, [(290), (400)])
            texto_sol = fonte.render("SOL", True, "white")
            tela.blit(texto_sol, [(360), (400)])
            texto_la = fonte.render("LÁ", True, "white")
            tela.blit(texto_la, [(470), (400)])
            texto_si = fonte.render("SI", True, "white")
            tela.blit(texto_si, [(560), (400)])

            pygame.display.flip()

        except:
            pass

        if cv2.waitKey(10) & 0xFF == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
