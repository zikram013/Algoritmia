"""
10
11 22 30 35 49 54 68 74 75 97
5
16 97 81 9 76
"""
import time
numeroNiveles = int(input())
niveles = str(input())
listaNivel = niveles.split()
listaNivel = list(map(int, listaNivel))
numeroJugadores = int(input())
nivelJugadores = str(input())
listaJugadores = nivelJugadores.split()
listaJugadores = list(map(int, listaJugadores))


def GOWRecursivo(levelPlayer, start, end, listaNivel):
    if start > end:
        if start == 0:
            return "X " + str(listaNivel[start])
        elif start == len(listaNivel):
            return str(listaNivel[start-1]) + " X"
        else:
            return str(listaNivel[start - 1]) + " " + str(listaNivel[start])
    mid = (start + end) // 2
    if listaNivel[mid] == levelPlayer:
        if mid == len(listaNivel) - 1:
            return str(listaNivel[mid - 1]) + " X"
        else:
            return str(listaNivel[mid - 1]) + " " + str(listaNivel[mid + 1])
    elif levelPlayer < listaNivel[mid]:
        return GOWRecursivo(levelPlayer, start, mid - 1, listaNivel)
    else:
        return GOWRecursivo(levelPlayer, mid + 1, end, listaNivel)


def GOW(listaNivel, levelPlayer):
    return GOWRecursivo(levelPlayer, 0, len(listaNivel) - 1, listaNivel)

#inicio=time.time()
for i in listaJugadores:
    menorYmayor = GOW(listaNivel, i)
    print(menorYmayor)
#fin=time.time()
