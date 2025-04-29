# Minimax.py

def es_estado_terminal(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != ' ':
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != ' ':
            return True
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != ' ':
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != ' ':
        return True
    return all(c != ' ' for fila in tablero for c in fila)

def evaluar_estado(tablero):
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2]:
            if tablero[i][0] == 'X': return 10
            elif tablero[i][0] == 'O': return -10
        if tablero[0][i] == tablero[1][i] == tablero[2][i]:
            if tablero[0][i] == 'X': return 10
            elif tablero[0][i] == 'O': return -10
    if tablero[0][0] == tablero[1][1] == tablero[2][2]:
        if tablero[0][0] == 'X': return 10
        elif tablero[0][0] == 'O': return -10
    if tablero[0][2] == tablero[1][1] == tablero[2][0]:
        if tablero[0][2] == 'X': return 10
        elif tablero[0][2] == 'O': return -10
    return 0

def generar_movimientos_posibles(tablero):
    return [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == ' ']

def aplicar_movimiento(tablero, movimiento):
    i, j = movimiento
    nuevo_tablero = [fila[:] for fila in tablero]
    nuevo_tablero[i][j] = 'X'
    return nuevo_tablero

def poda_alfa_beta(tablero, profundidad, alfa, beta, es_maximizador):
    if profundidad == 0 or es_estado_terminal(tablero):
        return evaluar_estado(tablero), None

    mejor_movimiento = None

    if es_maximizador:
        max_eval = float('-inf')
        for movimiento in generar_movimientos_posibles(tablero):
            nuevo_estado = aplicar_movimiento(tablero, movimiento, 'X')
            valor, _ = poda_alfa_beta(nuevo_estado, profundidad - 1, alfa, beta, False)
            if valor > max_eval:
                max_eval = valor
                mejor_movimiento = movimiento
            alfa = max(alfa, valor)
            if beta <= alfa:
                break
        return max_eval, mejor_movimiento
    else:
        min_eval = float('inf')
        for movimiento in generar_movimientos_posibles(tablero):
            nuevo_estado = aplicar_movimiento(tablero, movimiento, 'O')
            valor, _ = poda_alfa_beta(nuevo_estado, profundidad - 1, alfa, beta, True)
            if valor < min_eval:
                min_eval = valor
                mejor_movimiento = movimiento
            beta = min(beta, valor)
            if beta <= alfa:
                break
        return min_eval, mejor_movimiento

def minimax(estado, profundidad, es_maximizador):
    if profundidad == 0 or es_estado_terminal(estado):
        return evaluar_estado(estado)

    if es_maximizador:
        mejor_valor = float('-inf')
        for movimiento in generar_movimientos_posibles(estado):
            nuevo_estado = aplicar_movimiento(estado, movimiento)
            valor = minimax(nuevo_estado, profundidad - 1, False)
            mejor_valor = max(mejor_valor, valor)
        return mejor_valor
    else:
        mejor_valor = float('inf')
        for movimiento in generar_movimientos_posibles(estado):
            nuevo_estado = aplicar_movimiento(estado, movimiento)
            valor = minimax(nuevo_estado, profundidad - 1, True)
            mejor_valor = min(mejor_valor, valor)
        return mejor_valor
