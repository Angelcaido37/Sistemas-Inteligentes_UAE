import torch
import torch.nn as nn
import torch.optim as optim

# Datos: XOR (no linealmente separable)
X = torch.tensor([
    [0.0, 0.0],
    [0.0, 1.0],
    [1.0, 0.0],
    [1.0, 1.0]
])
y = torch.tensor([
    [0.0],
    [1.0],
    [1.0],
    [0.0]
])

# Modelo 1: Perceptrón simple (sin capa oculta)
class Perceptron(nn.Module):
    def __init__(self):
        super(Perceptron, self).__init__()
        self.linear = nn.Linear(2, 1)

    def forward(self, x):
        return torch.sigmoid(self.linear(x))

#Modelo 2: MLP con una capa oculta
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()
        self.hidden = nn.Linear(2, 4)
        self.out = nn.Linear(4, 1)

    def forward(self, x):
        x = torch.relu(self.hidden(x))
        return torch.sigmoid(self.out(x))

# Entrenamiento para ambos modelos
def entrenar(modelo, X, y, epochs=5000, lr=0.1):
    criterion = nn.BCELoss()
    optimizer = optim.SGD(modelo.parameters(), lr=lr)
    for _ in range(epochs):
        optimizer.zero_grad()
        outputs = modelo(X)
        loss = criterion(outputs, y)
        loss.backward()
        optimizer.step()
    return modelo

# Entrenar Perceptrón
modelo_perceptron = Perceptron()
entrenar(modelo_perceptron, X, y)

# Entrenar MLP
modelo_mlp = MLP()
entrenar(modelo_mlp, X, y)

# Evaluación
with torch.no_grad():
    pred_perceptron = (modelo_perceptron(X) > 0.5).float()
    pred_mlp = (modelo_mlp(X) > 0.5).float()

# Mostrar resultados
print("Resultados XOR con Perceptrón:")
for i in range(len(X)):
    print(f"Entrada: {X[i].tolist()} -> Pred: {int(pred_perceptron[i].item())} (Esperado: {int(y[i].item())})")

print("\nResultados XOR con MLP:")
for i in range(len(X)):
    print(f"Entrada: {X[i].tolist()} -> Pred: {int(pred_mlp[i].item())} (Esperado: {int(y[i].item())})")
