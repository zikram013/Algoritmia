# Garantiza el optimo del arbol de recubrimiento
# Seleccionar la arista mas corta

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

g2 = [
    [],
    [(1,3,1), (1,4,2), (1,7,6)],
    [(2,5,2), (2,6,4), (2,7,7)],
    [(3,1,1), (3,4,3), (3,5,5)],
    [(4, 1, 2), (4, 3, 3), (4, 5, 1), (4, 6, 9)],
    [(5, 2, 2), (5, 4, 1), (5, 7, 8)],
    [(6, 2, 4), (6, 4, 9)],
    [(7, 1, 6), (7, 2, 7), (7, 3, 5), (7, 5, 8)],
]

def kruskal(g):
    componentes = list(range(len(g)))  # lista[0,1,2..7]
    count = len(g) - 1  # Numero de componentes conexas
    sumaAristas = 0  # Acumulamos la suma de las aristas que vamos eligiendo
    list_edges = []
    for ady in g:
        for inicio, fin, peso in ady:
            if inicio < fin:
                list_edges.append((peso,inicio, fin))
    list_edges.sort()
    i = 0
    while (len(list_edges) > i) and (count > 1):
        peso, inicio, fin = list_edges[i]
        if componentes[inicio] != componentes[fin]:
            sumaAristas += peso
            count -= 1
            actualizarComponentes(componentes, componentes[inicio], componentes[fin])
        i += 1
    return sumaAristas


def actualizarComponentes(componentes, viejo_id, nuevo_id):
    for c in range(len(componentes)):
        if componentes[c] == viejo_id:
            componentes[c] = nuevo_id


sol = kruskal(g)
print(sol)
