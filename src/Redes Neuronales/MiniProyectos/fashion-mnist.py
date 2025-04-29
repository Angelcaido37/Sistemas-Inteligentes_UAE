""" Objetivo:
Entrenar la CNN creada anteriormente usando los datasets Fashion-MNIST y MNIST.

Comparar desempeño en términos de precisión, pérdida, curvas y matriz de confusión."""

from torchvision import datasets, transforms
from torch.utils.data import DataLoader

transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

# Fashion-MNIST y MNIST
train_fashion = datasets.FashionMNIST(root='./data', train=True, download=True, transform=transform)
test_fashion = datasets.FashionMNIST(root='./data', train=False, download=True, transform=transform)

train_mnist = datasets.MNIST(root='./data', train=True, download=True, transform=transform)
test_mnist = datasets.MNIST(root='./data', train=False, download=True, transform=transform)

batch_size = 64

train_loader_fashion = DataLoader(train_fashion, batch_size=batch_size, shuffle=True)
test_loader_fashion = DataLoader(test_fashion, batch_size=batch_size, shuffle=False)

train_loader_mnist = DataLoader(train_mnist, batch_size=batch_size, shuffle=True)
test_loader_mnist = DataLoader(test_mnist, batch_size=batch_size, shuffle=False)


def train_model(model, train_loader, test_loader, criterion, optimizer, device, epochs=10):
    model.to(device)
    train_loss_history = []
    train_acc_history = []

    for epoch in range(epochs):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0

        for images, labels in train_loader:
            images, labels = images.to(device), labels.to(device)

            optimizer.zero_grad()
            outputs = model(images)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * images.size(0)
            _, predicted = torch.max(outputs, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()

        epoch_loss = running_loss / len(train_loader.dataset)
        epoch_acc = correct / total
        train_loss_history.append(epoch_loss)
        train_acc_history.append(epoch_acc)
        print(f"Epoch [{epoch+1}/{epochs}], Loss: {epoch_loss:.4f}, Accuracy: {epoch_acc:.4f}")

    return train_loss_history, train_acc_history

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Fashion-MNIST
model_fashion = CustomCNN()
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model_fashion.parameters(), lr=0.001)

print("Entrenando en Fashion-MNIST")
train_model(model_fashion, train_loader_fashion, test_loader_fashion, criterion, optimizer, device)

# MNIST
model_mnist = CustomCNN()
optimizer2 = torch.optim.Adam(model_mnist.parameters(), lr=0.001)

print("Entrenando en MNIST")
train_model(model_mnist, train_loader_mnist, test_loader_mnist, criterion, optimizer2, device)

# Comparación y Visualización: