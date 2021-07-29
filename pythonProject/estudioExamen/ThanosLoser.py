"""
11 16
7 8
6 7
9 1
8 0
5 10
10 9
3 0
4 0
5 0
3 1
1 4
5 1
3 2
2 4
2 5
3 6
"""
planetas, conexiones = map(int, input().strip().split())
listaConex = list()
for i in range(planetas):
    listaConex.append([])

for i in range(conexiones):
    ini, end = map(int, input().strip().split())
    listaConex[ini].append(end)
    listaConex[end].append(ini)

nodoInicio = 0
recorrido = list()
recorrido.append(nodoInicio)
viajesPosibles = 0


def esSolucion(nodo, recorrido, listaConex):
    return nodo == 0 and len(recorrido) == len(listaConex) + 1


def factible(nodo, recorrido, listaConex):
    return nodo not in recorrido or (nodo == 0 and len(listaConex) == len(recorrido))


def hamilton(listaConex, nodoInicio, recorrido, viajesPosibles):
    if esSolucion(nodoInicio, recorrido, listaConex):
        viajesPosibles += 1
        #print(viajesPosibles)
    else:
        for ady in listaConex[nodoInicio]:
            if factible(ady, recorrido, listaConex):
                recorrido.append(ady)
                viajesPosibles = hamilton(listaConex, ady, recorrido, viajesPosibles)
                recorrido.pop()
    return viajesPosibles


viajesPosibles = hamilton(listaConex, nodoInicio, recorrido, viajesPosibles)
print(viajesPosibles)
