def esSolucion(supers, x, y, productos, contadorProductos, fila, columna):
    if productos == contadorProductos and x == fila - 1 and y == columna - 1:
        return True
    else:
        return False


def esFactible(supers, x, y, fila, columna):
    if 0 <= x < fila and 0 <= y < columna:
        return supers[x][y] == 0 or supers[x][y] == 1
    else:
        return False


def recorridoSuper(supers, x, y, paso, productos, contadorProductos, fila, columna,totalPasos):
    if esSolucion(supers, x, y, contadorProductos, productos, fila, columna):
        if paso<totalPasos:
            totalPasos=paso
    else:
        exito = False
        mov = [[0, 1],
               [1, 0],
               [0, -1],
               [-1, 0]]
        i = 0
        while not exito and i < len(mov):
            if esFactible(supers, x + mov[i][0], y + mov[i][1], fila, columna):
                if supers[x + mov[i][0]][y + mov[i][1]] == 1:
                    contadorProductos += 1
                    supers[x + mov[i][0]][y + mov[i][1]] = paso
                    [supers, paso,totalPasos] = recorridoSuper(supers, x + mov[i][0], y + mov[i][1], paso + 1, productos,
                                                           contadorProductos, fila, columna,totalPasos)
                    if not exito:
                        supers[x + mov[i][0]][y + mov[i][1]] = 1
                        contadorProductos -= 1
                        paso -= 1

                elif supers[x + mov[i][0]][y + mov[i][1]] == 0:
                    supers[x + mov[i][0]][y + mov[i][1]] = paso
                    [supers, paso,totalPasos] = recorridoSuper(supers, x + mov[i][0], y + mov[i][1], paso + 1, productos,
                                                           contadorProductos, fila, columna,totalPasos)
                    if not exito:
                        supers[x + mov[i][0]][y + mov[i][1]] = 0
                        paso -= 1

            i += 1
    return supers, paso,totalPasos

def initSuper(fila,columna):
    supers=list()
    for i in range(fila):
        supers.append([0] * columna)

    for f in range(fila):
        pasillo = str(input())
        listPasillo = pasillo.split()
        listPasillo = list(map(int, listPasillo))
        for c in range(columna):
            supers[f][c] = int(listPasillo[c])
    return supers

fila, columna, productos = map(int, input().strip().split())
supers = initSuper(fila,columna)

iniX = 0
iniY = 0
paso = 100
supers[iniX][iniY] = paso
contadorProductos = 0
totalPasos=float('inf')
[supers, paso,totalPasos] = recorridoSuper(supers, iniX, iniY, paso + 1, productos, contadorProductos, fila, columna,totalPasos)
print(totalPasos-100)
