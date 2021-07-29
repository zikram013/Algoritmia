# N representa los componentes
# M representa las conexiones
# Las siguientes n lineas enteros que indican el tipo al que pertenece cada componente
# Las siguientes M lineeas contienen 3 enteros c,d conexion y l longitud
"""
6 10
0 0 0 1 1 1
0 1 2
0 3 1
0 2 5
1 2 3
1 3 2
2 3 3
2 4 1
2 5 5
3 4 1
4 5 1
"""
import collections

cables, conexiones = map(int, input().strip().split())
diccionarioTipoConexion = dict()
conexionesCableadas = list()

tipoComponente = str(input())
tipoComponenteModifcado = tipoComponente.replace(" ", "")

for i in range(cables):
    diccionarioTipoConexion[int(i)] = tipoComponenteModifcado[int(i)]

for i in range(cables):
    conexionesCableadas.append([])

for i in range(conexiones):
    inicio, fin, longitud = map(int, input().strip().split())
    conexionesCableadas[inicio].append((inicio, fin, longitud))
    conexionesCableadas[fin].append((fin, inicio, longitud))


def BoomOfDistra(conexionesCableadas, origen, tipoConex):
    solutionsInDict = {}
    tam = [float('inf')] * len(conexionesCableadas)
    visitados = [False] * len(conexionesCableadas)
    visitados[origen] = True
    tam[origen] = 0

    for inicio, fin, peso in conexionesCableadas[origen]:
        tam[fin] = peso
    for i in range(0, len(conexionesCableadas)):
        sigCable = lonMin(tam, visitados)
        visitados[sigCable] = True
        for inicio, fin, peso in conexionesCableadas[sigCable]:
            tam[fin] = min(tam[fin], tam[inicio] + peso)

    lp = BestLong(tam, tipoConex,origen)
    return lp

def BestLong(tam,tipoConex,origen):
    l = float('inf')
    for i in range(0,len(tam)-1):
        if tipoConex[origen] == tipoConex[i]:
            if tam[i] < l and tam[i] != 0:
                l = tam[i]
    return l

def lonMin(tam, visitados):
    mini = float('inf')
    ind = 0
    for i in range(1, len(tam)):
        if not visitados[i] and tam[i] < mini:
            mini = tam[i]
            ind = i
    return ind


c=float('inf')
listSol = {}

for i in range(0, len(conexionesCableadas)):
    sol = BoomOfDistra(conexionesCableadas, i, diccionarioTipoConexion)
    if diccionarioTipoConexion[i]not in listSol:
        listSol[diccionarioTipoConexion[i]]=sol
    else:
        if listSol[diccionarioTipoConexion[i]]>sol:
            listSol[diccionarioTipoConexion[i]]=sol
listSol2=dict(sorted(listSol.items()))
for clave in listSol2:
    v=listSol2[clave]
    print(v,end=" ")


