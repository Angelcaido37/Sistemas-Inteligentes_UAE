import cv2
import mediapipe as mp
from PIL import ImageFont, ImageDraw, Image
import numpy as np

# -----------------------
# Función para mostrar texto con ñ y tildes
def dibujar_texto_unicode(img, texto, posicion=(10, 40), color=(255, 0, 0), tamaño=32):
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)
    fuente = ImageFont.truetype("arial.ttf", tamaño)  # Usa otra TTF si lo deseas
    draw.text(posicion, texto, font=fuente, fill=color)
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

# -----------------------
# Inicializar MediaPipe
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

# -----------------------
# Función de detección de gestos simples
def detectar_gesto(hand_landmarks):
    dedos_abiertos = 0
    finger_tips = [8, 12, 16, 20]  # Índice, medio, anular, meñique
    finger_dips = [6, 10, 14, 18]

    for tip, dip in zip(finger_tips, finger_dips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[dip].y:
            dedos_abiertos += 1

    pulgar_arriba = hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x

    if dedos_abiertos == 4 and pulgar_arriba:
        return "✋ Mano abierta"
    elif dedos_abiertos == 0 and not pulgar_arriba:
        return "✊ Puño"
    elif dedos_abiertos == 0 and pulgar_arriba:
        return "👍 Pulgar arriba"
    else:
        return "🤔 Gesto no identificado"

# -----------------------
# Iniciar cámara
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("No se pudo acceder a la cámara")
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            gesto = detectar_gesto(hand_landmarks)
            frame = dibujar_texto_unicode(frame, gesto, posicion=(10, 40), color=(0, 0, 255))

    cv2.imshow("Detección de Gestos", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
