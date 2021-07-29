"""
3 3
A 0
B 1
C 0
A B 5
A C 10
C B 8
C B



7 7
A 0
B 1
C 0
D 5
E 2
F 3
G 5
B G 5
G D 10
D E 8
F E 3
A C 1
B A 1
C F 1
B F


"""

lugares, caminos = map(int, input().strip().split())
dictLugares = dict()
dictLugares['l'] = []
dictLugares['feromonas'] = []
for i in range(lugares):
    l, feromona = map(str, input().strip().split())
    dictLugares['l'].append(l)
    dictLugares['feromonas'].append(int(feromona))

listaCaminos = list()
for i in range(caminos):
    listaCaminos.append([])
for i in range(caminos):
    ini, fin, distancia = map(str, input().strip().split())
    if dictLugares['feromonas'][dictLugares['l'].index(fin)] > 0:
        listaCaminos[dictLugares['l'].index(ini)].append(((dictLugares['l'].index(ini)), (dictLugares['l'].index(fin)), int(distancia)))
    if dictLugares['feromonas'][dictLugares['l'].index(ini)] > 0:
        listaCaminos[dictLugares['l'].index(fin)].append( ((dictLugares['l'].index(fin)), (dictLugares['l'].index(ini)), int(distancia)))
# listaCaminos[dictLugares['l'].index(fin)].append(((dictLugares['l'].index(fin)), (dictLugares['l'].index(ini)), int(distancia)))

origen, destino = map(str, input().strip().split())
origenNumerico = dictLugares['l'].index(origen)
destinoNumerico = dictLugares['l'].index(destino)


# Si el valor del punto es 0 no pueden llegar

def nexColonia(distance, visitados):
    mini = float('inf')
    ind = 0
    for i in range(1, len(distance)):
        if not visitados[i] and distance[i] < mini:
            mini = distance[i]
            ind = i
    return ind


def distra(origen, destino, listaCaminos):
    distance = [float('inf')] * len(listaCaminos)
    visitados = [False] * len(listaCaminos)
    visitados[origen] = True
    distance[origen] = 0
    for ini, fin, peso in listaCaminos[origen]:
        distance[fin] = peso
    for i in range(1, len(listaCaminos)):
        proxColonia = nexColonia(distance, visitados)
        visitados[proxColonia] = True
        for inicio, fin, peso in listaCaminos[proxColonia]:
            distance[fin] = min(distance[fin], distance[inicio] + peso)
        """
                else:
            for inicio, fin, peso in listaCaminos[proxColonia]:
                distance[fin] = min(distance[fin], distance[inicio] + peso)
            break
        """

    return distance


sol = distra(origenNumerico, destinoNumerico, listaCaminos)

print(dictLugares)
print(listaCaminos)
print(origenNumerico, " ", destinoNumerico)

print(sol[destinoNumerico])
