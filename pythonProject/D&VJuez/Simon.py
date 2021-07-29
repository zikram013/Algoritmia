"""
7 3
100 Murcia
200 Aragón
10 Cataluña
50 Andalucía
25 Cantabria
15 Madrid
55 Extremadura
10
48
99

cambiar todo a listas
"""
import operator

comunidades, solicita = map(int, input().strip().split())
DCA = {}
listFases = []
listCamas = []
tupla=list()

for i in range(comunidades):
    camas, CA = map(str, input().strip().split())
    DCA[CA] = int(camas)
    listCamas.append(int(camas))
    tupla.append((int(camas),CA))

for i in range(solicita):
    fase = int(input())
    listFases.append(fase)
listCamas.sort()

tupla.sort()
#print(tupla)
#print(len(tupla))
listaOrdenadaCA = sorted(DCA.items(), key=operator.itemgetter(1), reverse=False)



def DYV(umbral, start, end, listaCamas):
    if start > end:
        if start == 0:
            return listaCamas[start][1]
        elif start == len(listaCamas):
            return listaCamas[start - 1][1]
        else:
            return listaCamas[start][1]
    mid = (start + end) // 2
    if listaCamas[mid][0] == umbral:
        if mid != len(listaCamas) - 1:
            return listaCamas[mid][1]
        else:
            return listaCamas[mid-1][1]

    elif umbral < listaCamas[mid][0]:
        return DYV(umbral, start, mid - 1, listaCamas)
    else:
        return DYV(umbral, mid + 1, end, listaCamas)


def BB(listaCamas, umbral):
    return DYV(umbral, 0, len(listaCamas) - 1, listaCamas)


for i in listFases:
    sol = BB(tupla, i)
    print(sol, end="\n")

#sol=BB(tupla,10)
#print(sol)

"""
dyv:
    if start>end:
        true
    if listCamas[]>umbral and listaCamas>[-1/+1]> umbral:
        dyv(umbral,lista,mid+1,end)
    if listaCamas[]<umbral and listCamas[-1/+1]umbral:
        dyv(umbral,lista,start,mid-1)
    if listaCamas[]>umbral and listCamas[-1/+1]<umbral or listaCamas[]==umbral:
        return listaCamas[-1] listaCAmas[+1]

"""

"""
def dyv(CA, i):
    aux = 0
    cam = ""
    for valor in CA:
        if CA[valor] == i:
            return valor
        else:
            if CA[valor] > i and (aux-i) < i-CA[valor]:
                cam = valor
                aux = CA[valor]
            else:
                aux=CA[valor]

    return cam
"""

"""
def dyv(camas, umbral):
    for i in camas:
        if i == umbral:
            return i
            break
        elif i > umbral:
            return i
            break


def obtenerkey(DCA, valor):
    return [clave for clave, val in DCA.items() if val == valor]
"""

"""
    if start > end:
        if start == 0:
            return listaCamas[start][0]
        elif start == len(listaCamas):
            return listaCamas[start - 1][0]
            
                elif start==0:
        return listaCamas[start][0]
"""
