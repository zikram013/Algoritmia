from random import randint

supermercados,caminos = map(int, input().strip().split())

listaCarreteras = list()

for i in range(supermercados):
    listaCarreteras.append([])

for i in range(caminos):
    inicio, fin, distancia = map(int, input().strip().split())
    listaCarreteras[inicio].append((inicio, fin, distancia))
    listaCarreteras[fin].append((fin,inicio,distancia))

def recorrido(listaCarreteras):
    numeroDeSupermercados = list(range(len(listaCarreteras)))
    componentesSupermercados = len(listaCarreteras)
    minimaDistancia = 0
    listaDeSupermercadosRecorridos = []
    for superMasProximo in listaCarreteras:
        for superInicio, superFin, distancia in superMasProximo:
            if superInicio < superFin:
                listaDeSupermercadosRecorridos.append((distancia, superInicio, superFin))
    listaDeSupermercadosRecorridos.sort()
    i = 0
    while (len(listaDeSupermercadosRecorridos) > i) and (componentesSupermercados > 1):
        distancia, superInicio, superFin = listaDeSupermercadosRecorridos[i]
        if numeroDeSupermercados[superInicio] != numeroDeSupermercados[superFin]:
            minimaDistancia += distancia
            componentesSupermercados -= 1
            seleccionarSuper(numeroDeSupermercados, numeroDeSupermercados[superInicio], numeroDeSupermercados[superFin])
        i += 1
    return minimaDistancia


def seleccionarSuper(numeroDeSupermercados,viejoId,nuevoID):
    for i in range(len(numeroDeSupermercados)):
        if numeroDeSupermercados[i] == viejoId:
            numeroDeSupermercados[i] = nuevoID

sol=recorrido(listaCarreteras)
print(sol)
"""
4 5
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4


7 7
0 1 3
0 2 7
1 3 3
1 4 4
2 3 2
3 4 7
5 6 6
"""