import cv2
import os
import time
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# === Función para dibujar texto con PIL ===
def draw_text_with_pil(img, text, position, font_size=24, color=(255, 255, 255)):
    # Convertir de BGR (OpenCV) a RGB (PIL)
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    # Cargar fuente TrueType (asegúrate de tener arial.ttf o cambia por otra)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    draw = ImageDraw.Draw(img_pil)
    draw.text(position, text, font=font, fill=color)

    # Convertir de nuevo a BGR
    return cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

# === Configuración inicial ===
output_dir = "rostros"
os.makedirs(output_dir, exist_ok=True)

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print("👤 Ingresa el nombre de la persona (sin espacios ni acentos):")
nombre_usuario = input("Nombre: ").strip().replace(" ", "_")
foto_id = 1

# === Bucle principal ===
while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ No se pudo acceder a la cámara.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    height, width = frame.shape[:2]
    center_x, center_y = width // 2, height // 2
    oval_w, oval_h = 200, 260

    # Dibujar óvalo guía
    cv2.ellipse(frame, (center_x, center_y), (oval_w, oval_h), 0, 0, 360, (0, 255, 0), 2)

    rostro_capturado = False

    for (x, y, w, h) in faces:
        face_center = (x + w // 2, y + h // 2)

        # Validar si el rostro está centrado
        if abs(face_center[0] - center_x) < 60 and abs(face_center[1] - center_y) < 80:
            frame = draw_text_with_pil(frame, "¡Rostro detectado correctamente, no se mueva!", (30, 30), 28, (0, 255, 0))
            rostro_capturado = True

            # Mostrar y esperar
            cv2.imshow("Captura de rostro", frame)
            cv2.waitKey(1000)

            rostro = frame[y:y+h, x:x+w]
            nombre_archivo = os.path.join(output_dir, f"{nombre_usuario}_{foto_id}.jpg")
            cv2.imwrite(nombre_archivo, rostro)
            print(f"✅ Rostro guardado: {nombre_archivo}")
            foto_id += 1

            # Menú después de guardar
            while True:
                frame = draw_text_with_pil(frame, "Presione 'c' para otra foto, 'n' nuevo usuario o 'q' para salir", (20, height - 40), 22)
                cv2.imshow("Captura de rostro", frame)
                key = cv2.waitKey(0) & 0xFF
                if key == ord('q'):
                    cap.release()
                    cv2.destroyAllWindows()
                    exit()
                elif key == ord('n'):
                    print("\n👤 Ingresa el nombre del nuevo usuario:")
                    nombre_usuario = input("Nombre: ").strip().replace(" ", "_")
                    foto_id = 1
                    break
                elif key == ord('c'):
                    break

    if not rostro_capturado:
        frame = draw_text_with_pil(frame, "Coloque su rostro en el óvalo", (30, 30), 28, (0, 0, 255))

    cv2.imshow("Captura de rostro", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# === Cierre ===
cap.release()
cv2.destroyAllWindows()
