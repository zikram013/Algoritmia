"""
10
11 22 30 35 49 54 68 74 75 97
5
16 97 81 9 76
"""
levels = int(input())
listaLevels = list()
niveles = list(map(int, input().strip().split()))
for i in niveles:
    listaLevels.append(i)

player = int(input())
listaPlayer = list()
jugadores = list(map(int, input().strip().split()))
for i in jugadores:
    listaPlayer.append(i)


def bb(listaLevels, ele, ini, fin):
    if ini > fin:
        return False, False
    mid = (ini + fin) // 2
    if mid == 1 and listaLevels[mid] > ele:
        return 'X', listaLevels[mid]
    elif mid==1 and ele<listaLevels[mid]:
        return listaLevels[mid-1],'X'
    elif listaLevels[mid] == ele:
        return listaLevels[mid - 1], listaLevels[mid + 1]
    elif listaLevels[mid - 1] < ele < listaLevels[mid]:
        return listaLevels[mid - 1], listaLevels[mid]
    elif listaLevels[mid] < ele < listaLevels[mid + 1]:
        return listaLevels[mid], listaLevels[mid + 1]
    elif ele < listaLevels[mid]:
        return bb(listaLevels, ele, mid - 1, listaLevels)
    else:
        return bb(listaLevels, ele, ini, mid - 1)


def dyv(listaLevels, ele):
    return bb(listaLevels, ele, 0, len(listaLevels) - 1)


for i in listaPlayer:
    ant, sig = dyv(listaLevels, i)
    print(ant, sig)
