def inicializarGrafo():
    # Lo vamos a representar como lista de adyacencia:
    grafo = {}
    grafo['n'] = 4
    grafo['adyacencia'] = [[1, 2, 3], [0], [0, 3], [0, 2]]
    return grafo


def inicializarSolucion(grafo):
    sol = [-1] * grafo['n']
    return sol


def esSolucion(nodo, grafo):
    return nodo >= grafo['n']


def esFactible(grafo, sol, nodo, color):
    factible = True
    ady = grafo['adyacencia'][nodo]
    i = 0
    while factible and i < len(ady):
        if ady[i] < nodo:
            factible = color != sol[ady[i]]
        i += 1
    return factible


def coloreadoVA(grafo, m, sol, nodo):
    if esSolucion(nodo, grafo):
        print(sol)
        # en caso de que sean todas las soluciones se deben poner aqui en vez de parar
        exito = True
    else:
        exito = False
        color = 1
        while not exito and color <= m:
            if esFactible(grafo, sol, nodo, color):
                sol[nodo] = color
                [sol, exito] = coloreadoVA(grafo, m, sol, nodo + 1)
                if not exito:
                    sol[nodo] = -1
            color += 1
    return sol, exito


grafo = inicializarGrafo()
sol = inicializarSolucion(grafo)
print(grafo)
m = 3  # numero de colores diferentes
nodo = 0  # primer nodo a colorear
[sol, exito] = coloreadoVA(grafo, m, sol, nodo)
print(sol)
