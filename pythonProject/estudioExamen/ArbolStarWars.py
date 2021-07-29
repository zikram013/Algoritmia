# N miembros de la familia
# Identificador e hijos
# M consultas
# contienen un entero cada unq ue identifaca al miebro del cual se quiere saber el nivel
# list(map(int, input().strip().split()))
"""
10
0 2
2 9
9 7
7 1 6 8
1 3 4
6
8
3
4 5
5
3
1
6
5
sol: 5 5 7
"""
from collections import deque

miembros = int(input())
listaFamiliar = list()
for i in range(miembros):
    listaFamiliar.append([])
for i in range(miembros):
    unionesFamiliares = list(map(int, input().strip().split()))
    # print(unionesFamiliares)
    # print(len(unionesFamiliares))
    for j in range(1, len(unionesFamiliares)):
        # print(unionesFamiliares[j])
        listaFamiliar[unionesFamiliares[0]].append(unionesFamiliares[j])

print(listaFamiliar)


def recorridoProfundidad(listaFamiliar):
    n = len(listaFamiliar)
    niveles = {}
    visitados = [False] * n
    for nodo in range(0,n):
        contador=0
        if not visitados[nodo]:
            rp(niveles,contador,listaFamiliar,nodo,visitados)
    return niveles


def rp(niveles, contador, listaFamiliar, ady, visitados):
    visitados[ady]=True
    contador=contador+1
    if contador in niveles:
        niveles[contador]+=[ady]
    else:
        niveles[contador]=[ady]
    for w in listaFamiliar[ady]:
        if not visitados[w]:
            rp(niveles,contador,listaFamiliar,w,visitados)


sol = recorridoProfundidad(listaFamiliar)

print(sol)
