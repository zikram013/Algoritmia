# Con esto importamos colas en python
from _collections import deque

# Defininimos el grafo con sus componentes conexas
pilotes, parDePilotes = map(int, input().strip().split())
grafoPilotes = []

for i in range(pilotes):
    grafoPilotes.append([])

for i in range(parDePilotes):
    p1, p2 = map(int, input().strip().split())  # Pilotes sin una patata en medio
    grafoPilotes[p1].append(p2)
    grafoPilotes[p2].append(p1)


# En orden g: 0 1 2 3 4 5 6 7 8 9

def recorrido_anchura(g):
    n = len(g)
    visited = [False] * n
    cucharadas = 0
    for v in range(1, n):
        if not visited[v]:
            cucharadas = cucharadas + 1
            ra(g, visited, v)
    return cucharadas


def ra(g, visited, v):
    pila = []  # declaro la pila
    visited[v] = True  # marco el nodo como visitado
    print(v, end=" ")
    pila.append(v)  # Añado el nodo a la pila
    while len(pila) > 0:  # Mientras aun queden elementos en la pila
        aux = pila.pop(0)  # Quita el primer elemento de la pila que se ha introducido
        for w in g[aux]:  # Nodos adyacentes en el elemento que hemos quitado
            if not visited[w]:  # Si no esta visitado
                visited[w] = True  # Lo marcamos como visitado
                print(w, end=" ")
                pila.append(w)  # Lo añadimos a la pila


print(recorrido_anchura(grafoPilotes))

# #Si en esta codigo cambiamos la cola por la pila, encolas por apilar, y desencolar por desapilar se convierte en
# iterativo
# 1 2 4 8 3 7 9 5 6
