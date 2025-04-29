"""
Esta red tiene:
Dos entradas.
Una sola neurona.
Función de activación escalón (step).
Regla de aprendizaje del perceptrón. 
utiliza: OR o NAND para probar otros comportamientos.
"""

import numpy as np
# Datos: compuerta lógica AND
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([[0], [0], [0], [1]])

# Inicialización de pesos y bias
np.random.seed(42) #Fija una semilla para la generación de números aleatorios. Esto asegura que los resultados sean reproducibles (es decir, siempre se generarán los mismos números aleatorios).

weights = np.random.rand(2, 1) # Inicializa los pesos del perceptrón como un vector de tamaño (2, 1) con valores aleatorios entre 0 y 1. Estos pesos representan la importancia de cada entrada en la decisión final.
bias = np.random.rand(1) #Inicializa el sesgo (o bias) como un valor escalar aleatorio. El sesgo actúa como un término adicional que permite ajustar la salida del modelo.

# Función de activación: escalón
def step_function(x): #Esta función define la función de activación del perceptrón
    return np.where(x > 0, 1, 0) #Si el valor de entrada (x) es mayor que 0, devuelve 1.
                                 #Si el valor de entrada (x) es menor o igual a 0, devuelve 0.
# Hiperparámetros
learning_rate = 0.1 # Es la tasa de aprendizaje , que controla cuánto se ajustan los pesos y el sesgo en cada iteración del entrenamiento. Un valor más bajo hace que el modelo aprenda más lentamente, mientras que un valor más alto puede hacer que el modelo sea inestable.
epochs = 20 #Es el número de veces que el modelo recorrerá todo el conjunto de datos durante el entrenamiento. Cada "época" implica una pasada completa por todas las muestras de entrenamiento.


# Entrenamiento
for epoch in range(epochs):
    for i in range(len(X)):
        z = np.dot(X[i], weights) + bias
        y_pred = step_function(z)
        error = y[i] - y_pred
        weights += learning_rate * error * X[i].reshape(2, 1)
        bias += learning_rate * error

# Predicción final
z = np.dot(X, weights) + bias
y_pred_final = step_function(z)

# Mostrar resultados
for i in range(len(X)):
    print(f"Entrada: {X[i]} -> Predicción: {y_pred_final[i][0]} (Esperado: {y[i][0]})")

print("\nPesos finales:", weights.flatten())
print("Bias final:", bias[0])
