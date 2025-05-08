import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Cargar datos MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocesamiento
x_train = x_train.reshape(-1, 28*28).astype("float32") / 255.0 #Imagenes entrenamiento
x_test = x_test.reshape(-1, 28*28).astype("float32") / 255.0 #imagenes de prueba
y_train_cat = to_categorical(y_train, 10) #etiqueta  de entrenamiento
y_test_cat = to_categorical(y_test, 10) #etiquetas de pruebas

# Modelo MLP con Dropout y BatchNorm
#Primera capa
model = models.Sequential([ #define un modelo de capas apiladas en orden.
    layers.Input(shape=(784,)), #define que la entrada tiene 784 características (vector plano de imagen).
    layers.Dense(256), #una capa totalmente conectada con 256 neuronas.
    layers.BatchNormalization(), #normaliza la salida para acelerar el entrenamiento y hacerlo más establ
    layers.Activation("relu"), #usa la activación ReLU (Rectified Linear Unit), que hace el modelo más no lineal.
    layers.Dropout(0.3), #apaga el 30% de las neuronas al azar durante cada actualización de pesos (para evitar overfitting).

#segunda capa
    layers.Dense(128),
    layers.BatchNormalization(),
    layers.Activation("relu"),
    layers.Dropout(0.3),

    layers.Dense(10, activation="softmax")  # 10 clases y transforma las salidas en probabilidades (entre 0 y 1) que suman 1.
])

# Compilar el modelo
model.compile(
    optimizer="adam", # usa el optimizador Adam (muy bueno para problemas de clasificación).
    loss="categorical_crossentropy", #función de pérdida para problemas de clasificación multiclase con etiquetas one-hot.
    metrics=["accuracy"] #mide la exactitud durante el entrenamiento y validación.
)

# Entrenamiento
model.fit(x_train, y_train_cat, epochs=5, batch_size=64, validation_split=0.1)

"""fit: entrena el modelo.

epochs=5: hace 5 pasadas completas sobre los datos de entrenamiento.

batch_size=64: usa lotes de 64 ejemplos antes de actualizar los pesos.

validation_split=0.1: guarda el 10% de los datos de entrenamiento para validar (evaluar el modelo durante el entrenamiento)."""

#Evaluación
loss, accuracy = model.evaluate(x_test, y_test_cat)
print(f"Precisión en test: {accuracy:.2%}")

"""evaluate: mide el desempeño en los datos que el modelo no ha visto.
e Imprime la precisión final como porcentaje."""

# Cargar los datos MNIST
(x_train, y_train), (_, _) = mnist.load_data()
# Mostrar la primera imagen del dataset
plt.imshow(x_train[0], cmap="gray")
plt.title(f"Etiqueta: {y_train[0]}")
plt.axis("off")
plt.show()