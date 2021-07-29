# Defininimos el grafo con sus componentes conexas
g = [[], [2, 4, 8], [1, 3, 4], [2, 4, 5], [1, 2, 3, 7], [3, 6], [5, 7], [4, 6, 9], [1, 9], [7, 8]]


# G de 0 es una lista vacia para que no haya lista vacia

# En orden g: 0 1 2 3 4 5 6 7 8 9

def recorrido_profundidad(g):
    n = len(g)  # Listas de conexiones de cada nodo
    visited = [False] * n  # Los ponemos todos a false
    for v in range(1, n):  # recorremos los nodos
        if not visited[v]:  # si esos nodos no estan visitados lo mandamos a marcar
            rp(g, visited, v)


def rp(g, visited, v):
    visited[v] = True
    print(v, end=" ")  # imprimo los nodos visitados
    for w in g[v]:
        if not visited[w]:
            rp(g, visited, w)




recorrido_profundidad(g)
