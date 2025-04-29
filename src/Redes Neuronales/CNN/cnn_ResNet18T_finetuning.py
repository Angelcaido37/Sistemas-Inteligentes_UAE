import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader

# Transformaciones (más parecidas a ImageNet)
transform = transforms.Compose([
    transforms.Resize((224, 224)),               # Redimensionar a lo que espera ResNet
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],  # Media y desviación estándar de ImageNet
                         std=[0.229, 0.224, 0.225])
])

# Dataset
train_data = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
test_data = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = DataLoader(test_data, batch_size=1000)

# Cargar modelo preentrenado ResNet18
resnet = models.resnet18(pretrained=True)

# FINE-TUNING: permitir que TODAS las capas se entrenen
for param in resnet.parameters():
    param.requires_grad = True  # 🔥 Ahora se entrenan TODAS las capas, no solo la final

# Reemplazar la capa final por una de 10 clases
resnet.fc = nn.Linear(resnet.fc.in_features, 10)

#  Crear optimizador para TODA la red (no solo la capa final)
optimizer = optim.Adam(resnet.parameters(), lr=0.0001)  # LR bajo para no dañar pesos preentrenados
criterion = nn.CrossEntropyLoss()

#  Entrenamiento
def entrenar(model, loader, optimizer, criterion, epochs=5):
    model.train()
    for epoch in range(epochs):
        total_loss = 0
        for images, labels in loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        print(f"Epoch {epoch+1}/{epochs}, Loss: {total_loss:.4f}")

# Evaluación
def evaluar(model, loader):
    model.eval()
    total = correct = 0
    with torch.no_grad():
        for images, labels in loader:
            outputs = model(images)
            preds = torch.argmax(outputs, dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    print(f"Precisión en test: {correct / total:.2%}")

# Ejecutar
entrenar(resnet, train_loader, optimizer, criterion, epochs=5)
evaluar(resnet, test_loader)
