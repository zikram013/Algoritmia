def test_graph():
    """
    (0)---(1)---(2)
      \  /  \  /
      (3)---(4)
    """
    v = 5
    edges = [(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 4), (3, 4)]
    graph = [[] for _ in range(v)]
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)
    return graph


def esFactible(nodo, sol, n):
    return nodo not in sol or (nodo == 0 and len(sol) == n)


def esSolucion(grafo, sol, nodo):
    return nodo == 0 and len(sol) == len(grafo) + 1


def hamiltonVA(g, nodo, sol, soluciones):
    if esSolucion(g, sol, nodo):
        soluciones += 1
    else:
        for ady in g[nodo]:
            if esFactible(ady, sol, len(g)):
                sol.append(ady)
                soluciones = hamiltonVA(g, ady, sol, soluciones)
                # deshacer:
                sol.pop()
    return soluciones


grafo = test_graph()
ini = 0
sol = [ini]
soluciones = hamiltonVA(grafo, ini, sol, 0)
print(soluciones)
