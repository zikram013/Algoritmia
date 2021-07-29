# Fila,Columna,Regalos
# Regalos+1 Pared
# Vale 0- puede pasar
# Vale entre >1<regalos el orden de recogida
# if sorted(lst)==lst
"""
5 6 4
0 1 0 5 0 0
0 2 0 5 4 0
0 5 0 5 0 0
0 3 5 0 5 0
0 0 0 0 0 0
"""


def initGymkana(fila, columna):
    gymkana = list()
    for i in range(fila):
        gymkana.append([0] * columna)

    for f in range(fila):
        pasillo = str(input())
        listPasillo = pasillo.split()
        listPasillo = list(map(int, listPasillo))
        for c in range(columna):
            gymkana[f][c] = int(listPasillo[c])
    return gymkana


def esFactible(gymkana, x, y, fila, columna, regalos, listaRegalos):
    if 0 <= x < fila and 0 <= y < columna:
        # print("elemento ultimo lista ", listaRegalos[-1])
        return gymkana[x][y] == 0 or gymkana[x][y] == listaRegalos[-1] + 1
    else:
        return False


def esSolucion(gymkana, x, y, listaRegalos, fila, columna, regalos):
    return len(listaRegalos) == regalos + 1


def recorridoGym(gymkana, x, y, paso, listaRegalos, totalPasos, fila, columna, regalos, listapasos, guardaPasos):
    if esSolucion(gymkana, x, y, listaRegalos, fila, columna, regalos):
       # print("entro ",listaRegalos, " ",paso)
        listapasos.append(paso)
    else:
        exito = False
        mov = [
            [0, 1],
            [1, 0],
            [0, -1],
            [-1, 0]]
        i = 0
        while not exito and i < len(mov):
            if esFactible(gymkana, x + mov[i][0], y + mov[i][1], fila, columna, regalos, listaRegalos):
                #                   fila 0 + 0   col 0 + 1
                aux = gymkana[x + mov[i][0]][y + mov[i][1]]
                if 1 <= aux <= regalos:
                    guardaPasos[aux] = paso
                    listaRegalos.append(aux)
                    #print(listaRegalos)
                    # print(paso)
                gymkana[x + mov[i][0]][y + mov[i][1]] = paso
                [totalPasos, paso, listapasos] = recorridoGym(gymkana, x + mov[i][0], y + mov[i][1], paso + 1,
                                                              listaRegalos,
                                                              totalPasos, fila,
                                                              columna, regalos, listapasos, guardaPasos)
                if not exito:
                    gymkana[x + mov[i][0]][y + mov[i][1]] = aux
                    if len(listaRegalos) > 1 < regalos + 1 and guardaPasos.get(aux) and aux!=0:
                        listaRegalos.pop()
                        guardaPasos.pop(aux)
                    elif len(listaRegalos) == regalos + 1 and aux!=0:
                        listaRegalos.pop()
                        guardaPasos.pop(regalos)
                    paso -= 1
            i += 1

    return totalPasos, paso, listapasos


fila, columna, regalos = map(int, input().strip().split())
gymkana = initGymkana(fila, columna)
iniX = 0
iniY = 0
paso = 100
gymkana[iniX][iniY] = paso
listaRegalos = [0]
listapasos = list()
totalPasos = float('inf')
guardaPasos = dict()
[totalPasos, paso, listapasos] = recorridoGym(gymkana, iniX, iniY, paso + 1, listaRegalos, totalPasos, fila, columna,
                                              regalos, listapasos, guardaPasos)
print(min(listapasos)-100)
"""
gymkana[x + mov[i][0]][y + mov[i][1]] = aux
                    if len(listaRegalos) > 1 < regalos + 1:
                        listaRegalos.pop()
                        guardaPasos.pop(aux)
                    elif len(listaRegalos) == regalos + 1:
                        listaRegalos.pop()
                        guardaPasos.pop(regalos)
                    paso -= 1
"""