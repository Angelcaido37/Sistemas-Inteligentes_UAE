
# Definición de un árbol binario
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None


def recorrido_pre_orden_iterativo(raiz):
    """
    Realiza un recorrido en pre-orden iterativo de un árbol binario.
    :param raiz: Nodo raíz del árbol.
    """
    if raiz is None:
        return
    
    pila = [raiz]  # Inicializar la pila con el nodo raíz

    while pila:
        nodo_actual = pila.pop()  # Extraer el nodo superior de la pila
        print(nodo_actual.valor, end=" ")  # Visitar el nodo actual

        # Agregar los hijos a la pila (primero el derecho, luego el izquierdo)
        if nodo_actual.derecha:
            pila.append(nodo_actual.derecha)
        if nodo_actual.izquierda:
            pila.append(nodo_actual.izquierda)

# Ejemplo de uso
if __name__ == "__main__":
    # Construir un árbol binario
    """
    Árbol construido:
            4
           / \
          2   6
         / \ / \
        1  3 5  7
    """
    raiz = Nodo(4)
    raiz.izquierda = Nodo(2)
    raiz.derecha = Nodo(6)
    raiz.izquierda.izquierda = Nodo(1)
    raiz.izquierda.derecha = Nodo(3)
    raiz.derecha.izquierda = Nodo(5)
    raiz.derecha.derecha = Nodo(7)

# Ejemplo de uso
print("\nRecorrido en pre-orden (iterativo):")
recorrido_pre_orden_iterativo(raiz)