from random import randint
"""
g = [
    [],
    [(1, 3, 1), (1, 4, 2), (1, 7, 6)],
    [(2, 5, 2), (2, 6, 4), (2, 7, 7)],
    [(3, 1, 1), (3, 4, 3), (3, 7, 5)],
    [(4, 1, 2), (4, 3, 3), (4, 5, 1), (4, 6, 9)],
    [(5, 2, 2), (5, 4, 1), (5, 7, 8)],
    [(6, 2, 4), (6, 4, 9)],
    [(7, 1, 6), (7, 2, 7), (7, 3, 5), (7, 5, 8)]
]
"""
supermercados,caminos = map(int, input().strip().split())

listaCarreteras = list()

for i in range(supermercados):
    listaCarreteras.append([])

for i in range(caminos):
    inicio, fin, distancia = map(int, input().strip().split())
    listaCarreteras[inicio].append((inicio, fin, distancia))
    #listaCarreteras[fin].append((fin,inicio,distancia))


def prim(g):
    inicial = randint(0, len(g)-1)
    visitados = [False] * len(g)
    pesoMinimo = 0
    visitados[inicial] = True
    shortest_edges = [float('inf')] * len(g)  #
    for inicio, fin, peso in g[inicial]:  # ponemos todos a infinito primero y luego cogemos la posicion del end y le ponemos el peso correspondiente
        shortest_edges[fin] = peso
    for i in range(0, len(g)):
        next_nodo, peso = select_min(visitados, shortest_edges)
        pesoMinimo += peso
        visitados[next_nodo] = True
        for edge in g[next_nodo]:
            inicio, fin, peso = edge
            if not visitados[fin]:
                shortest_edges[fin] = min(shortest_edges[fin], peso)
    return pesoMinimo


def select_min(visitados, shortest_edges):
    next_nodo = None
    peso = float('inf')
    for i in range(0, len(shortest_edges)):
        if not visitados[i] and shortest_edges[i] < peso:
            next_nodo = i
            peso = shortest_edges[i]

    return next_nodo, peso


sol = prim(listaCarreteras)
print(sol)
