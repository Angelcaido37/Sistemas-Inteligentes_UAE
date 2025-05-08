#Instalar el .whl
# Pip install face_recognition

import face_recognition
import cv2
import os

# === 1. Cargar imágenes de personas conocidas ===
known_face_encodings = []
known_face_names = []

path = "rostros"  # Carpeta con los .jpg

for filename in os.listdir(path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        image_path = os.path.join(path, filename)
        image = face_recognition.load_image_file(image_path)
        encoding = face_recognition.face_encodings(image)

        if encoding:  # Asegurarse que encontró rostro
            known_face_encodings.append(encoding[0])
            name = os.path.splitext(filename)[0]  # Nombre sin .jpg
            known_face_names.append(name)
        else:
            print(f"No se detectó rostro en {filename}")

# === 2. Activar cámara ===
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Reducir imagen para procesar más rápido
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

    # === 3. Detectar y codificar rostro en vivo ===
    face_locations = face_recognition.face_locations(rgb_small)
    face_encodings = face_recognition.face_encodings(rgb_small, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # === 4. Comparar con rostros conocidos ===
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
        name = "Desconocido"

        if True in matches:
            index = matches.index(True)
            name = known_face_names[index]

        # === 5. Dibujar recuadro y nombre ===
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

    cv2.imshow("Reconocimiento Facial", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
