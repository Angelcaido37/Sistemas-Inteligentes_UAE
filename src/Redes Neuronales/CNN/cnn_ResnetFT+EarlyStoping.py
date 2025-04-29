import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import datasets, transforms, models
from torch.utils.data import DataLoader, random_split

# Transformaciones
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225])
])

# Dataset con separación entrenamiento/validación
full_train = datasets.CIFAR10(root='./data', train=True, download=True, transform=transform)
train_size = int(0.9 * len(full_train))
val_size = len(full_train) - train_size
train_data, val_data = random_split(full_train, [train_size, val_size])

test_data = datasets.CIFAR10(root='./data', train=False, download=True, transform=transform)

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)
val_loader = DataLoader(val_data, batch_size=1000)
test_loader = DataLoader(test_data, batch_size=1000)

# Modelo preentrenado
resnet = models.resnet18(pretrained=True)

#  Fine-Tuning: entrenar TODAS las capas
for param in resnet.parameters():
    param.requires_grad = True

# Reemplazar la capa final por una para CIFAR-10
resnet.fc = nn.Linear(resnet.fc.in_features, 10)

# Pérdida y optimizador
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(resnet.parameters(), lr=0.0001)

# Función de evaluación para validación
def evaluar(model, loader):
    model.eval()
    total = correct = loss_total = 0
    with torch.no_grad():
        for images, labels in loader:
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss_total += loss.item()
            preds = torch.argmax(outputs, dim=1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)
    acc = correct / total
    loss_avg = loss_total / len(loader)
    return acc, loss_avg

#  Entrenamiento con Early Stopping
def entrenar(model, train_loader, val_loader, optimizer, criterion, epochs=50, patience=5):
    best_val_loss = float('inf')
    trigger_times = 0

    for epoch in range(epochs):
        model.train()
        total_loss = 0

        for images, labels in train_loader:
            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()

        # Evaluar en validación
        val_acc, val_loss = evaluar(model, val_loader)
        print(f"Epoch {epoch+1}/{epochs} | Train Loss: {total_loss:.4f} | Val Loss: {val_loss:.4f} | Val Acc: {val_acc:.2%}")

        # Early Stopping
        if val_loss < best_val_loss:
            best_val_loss = val_loss
            trigger_times = 0
            torch.save(model.state_dict(), "best_model.pth")  # Guardar mejor modelo
        else:
            trigger_times += 1
            if trigger_times >= patience:
                print(f"Early stopping activado (no mejora en {patience} epochs)")
                break

#  Entrenar y evaluar
entrenar(resnet, train_loader, val_loader, optimizer, criterion, epochs=30, patience=5)

#  Cargar mejor modelo y evaluar en test
resnet.load_state_dict(torch.load("best_model.pth"))
test_acc, _ = evaluar(resnet, test_loader)
print(f"Precisión final en test: {test_acc:.2%}")

"""Fine-tuning total de ResNet18.

División train/val/test.

 Early stopping si la pérdida de validación no mejora.

 Guarda el mejor modelo (best_model.pth) automáticamente."""