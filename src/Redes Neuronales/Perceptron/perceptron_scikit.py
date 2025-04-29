from sklearn.linear_model import Perceptron
import numpy as np

# Datos de entrada: compuerta lógica AND
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])
y = np.array([0, 0, 0, 1])  # Salida esperada

# Crear el modelo del perceptrón
modelo = Perceptron(max_iter=1000, eta0=0.1, random_state=42)

# Entrenar el modelo
modelo.fit(X, y)

# Hacer predicciones
predicciones = modelo.predict(X)

# Mostrar resultados
for i in range(len(X)):
    print(f"Entrada: {X[i]} -> Predicción: {predicciones[i]} (Esperado: {y[i]})")

# Mostrar pesos y bias
print("\nPesos aprendidos:", modelo.coef_[0])
print("Bias aprendido:", modelo.intercept_[0])
