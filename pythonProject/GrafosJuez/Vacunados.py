from _collections import deque

"""
9 8
0 1
1 6
2 3
2 4
5 4
6 7
8 7
8 3

"""

"""
gruposRiesgo, relaciones = map(int, input().strip().split())
grafoVacunas = []
# Grafo dirigido

for i in range(gruposRiesgo):
    grafoVacunas.append([])

# Riesgo de contagio de U a V
for i in range(relaciones):
    grupoU, grupoV = map(int, input().strip().split())
    grafoVacunas[grupoU].append(grupoV)
"""

miembros = int(input())
listaFamiliar = list()
for i in range(miembros):
    listaFamiliar.append([])
for i in range(miembros):
    unionesFamiliares = list(map(int, input().strip().split()))
    # print(unionesFamiliares)
    # print(len(unionesFamiliares))
    for j in range(1, len(unionesFamiliares)):
        # print(unionesFamiliares[j])
        listaFamiliar[unionesFamiliares[0]].append(unionesFamiliares[j])

print(listaFamiliar)



# Primero se vacunan los que tienen adyacentes y no son adyancentes de otros

# print(grafoVacunas)
def recorrido_profundidad_vacunas(grafoVacunas):
    niveles = {}
    visitados = set()
    n = len(grafoVacunas)
    visited = [False] * n
    listaAlmacenNoPrimeros = []
    for nodo in range(0, n):
        contador = 0
        if not nodo in visitados:
            ra(grafoVacunas, visitados, nodo, contador, niveles)
    print(niveles)
    pintarResultado(niveles)


def ra(grafoVacunas, visitados, nodo, contador, niveles):
    visitados.add(nodo)
    contador = contador + 1
    if contador in niveles:
        niveles[contador] += [nodo]
    else:
        niveles[contador] = [nodo]
    # print(nodo, end=" ")
    for w in grafoVacunas[nodo]:
        if w not in visitados:
            ra(grafoVacunas, visitados, w, contador, niveles)


def pintarResultado(niveles):
    for clave in niveles:
        ordenados = sorted(niveles[clave])
        # cadena=" ".join(map(str,niveles[clave]))
        cadena = " ".join(map(str, ordenados))
        # print(niveles[clave], end="\n")
        print(cadena)


recorrido_profundidad_vacunas(listaFamiliar)

"""def ra(grafoVacunas, visitados, nodo):
    cola = deque()
    visitados.add(nodo)
    print(nodo, end="\n")
    cola.append(nodo)
    while len(cola) > 0:
        aux = cola.popleft()
        for w in grafoVacunas[aux]:  #
                if not w in visitados:
                    visitados.add(w)
                    print(w, end=" ")
                    cola.append(w)"""
