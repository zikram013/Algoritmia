import numpy as np


def inicializarLaberinto():
    laberinto = np.zeros([10, 10])
    paredes = np.array(
        [[0, 2], [0, 7], [1, 0], [1, 2], [1, 5], [1, 6], [1, 8], [2, 6], [2, 8], [3, 1], [3, 4], [3, 5], [3, 6], [4, 2],
         [4, 3], [4, 7], [5, 5], [5, 7], [6, 0], [6, 3], [6, 4], [6, 7], [6, 9], [7, 1], [7, 2], [7, 8], [7, 9], [8, 2],
         [8, 4], [8, 5]])
    laberinto[paredes[:, 0], paredes[:, 1]] = np.inf
    return laberinto


def esSolucion(lab, fila, columna):
    return (fila == np.size(lab, 0) - 1) and (columna == np.size(lab, 1) - 1)


def esFactible(lab, fila, columna):
    return 0 <= fila < np.size(lab, 0) and 0 <= columna < np.size(lab, 1) and lab[fila][columna] == 0


def laberintoVueltaAtras(lab, fila, columna, paso):
    if esSolucion(lab, fila, columna):
        exito = True
    else:
        exito = False
        mov = np.array([[0, 1], [1, 0], [0, -1], [-1, 0]])
        i = 0
        while not exito and i < np.size(mov, 0):
            if esFactible(lab, fila + mov[i, 0], columna + mov[i, 1]):
                lab[fila + mov[i, 0], columna + mov[i, 1]] = paso
                [lab, exito] = laberintoVueltaAtras(lab, fila + mov[i, 0], columna + mov[i, 1], paso + 1)
                if not exito:
                    lab[fila + mov[i, 0], columna + mov[i, 1]] = 0
            i += 1
    return lab, exito


lab = inicializarLaberinto()
Xini = 0
Yini = 0
paso = 1
lab[Xini, Yini] = paso
[lab, exito] = laberintoVueltaAtras(lab, Xini, Yini, paso + 1)
print(lab)
