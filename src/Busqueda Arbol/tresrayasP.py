
from poda import poda_alfa_beta

# Ejemplo simplificado de Tres en Raya
tablero = [
    ['X', 'O', ' '],
    [' ', 'X', ' '],
    ['O', ' ', ' ']
]

valor, movimiento = poda_alfa_beta(
    tablero,
    profundidad=5,
    alfa = float('-inf')  # Inicialmente, MAX no ha encontrado nada, empieza desde el peor posible
    beta = float('inf')   # Inicialmente, MIN no ha encontrado nada, empieza desde el mejor posible
    es_maximizador=True  # 'X' es el jugador maximizador
)

#  Poda Alfa-Beta para decidir la mejor jugada
print("Mejor valor:", valor)
print("Mejor movimiento:", movimiento)
