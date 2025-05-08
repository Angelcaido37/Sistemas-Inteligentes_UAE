import cv2
import os
import time

# Crear carpeta si no existe
output_dir = "rostros"
os.makedirs(output_dir, exist_ok=True)

# Inicializar cámara
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

print("🧑 Ingresa el nombre de la persona (sin espacios ni acentos):")
nombre_usuario = input("Nombre: ").strip().replace(" ", "_")

foto_id = 1  # Contador de fotos por usuario

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ No se pudo acceder a la cámara.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    mensaje = "Coloque su rostro en el óvalo"
    rostro_capturado = False

    height, width = frame.shape[:2]
    center_x, center_y = width // 2, height // 2
    oval_w, oval_h = 200, 260

    # Dibujar óvalo guía
    cv2.ellipse(frame, (center_x, center_y), (oval_w, oval_h), 0, 0, 360, (0, 255, 0), 2)

    for (x, y, w, h) in faces:
        face_center = (x + w // 2, y + h // 2)

        # Validar que el rostro esté centrado
        if abs(face_center[0] - center_x) < 60 and abs(face_center[1] - center_y) < 80:
            mensaje = "¡Rostro detectado correctamente, no se mueva!"
            cv2.putText(frame, mensaje, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)
            rostro_capturado = True

            # Esperar 1 segundo y capturar
            cv2.imshow("Captura de rostro", frame)
            cv2.waitKey(1000)

            rostro = frame[y:y+h, x:x+w]
            nombre_archivo = os.path.join(output_dir, f"{nombre_usuario}_{foto_id}.jpg")
            cv2.imwrite(nombre_archivo, rostro)
            print(f"✅ Rostro guardado: {nombre_archivo}")
            foto_id += 1

            # Preguntar si quiere capturar otro rostro
            while True:
                cv2.putText(frame, "Presione 'c' para otra foto, 'n' nuevo usuario o 'q' para salir",
                            (20, height - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
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
        cv2.putText(frame, mensaje, (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

    cv2.imshow("Captura de rostro", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
