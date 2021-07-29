dispositivos, conexiones, coste = map(int, input().strip().split())
grafoSistemas = {}

for i in range(conexiones):
    c1, c2 = map(int, input().strip().split())
    if c1 in grafoSistemas:
        grafoSistemas[c1] += [c2]
    else:
        grafoSistemas[c1] = [c2]

    if c2 in grafoSistemas:
        grafoSistemas[c2] += [c1]
    else:
        grafoSistemas[c2] = [c1]

#print(grafoSistemas)


# si el vertice tiene mas de una adyacencia es punto de articulacion
# Si el vertices no es raiz y alguno de sus hijo no tiene forma de llegar a los vertices superiores es
# punto de articulacion
def recorrido(grafoSistemas, coste):
    n = len(grafoSistemas)
    tiempo=0
    low={}
    disc={}
    listaPuntosArticulacion=[]
    #visitados = set()
    visisted = [False] * n
    for nodo in range(0, n):
        if len(grafoSistemas[nodo])>= 2:
            listaPuntosArticulacion.append(nodo)
        if not visisted[nodo]:
            articulacion(grafoSistemas, visisted, nodo,tiempo)
    coste=coste*len(listaPuntosArticulacion)
    print(coste)

def articulacion(grafoSistemas, visited, nodo,tiempo):
    visited[nodo] = True
    tiempo=tiempo+1
    #print(nodo, end=" ")
    for n in grafoSistemas[nodo]:
        if not visited[n]:
            articulacion(grafoSistemas, visited, n,tiempo)


recorrido(grafoSistemas, coste)

"""

def rp(grafoSistemas, visited, nodo, iteracionDescubrimiento, tiempo):
    visited[nodo] = True
    tiempo = tiempo + 1
    print(nodo, end=" ")  # imprimo los nodos visitados
    iteracionDescubrimiento[nodo] = tiempo
    for w in grafoSistemas[nodo]:
        if not visited[w]:
            rp(grafoSistemas, visited, w, iteracionDescubrimiento, tiempo)


recorrido(grafoSistemas, coste)

"""
