
from Minimax import minimax

# Ejemplo simplificado de Tres en Raya
tablero = [
    ['X', 'O', ' '],
    [' ', 'X', ' '],
    ['O', ' ', ' ']
]



#Usar Minimax  para decidir la mejor jugada
mejor_valor = minimax(tablero, profundidad=3, es_maximizador=True)
print("Mejor valor:", mejor_valor)
