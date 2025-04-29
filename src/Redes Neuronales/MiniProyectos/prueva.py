import torch

print("CUDA disponible:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("Nombre del dispositivo:", torch.cuda.get_device_name(0))
    print("Capacidad de cómputo:", torch.cuda.get_device_capability(0))
