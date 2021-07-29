"""
9 14
0 1 4
0 7 8
1 2 8
1 7 11
2 3 7
2 5 4
2 8 2
3 4 9
3 5 14
4 5 10
5 6 2
6 7 1
6 8 6
7 8 7
0 4
"""
nCerv, conexiones = map(int, input().strip().split())
listaCerveza = list()
for i in range(nCerv):
    listaCerveza.append([])

for i in range(conexiones):
    c1, c2, distancia = map(int, input().strip().split())
    listaCerveza[c1].append((c1, c2, distancia))
    listaCerveza[c2].append((c2, c1, distancia))

origen, destino = map(int, input().strip().split())


def siguienteNodo(visitados, distancias):
    maximo = float('inf')
    indice = -1
    for c in range(1, len(distancias)):
        di = distancias[c]
        if not visitados[c] and di < maximo:
            maximo = di
            indice = c

    return indice


def distra(listaCerveza, origen):
    visitados = [False] * len(listaCerveza)
    distancias = [float('inf')] * len(listaCerveza)
    visitados[origen] = True
    listaNodoVisitados = list()
    listaNodoVisitados.append(origen)
    distancias[origen] = 0
    for ini, fin, dis in listaCerveza[origen]:
        distancias[fin] = dis

    for i in range(1, len(listaCerveza)):
        # ini, fin, peso = distancias[i]
        nodonext = siguienteNodo(visitados, distancias)
        visitados[nodonext] = True
        listaNodoVisitados.append(nodonext)
        for ini, fin, dis in listaCerveza[nodonext]:
                distancias[fin] = min(distancias[fin], distancias[ini] + dis)
    return distancias, listaNodoVisitados


distancia, bebidas = distra(listaCerveza, origen)
print(distancia, bebidas)
print(distancia[destino])
cadena = str()
for i in bebidas:
    print(i, end=" ")
