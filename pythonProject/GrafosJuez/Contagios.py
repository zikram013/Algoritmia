from collections import deque

personas, numeroRelaciones = map(int, input().strip().split())
grafo = []

for i in range(personas):
    grafo.append([])
for i in range(numeroRelaciones):
    n, d = map(int, input().strip().split())
    grafo[n].append(d)  # Solo si es dirigido
    # grafo[d].append(n)  # Con ambas si es dirigido


def recorrido_profundidad(grafo):
    contador = 0
    resultado = "NO"
    listaCaminosTodosContagios = []
    visitas = len(grafo)
    visited = [False] * visitas
    for nodo in range(0, visitas):
        if not visited[nodo]:
            rp(grafo, visited, nodo)
            # print(visited)
            # for i in visited:
            #   if i:
            #      contador = contador + 1
            # print(contador)
            #print(visited)
            if visited.count(True) == len(visited):
                listaCaminosTodosContagios.append(True)
                visited = [False] * visitas
            else:
                listaCaminosTodosContagios.append(False)
                visited = [False] * visitas
    #print(listaCaminosTodosContagios)
    if listaCaminosTodosContagios.count(False) >= 1:
        print("NO")
    else:
        print("SI")


"""
def rp(grafo, visited, nodo):
    visited[nodo] = True
    print(nodo,end="")
    for w in grafo[nodo]:
        if not visited[w]:
            rp(grafo, visited, w)
"""


def rp(g, visited, v):
    cola = deque()
    visited[v] = True
   # print(v, end=" ")
    cola.append(v)
    while len(cola) > 0:
        aux = cola.popleft()
        for w in g[aux]:
            if not visited[w]:
                visited[w] = True
                #print(w, end=" ")
                cola.append(w)

recorrido_profundidad(grafo)
"""
5 8
0 4
1 0
1 2
2 1
2 4
3 1 
3 2
4 3

5 7
0 4
1 0
1 2
2 1
2 4
3 1
3 2




5 5
0 4
1 0
2 3
1 3
2 1
"""
