import torch
import torch.nn as nn
import torch.optim as optim

# Datos de entrada (ingresos mensuales, deuda total)
X = torch.tensor([[5000, 1000], [3000, 2500], [7000, 500], [2000, 4000],
                  [6000, 800], [4000, 3000], [1000, 5000]], dtype=torch.float32)

# Etiquetas (0 = rechazado, 1 = aprobado)
y = torch.tensor([[1], [0], [1], [0], [1], [0], [0]], dtype=torch.float32)

# Normalizar los datos
X_mean = X.mean(dim=0)
X_std = X.std(dim=0)
X_normalized = (X - X_mean) / X_std

# Definir el modelo
class LoanApprovalModel(nn.Module):
    def __init__(self):
        super(LoanApprovalModel, self).__init__()
        self.linear = nn.Linear(2, 1)
        # Inicialización manual de los pesos
        nn.init.xavier_uniform_(self.linear.weight)
        nn.init.zeros_(self.linear.bias)
    
    def forward(self, x):
        return torch.sigmoid(self.linear(x))

# Instanciar el modelo
model = LoanApprovalModel()

# Definir la función de pérdida y el optimizador
criterion = nn.BCELoss()  # Binary Cross Entropy Loss
optimizer = optim.SGD(model.parameters(), lr=0.01)

# Entrenamiento del modelo
epochs = 5000  # Número de épocas
for epoch in range(epochs):
    # Paso 1: Realizar una predicción
    predictions = model(X_normalized)
    
    # Paso 2: Calcular la pérdida
    loss = criterion(predictions, y)
    
    # Paso 3: Calcular los gradientes
    optimizer.zero_grad()  # Limpiar gradientes anteriores
    loss.backward()        # Calcular gradientes
    
    # Paso 4: Actualizar los parámetros
    optimizer.step()
    
    # Mostrar la pérdida cada 500 épocas
    if (epoch + 1) % 500 == 0:
        print(f"Época {epoch+1}/{epochs}, Pérdida: {loss.item():.4f}")

# Hacer predicciones con el modelo entrenado
print("\nPredicciones finales:")
with torch.no_grad():  # Desactivar el cálculo de gradientes
    predictions = model(X_normalized)
    for i, pred in enumerate(predictions):
        decision = "Aprobado" if pred >= 0.5 else "Rechazado"
        print(f"Solicitante {i+1}: Ingresos={X[i][0]:.0f}, Deuda={X[i][1]:.0f} -> Predicción: {pred.item():.4f} ({decision})")