


from heapq import nlargest #Usamos heapq.nlargest para seleccionar los beam_width nodos con las mejores evaluaciones.

def beam_search(inicio, beam_width, funcion_evaluacion, objetivo):
    nodos_actuales = [(funcion_evaluacion(inicio), [inicio])]

    while nodos_actuales:
        nuevos_nodos = []

        for _, camino in nodos_actuales:
            nodo_actual = camino[-1]

            if nodo_actual == objetivo:
                return camino

            for sucesor in generar_sucesores(nodo_actual):
                nuevo_camino = camino + [sucesor]
                nuevos_nodos.append((funcion_evaluacion(sucesor), nuevo_camino))

        nodos_actuales = nlargest(beam_width, nuevos_nodos, key=lambda x: -x[0])  # Nota: usar `-x[0]` si minimizas

    return None

def generar_sucesores(nodo): #La función generar_sucesores devuelve los posibles estados siguientes para un nodo dado.
    return [nodo + 1, nodo - 1]

def funcion_evaluacion(nodo, objetivo): #La función funcion_evaluacion asigna un valor a cada nodo basado en su "calidad". En este ejemplo, minimizamos la distancia al objetivo.
    return abs(objetivo - nodo)

# Ejemplo de uso
if __name__ == "__main__": #Si se encuentra el objetivo, se retorna el camino. Si no quedan nodos para expandir, se retorna None.
    inicio = 0
    beam_width = 2
    objetivo = 10

    camino = beam_search(
        inicio,
        beam_width,
        lambda nodo: funcion_evaluacion(nodo, objetivo),
        objetivo
    )

    if camino:
        print(f"Camino encontrado: {camino}")
    else:
        print("No se encontró un camino.")
