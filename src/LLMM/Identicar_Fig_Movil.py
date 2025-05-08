import tkinter as tk
from tkinter import filedialog, Label, Button
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions, preprocess_input

# Cargar modelo
model = MobileNetV2(weights='imagenet')

# Función para cargar y predecir imagen
def cargar_imagen():
    file_path = filedialog.askopenfilename(
    initialdir="/storage/emulated/0/​Android/data/ru.iiec.pydroid3/files",
    filetypes=[("Archivos de imagen", "*.jpg *.jpeg *.png")]
    )
    if not file_path:
        return

    img = Image.open(file_path).resize((224, 224))
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    decoded = decode_predictions(preds, top=3)[0]

    # Mostrar imagen
    img_display = Image.open(file_path).resize((200, 200))
    img_tk = ImageTk.PhotoImage(img_display)
    panel.config(image=img_tk)
    panel.image = img_tk

 # Mostrar predicciones
    resultado = "\n".join([f"{i+1}. {label}: {prob*100:.2f}%" for i, (_, label, prob) in enumerate(decoded)])
    resultado_label.config(text=resultado)

# Interfaz gráfica
ventana = tk.Tk()
ventana.title("Clasificador de Imágenes (MobileNetV2)")

btn_cargar = Button(ventana, text="Seleccionar Imagen", command=cargar_imagen)
btn_cargar.pack(pady=10)

panel = Label(ventana)
panel.pack()

resultado_label = Label(ventana, text="", font=("Arial", 12), justify="left")
resultado_label.pack(pady=10)

ventana.mainloop()