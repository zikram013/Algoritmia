g = [
    [],
    [(1, 2, 5), (1, 4, 3)],
    [(2, 5, 1)],
    [],
    [(4, 2, 1), (4, 3, 11), (4, 5, 6)],
    [(5, 3, 1)]
]
"""
cables, conexiones = map(int, input().strip().split())
diccionarioTipoConexion = dict()
conexionesCableadas = list()

tipoComponente = str(input())
tipoComponenteModifcado = tipoComponente.replace(" ", "")

for i in range(cables):
    diccionarioTipoConexion[int(i)] = tipoComponenteModifcado[int(i)]

for i in range(cables):
    conexionesCableadas.append([])

for i in range(conexiones):
    inicio, fin, longitud = map(int, input().strip().split())
    conexionesCableadas[inicio].append((inicio, fin, longitud))
    conexionesCableadas[fin].append((fin, inicio, longitud))
"""


def distra(g, origin):
    distance = [float('inf')] * len(g)
    visitados = [False] * len(g)
    distance[origin] = 0
    visitados[origin] = True

    for inicio, fin, peso in g[origin]:
        distance[fin] = peso
    for i in range(1, len(g)):
        nextNodo = select_min(distance, visitados)
        visitados[nextNodo] = True
        for inicio, fin, peso in g[nextNodo]:
            distance[fin] = min(distance[fin], distance[inicio] + peso)

    print(origin, " ", distance)
    #lp = BestLong(distance, tipoConex, origin)
    return distance


def BestLong(tam, tipoConex, origen):
    l = float('inf')
    for i in range(0, len(tam) - 1):
        if tipoConex[origen] == tipoConex[i]:
            if tam[i] < l and tam[i] != 0:
                l = tam[i]
    return l


def select_min(distance, visitados):
    minDistancia = float('inf')
    index = 0
    for i in range(1, len(distance)):
        if not visitados[i] and distance[i] < minDistancia:
            minDistancia = distance[i]
            index = i
    return index


listSol = []
sol = distra(g, 1)
print(sol)
"""
for i in range(0, len(conexionesCableadas) - 1):
    sol = distra(conexionesCableadas, i, diccionarioTipoConexion)
    listSol.append(sol)
"""
