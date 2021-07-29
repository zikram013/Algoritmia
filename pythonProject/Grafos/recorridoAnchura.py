# Con esto importamos colas en python
from _collections import deque

# Defininimos el grafo con sus componentes conexas
#g = [[], [2, 4, 8], [1, 3, 4], [2, 4, 5], [1, 2, 3, 7], [3, 6], [5, 7], [4, 6, 9], [1, 9], [7, 8]]


# En orden g: 0 1 2 3 4 5 6 7 8 9
gruposRiesgo, relaciones = map(int, input().strip().split())
grafoVacunas = []
# Grafo dirigido

for i in range(gruposRiesgo):
    grafoVacunas.append([])

# Riesgo de contagio de U a V
for i in range(relaciones):
    grupoU, grupoV = map(int, input().strip().split())
    grafoVacunas[grupoU].append(grupoV)


def recorrido_anchura(g):
    n = len(g)
    dic=dict()
    visited = [False] * n
    for v in range(0, n-1):
        if not visited[v]:
            contador=0
            ra(g, visited, v,0)


def ra(g, visited, v):
    cola = deque()  # declaro la cola
    visited[v] = True  # marco el nodo como visitado
    print(v, end=" ")
    cola.append(v)  # Añado el nodo a la cola
    while len(cola) > 0:  # Mientras aun queden elementos en la cola
        aux = cola.popleft()  # Quita el primer elemento de la cola que se ha introducido
        for w in g[aux]:  # Nodos adyacentes en el elemento que hemos quitado
            if not visited[w]:  # Si no esta visitado
                visited[w] = True  # Lo marcamos como visitado
                print(w, end=" ")
                cola.append(w)  # Lo añadimos a la cola


recorrido_anchura(grafoVacunas)

# #Si en esta codigo cambiamos la cola por la pila, encolas por apilar, y desencolar por desapilar se convierte en
# iterativo
