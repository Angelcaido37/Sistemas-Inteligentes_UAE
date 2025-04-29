"""MLP con tecnicas 
Dropout	Cuando tienes poca data o ves overfitting.
BatchNorm	En redes profundas, para mejorar la estabilidad y velocidad de entrenamiento."""

import torch
import torch.nn as nn
import torch.optim as optim
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Cargar el dataset Iris
iris = load_iris()
X = iris.data
y = iris.target

# Normalizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Convertir a tensores de PyTorch
X_tensor = torch.tensor(X_scaled, dtype=torch.float32)
y_tensor = torch.tensor(y, dtype=torch.long)

# Separar en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X_tensor, y_tensor, test_size=0.2, random_state=42)

#  Modelo con Dropout y BatchNorm
class MLP(nn.Module):
    def __init__(self):
        super(MLP, self).__init__()

        # Capa oculta 1: 4 → 10
        self.hidden1 = nn.Linear(4, 10)
        self.bn1 = nn.BatchNorm1d(10)       # BatchNorm para normalizar la salida
        self.dropout1 = nn.Dropout(0.3)     # Dropout con 30% de probabilidad

        # Capa oculta 2: 10 → 6
        self.hidden2 = nn.Linear(10, 6)
        self.bn2 = nn.BatchNorm1d(6)
        self.dropout2 = nn.Dropout(0.3)

        # Capa de salida: 6 → 3 (3 clases)
        self.output = nn.Linear(6, 3)

    def forward(self, x):
        # Capa 1 con ReLU, BatchNorm y Dropout
        x = torch.relu(self.bn1(self.hidden1(x)))
        x = self.dropout1(x)

        # Capa 2 con ReLU, BatchNorm y Dropout
        x = torch.relu(self.bn2(self.hidden2(x)))
        x = self.dropout2(x)

        # Capa de salida (sin softmax porque lo maneja la función de pérdida)
        x = self.output(x)
        return x

# Instanciar modelo, función de pérdida y optimizador
model = MLP()
criterion = nn.CrossEntropyLoss()  # Para clasificación multiclase
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Entrenamiento del modelo
epochs = 300
for epoch in range(epochs):
    model.train()
    optimizer.zero_grad()
    output = model(X_train)
    loss = criterion(output, y_train)
    loss.backward()
    optimizer.step()

# Evaluación en test
model.eval()
with torch.no_grad():
    y_logits = model(X_test)
    y_pred = torch.argmax(y_logits, dim=1)
    accuracy = (y_pred == y_test).float().mean()

print(f"Precisión en conjunto de prueba: {accuracy.item():.2f}")
