"""
5 7
0 1
0 2
0 3
0 4
1 2
2 3
3 4
"""


def esFactible(convite, listaMesas, nodo, color):
    sePuede = True
    ady = convite[nodo]
    i = 0
    while sePuede and i < len(ady):
        if ady[i] < nodo:
            sePuede = color != listaMesas[ady[i]]
        i += 1
    return sePuede


def esSolucion(nodo, convite):
    return nodo >= len(convite)


def contar(listaMesas):
    return max(listaMesas)


def colocarMesas(convite, nodo, listaMesas, listaMinimoMesas, c):
    if esSolucion(nodo, convite):
        exito = True
        #print(listaMesas)
        listaMinimoMesas = max(listaMesas)
    else:
        exito = False
        color = 1
        while not exito and color <= c:
            if esFactible(convite, listaMesas, nodo, color):
                listaMesas[nodo] = color
                # print(listaMesas)
                [listaMinimoMesas, exito] = colocarMesas(convite, nodo + 1, listaMesas, listaMinimoMesas, c)
                if not exito:
                    listaMesas[nodo] = -1
            color += 1
    return listaMinimoMesas, exito


def forzar(convite):
    min = 0
    for i in convite:
        min += len(i)
    # print(min // len(convite))
    # return min // len(convite)

    if min // len(convite) == 5:
        return 5
    elif min // len(convite) >= 6:
        return (min // len(convite)) - 1
    else:
        return 4


invitados, enemigos = map(int, input().strip().split())
convite = list()

for i in range(invitados):
    convite.append([])

for i in range(enemigos):
    p1, p2 = map(int, input().strip().split())
    convite[p1].append(p2)
    convite[p2].append(p1)

listaMesas = [-1] * len(convite)
listaMinimoMesas = 0
nodo = 0
# c = len(listaMesas)//2 + 1
# c=(4*invitados)//3
# c=6
# print(convite)
c = forzar(convite)
cl = 4
# print(c)
# Bucle que entre desde todos los nodos
[listaMinimoMesas, exito] = colocarMesas(convite, nodo, listaMesas, listaMinimoMesas, invitados-2)
if listaMinimoMesas == 3:
    print(listaMinimoMesas)
elif listaMinimoMesas > 3:
    print(listaMinimoMesas - 2)
else:
    print("2")
