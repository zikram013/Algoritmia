personas, numeroRelaciones = map(int, input().strip().split())
grafo = []

for i in range(personas):
    grafo.append([])
for i in range(numeroRelaciones):
    n, d = map(int, input().strip().split())
    grafo[n].append(d)




def recorrido_profundidad(grafo):
    n = len(grafo)
    visited = [False] * n
    recorridoPorNodo = {}
    for nodo in range(0, n):
        if not visited[nodo]:
            recorridoPorNodo[nodo] = [nodo]
            print(recorridoPorNodo[nodo])
            entrada = recorridoPorNodo.get(nodo)
            str(entrada)
            rp(grafo, visited, nodo, recorridoPorNodo, entrada)
        visited = [False] * n
    print(recorridoPorNodo)


def rp(grafo, visited, nodo, recorridoPorNodo, entrada):
    visited[nodo] = True
    listaRecorrido = []
    int(entrada)
    for w in grafo[nodo]:
        if not visited[w]:
            # recorridoPorNodo[nodo] += [w]
            listaRecorrido.append(w)
            recorridoPorNodo[entrada] += [w]
            rp(grafo, visited, w, recorridoPorNodo, entrada)
    #recorridoPorNodo[entrada] += [listaRecorrido]


recorrido_profundidad(grafo)
