# N P dimensiones
# P1 P2 y el movimiento hacia adelante y hacia un lado
# X y lugar de inicio

def crearTablero(n, m):
    tablero = list()
    for i in range(n):
        tablero.append([0] * n)
    for i in range(n):
        for j in range(m):
            tablero[i][j] = 0
    return tablero


def esSolucion(n, m, paso):
    return n * m == paso


def esFactible(tablero, fila, columna):
    if 0 <= fila < len(tablero) and 0 <= columna < len(tablero):
        return tablero[fila][columna] == 0
    else:
        return False


def laberinto(tablero, x, y, paso, delante, lado, n, m,mov):
    #print(paso)
    if n * m == paso:
        exito = True
    else:
        exito = False

        i = 0
        while not exito and i < len(mov):
            if esFactible(tablero, x + mov[i][0], y + mov[i][1]):
                tablero[x + mov[i][0]][y + mov[i][1]] = paso
                [tablero, exito] = laberinto(tablero, x + mov[i][0], y + mov[i][1], paso + 1, delante, lado, n, m,mov)
                if not exito:
                    tablero[x + mov[i][0]][y + mov[i][1]] = 0
            i += 1

    return tablero, exito


datosLaberintoYmovs = str(input())
listaDatos = datosLaberintoYmovs.split()
listaDatos = list(map(int, listaDatos))
for i in range(len(listaDatos)):
    if i == 0:
        n = listaDatos[i]
    elif i == 1:
        m = listaDatos[i]
    elif i == 2:
        haciaDelante = int(listaDatos[i])
    elif i == 3:
        haciaUnLado = int(listaDatos[i])

iniX, iniY = map(int, input().strip().split())
tablero = crearTablero(n, m)
paso = 1
tablero[iniX][iniY] = paso
mov = [[haciaDelante, haciaUnLado],
       [haciaDelante, -haciaUnLado],
       [-haciaDelante, haciaUnLado],
       [-haciaDelante, -haciaUnLado],
       [haciaUnLado, haciaDelante],
       [haciaUnLado, -haciaDelante],
       [-haciaUnLado, haciaDelante],
       [-haciaUnLado, -haciaDelante]]
[tablero, exito] = laberinto(tablero, iniX, iniY, paso, haciaDelante, haciaUnLado, n, m,mov)
if exito:
    print("PASALACABRA")
else:
    print("NADA")
