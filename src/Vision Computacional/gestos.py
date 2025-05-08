import cv2
import mediapipe as mp

# Inicializar MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.5
)

# Abrir cámara
cap = cv2.VideoCapture(0)

# Función para detectar gesto
def detectar_gesto(hand_landmarks):
    dedos_abiertos = 0

    # Coordenadas de referencia (eje Y para vertical)
    finger_tips = [8, 12, 16, 20]  # Índice, medio, anular, meñique
    finger_dips = [6, 10, 14, 18]

    for tip, dip in zip(finger_tips, finger_dips):
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[dip].y:
            dedos_abiertos += 1

    # Pulgar (eje X para horizontal)
    if hand_landmarks.landmark[4].x > hand_landmarks.landmark[3].x:
        pulgar_arriba = True
    else:
        pulgar_arriba = False

    # Clasificación simple
    if dedos_abiertos == 4 and pulgar_arriba:
        return "Mano abierta"
    elif dedos_abiertos == 0 and not pulgar_arriba:
        return "Puño"
    elif dedos_abiertos == 0 and pulgar_arriba:
        return "Pulgar arriba"
    else:
        return "Gesto no identificado"

# Bucle principal
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Dibujar mano
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Detectar gesto
            gesto = detectar_gesto(hand_landmarks)
            cv2.putText(frame, gesto, (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Mostrar imagen
    cv2.imshow("Detección de Gestos", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


