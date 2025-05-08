import cv2
import numpy as np

# === Función avanzada de detección de color por HSV ===
def detectar_color_avanzado_v2(h, s, v):
    if s < 40 and v > 200:
        return "Blanco"
    elif s < 40 and v < 80:
        return "Negro"
    elif s < 50:
        return "Gris"

    if (h >= 0 and h <= 10) or (h >= 170 and h <= 180):
        return "Rojo"
    elif 11 <= h <= 20:
        return "Naranja"
    elif 21 <= h <= 34:
        return "Amarillo"
    elif 35 <= h <= 70:
        return "Verde"
    elif 71 <= h <= 84:
        return "Verde azulado"
    elif 85 <= h <= 95:
        return "Cian"
    elif 96 <= h <= 105:
        return "Turquesa"
    elif 106 <= h <= 120:
        return "Azul"
    elif 121 <= h <= 135:
        return "Azul oscuro"
    elif 136 <= h <= 160:
        return "Morado"
    elif 161 <= h <= 169:
        return "Rosa fuerte"
    else:
        return "Desconocido"

# === Función para obtener código HEX desde BGR ===
def bgr_to_hex(bgr):
    return "#{:02X}{:02X}{:02X}".format(bgr[2], bgr[1], bgr[0])

# === Inicializar cámara ===
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    blurred = cv2.GaussianBlur(frame, (7, 7), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    height, width = frame.shape[:2]
    box_w, box_h = 200, 200
    cx, cy = width // 2, height // 2

    x1 = cx - box_w // 2
    y1 = cy - box_h // 2
    x2 = cx + box_w // 2
    y2 = cy + box_h // 2

    # Dibujar recuadro guía
    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 255, 255), 2)

    roi = hsv[y1:y2, x1:x2]
    avg_hsv = np.mean(roi.reshape(-1, 3), axis=0).astype(int)
    h, s, v = avg_hsv

    color_name = detectar_color_avanzado_v2(h, s, v)

    # Convertir HSV a BGR para mostrar color real
    bgr_color = cv2.cvtColor(np.uint8([[[h, s, v]]]), cv2.COLOR_HSV2BGR)[0][0].tolist()
    bgr_color = tuple(int(c) for c in bgr_color)
    hex_color = bgr_to_hex(bgr_color)

    # Mostrar cuadro de color
    cv2.rectangle(frame, (10, 10), (160, 110), bgr_color, -1)

    # Mostrar nombre, RGB y HEX
    cv2.putText(frame, f"{color_name}", (170, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
    cv2.putText(frame, f"RGB: {bgr_color}", (170, 80), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200,200,200), 2)
    cv2.putText(frame, f"HEX: {hex_color}", (170, 110), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (200,200,200), 2)

    cv2.imshow("Color del objeto en el centro", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
