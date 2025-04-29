import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Cargar datos MNIST
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Preprocesamiento
x_train = x_train.reshape(-1, 28*28).astype("float32") / 255.0
x_test = x_test.reshape(-1, 28*28).astype("float32") / 255.0
y_train_cat = to_categorical(y_train, 10)
y_test_cat = to_categorical(y_test, 10)

# Modelo MLP con Dropout y BatchNorm
model = models.Sequential([
    layers.Input(shape=(784,)),
    layers.Dense(256),
    layers.BatchNormalization(),
    layers.Activation("relu"),
    layers.Dropout(0.3),

    layers.Dense(128),
    layers.BatchNormalization(),
    layers.Activation("relu"),
    layers.Dropout(0.3),

    layers.Dense(10, activation="softmax")  # 10 clases
])

# Compilar el modelo
model.compile(
    optimizer="adam",
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)

# Entrenamiento
model.fit(x_train, y_train_cat, epochs=5, batch_size=64, validation_split=0.1)

#Evaluación
loss, accuracy = model.evaluate(x_test, y_test_cat)
print(f"Precisión en test: {accuracy:.2%}")
