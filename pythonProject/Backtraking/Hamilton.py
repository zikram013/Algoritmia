def test_graph():
    """
    (0)---(1)---(2)
      \  /  \  /
      (3)---(4)
    """
    v = 5
    edges = [(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
    graph = [[] for _ in range(v)]
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)
    return graph

def esFactible(nodo, sol, n):
    return nodo not in sol or (nodo == 0 and len(sol) == n)

def esSolucion(grafo, sol, nodo):
    return nodo == 0 and len(sol) == len(grafo) + 1
def hamiltonVA(g, nodo, solucion, soluciones):
    #if ini == 0 and len(solucion) == n + 1:
    if esSolucion(g, sol, nodo):
        #listsolucion.append(solucion)
        soluciones += 1
    else:
        for ady in g[nodo]:
            if esFactible(ady, solucion, len(g)):
                solucion.append(ady)
                soluciones = hamiltonVA(g,ady, solucion,soluciones)
                #deshacer:
                solucion.pop()
    return soluciones

grafo = test_graph()
ini=0
sol=[ini]
soluciones=hamiltonVA(grafo,ini,sol,0)
print(soluciones)