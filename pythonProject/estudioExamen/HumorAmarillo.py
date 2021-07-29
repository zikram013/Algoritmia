"""
4 6
0 0 0 0 2 0
0 -1 -1 -1 0 0
0 0 0 0 0 0
0 -1 0 0 0 0

5 5
0 -1 2 0 0
0 -1 0 0 0
0 0 0 0 0
0 -1 0 0 0
0 -1 0 0 0
"""
filas, columnas = map(int, input().strip().split())
lab = list()
for i in range(filas):
    lab.append([0] * columnas)
for i in range(filas):
    casillas = list(map(int, input().strip().split()))
    for j in range(columnas):
        lab[i][j] = casillas[j]


def esSolucion(lab, fila, columna,aux):
    return aux == 2


def esFactible(lab, fila, columna, paso):
    if 0 <= fila < len(lab) and 0 <= columna < len(lab[0]):
        if paso % 2 == 0:
            return lab[fila][columna] == 0 or lab[fila][columna] == 2
        else:
            return lab[fila][columna] == 0 or lab[fila][columna] == -1 or lab[fila][columna] == 2


def recorrer(lab, fila, columna, paso, totalPasos, p, aux):
    if esSolucion(lab, fila, columna, aux):
        p.append(paso)
        totalPasos = paso
    else:
        exito = False
        mov = [[0, 1],
               [1, 0],
               [0, -1],
               [-1, 0]]
        i = 0
        while not exito and i < len(mov):
            if esFactible(lab, fila + mov[i][0], columna + mov[i][1], paso):
                aux = lab[fila + mov[i][0]][columna + mov[i][1]]
                lab[fila + mov[i][0]][columna + mov[i][1]] = paso
                [lab, totalPasos, paso, p] = recorrer(lab, fila + mov[i][0], columna + mov[i][1], paso + 1, totalPasos,
                                                      p, aux)
                if not exito:
                    lab[fila + mov[i][0]][columna + mov[i][1]] = aux
                    paso -= 1
            i += 1
    return lab, totalPasos, paso, p


aux = 0
iniX = 0
iniY = 0
paso = 100
lab[iniX][iniY] = paso
totalPasos = 0
p = list()
[lab, totalPasos, paso, p] = recorrer(lab, iniX, iniY, paso + 1, totalPasos, p, aux)

print(min(p)-101)
