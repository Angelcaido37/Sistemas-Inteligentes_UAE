import torch
import torch.nn as nn
import torch.optim as optim

# Datos: compuerta lógica AND
X = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])
y = torch.tensor([
    [0.0],
    [0.0],
    [0.0],
    [1.0]
])

# Definir el modelo: un perceptrón simple (una neurona)
class Perceptron(nn.Module):
    def __init__(self):
        super(Perceptron, self).__init__()
        self.linear = nn.Linear(2, 1)  # 2 entradas, 1 salida

    def forward(self, x):
        out = self.linear(x)
        return torch.sigmoid(out)  # activación sigmoide

# Instanciar el modelo
model = Perceptron()

# Definir función de pérdida y optimizador
criterion = nn.BCELoss()  # Binary Cross Entropy
optimizer = optim.SGD(model.parameters(), lr=0.1)

# Entrenamiento
epochs = 100
for epoch in range(epochs):
    optimizer.zero_grad()
    outputs = model(X)
    loss = criterion(outputs, y)
    loss.backward()
    optimizer.step()

# Evaluación final
with torch.no_grad():
    outputs = model(X)
    predictions = (outputs > 0.5).float()

# Mostrar resultados
for i in range(len(X)):
    print(f"Entrada: {X[i].tolist()} -> Predicción: {int(predictions[i].item())} (Esperado: {int(y[i].item())})")

# Pesos y bias aprendidos
print("\nPesos:", model.linear.weight.data.numpy())
print("Bias:", model.linear.bias.data.numpy())

"""
Se utiliza torch.sigmoid para convertir la salida a un rango entre 0 y 1.
La predicción final se redondea: > 0.5 se convierte en 1 (clase positiva).
"""