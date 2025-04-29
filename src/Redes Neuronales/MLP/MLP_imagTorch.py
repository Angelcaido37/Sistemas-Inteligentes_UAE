import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

# Transformaciones para MNIST: convertir a tensor y normalizar
transform = transforms.Compose([
    transforms.ToTensor(),  # Convierte a tensor
    transforms.Normalize((0.1307,), (0.3081,))  # Normaliza con media y desviación estándar
])

#Cargar datos
train_data = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_data = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = DataLoader(test_data, batch_size=1000)

#MLP con Dropout y BatchNorm para imágenes de MNIST
class MLP_MNIST(nn.Module):
    def __init__(self):
        super(MLP_MNIST, self).__init__()
        self.flatten = nn.Flatten()

        self.fc1 = nn.Linear(28 * 28, 256)
        self.bn1 = nn.BatchNorm1d(256)
        self.dropout1 = nn.Dropout(0.3)

        self.fc2 = nn.Linear(256, 128)
        self.bn2 = nn.BatchNorm1d(128)
        self.dropout2 = nn.Dropout(0.3)

        self.fc3 = nn.Linear(128, 10)  # 10 clases (0–9)

    def forward(self, x):
        x = self.flatten(x)
        x = torch.relu(self.bn1(self.fc1(x)))
        x = self.dropout1(x)
        x = torch.relu(self.bn2(self.fc2(x)))
        x = self.dropout2(x)
        x = self.fc3(x)  # logits sin softmax
        return x

#Entrenamiento
def entrenar(model, train_loader, optimizer, criterion, epochs=5):
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch+1}/{epochs} - Loss: {total_loss:.4f}")

# Evaluación
def evaluar(model, test_loader):
    model.eval()
    correctos = 0
    total = 0
    with torch.no_grad():
        for images, labels in test_loader:
            outputs = model(images)
            pred = torch.argmax(outputs, dim=1)
            correctos += (pred == labels).sum().item()
            total += labels.size(0)
    print(f"Precisión en test: {correctos / total:.2%}")

# Instancia del modelo, pérdida y optimizador
model = MLP_MNIST()
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Entrenar y Evaluar
entrenar(model, train_loader, optimizer, criterion, epochs=5)
evaluar(model, test_loader)


"""Cómo aplicar una MLP a imágenes reales (convertidas en vectores).

Cómo usar BatchNorm y Dropout en una red profunda para mejorar rendimiento.

Cómo integrar torchvision y DataLoader para datasets reales."""