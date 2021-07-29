"""
10 15
7 8 12
6 7 92
1 9 22
8 0 11
9 4 89
3 0 76
4 0 10
5 0 79
3 1 36
1 4 95
5 1 65
3 2 73
2 4 36
2 5 29
5 6 32
"""
ciudades, conexiones = map(int, input().strip().split())
listaCiudades = list()
for i in range(ciudades):
    listaCiudades.append([])

for i in range(conexiones):
    ini, fin, peso = map(int, input().strip().split())
    listaCiudades[ini].append((ini, fin, peso))

total = 0


def profrec(listaCiudades, nodo, distan, maximaDistancia):
    global total
    proximaDistancia = 0
    if len(listaCiudades[nodo]) > 0:
        for i in listaCiudades[nodo]:
            distancia = i[2] + distan
            if maximaDistancia < distancia:
                maximaDistancia = distancia
            proximaDistancia = profrec(listaCiudades, i[1], distancia, maximaDistancia)
            if total < maximaDistancia:
                total = maximaDistancia
    return proximaDistancia


def prof(listaCiudades):
    maximaDistancia = 0
    for i in listaCiudades:
        for j in i:
            distancia = j[2]
            profrec(listaCiudades, j[1], distancia, maximaDistancia)
    print(total)


prof(listaCiudades)
"""
# print(listaCiudades)
listSoluciones = list()


def RP(listaCiudades, nodoInicio):
    listaVisitados = list()
    listaVisitados.append(nodoInicio)
    contador = 0
    maxDist=0
    dist = rec(listaCiudades, nodoInicio, listaVisitados, contador,maxDist)
    return dist


def rec(listaCiudades, nodoInicio, listaVisitados, contador,maxDist):
    maxio = 0
    ciudadFin = 0
    if len(listaCiudades[nodoInicio]) > 0:
        for i in listaCiudades[nodoInicio]:
            if maxio < i[2] and i[1] not in listaVisitados:
                maxio = i[2]
                ciudadFin = i[1]
                dist=maxio+
                if 
        listaVisitados.append(ciudadFin)
        contador += maxio
        maxio = rec(listaCiudades, ciudadFin, listaVisitados, contador,maxDist)
    return contador


for i in range(ciudades):
    sol = RP(listaCiudades, i)
    listSoluciones.append(sol)

print(listSoluciones)
"""
