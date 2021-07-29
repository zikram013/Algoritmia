"""
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
"""
sudoku = [0] * 9
for x in range(9):
    sudoku[x] = list(map(int, input().strip().split()))


def esFactible(sudoku, fila, columna, num):
    facFila = True
    factColumna = True
    factSub = True
    for i in range(9):
        if sudoku[i][columna] == num:
            facFila = False
    for i in range(9):
        if sudoku[fila][columna] == num:
            factColumna = False
    fil = (fila // 3) * 3
    column = (columna // 3) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[fil + i][column + j] == num:
                factSub = False
    fact = not facFila and not factSub and not factColumna
    return fact


def resolverSudoku(sudoku, fila, columna):
    # Comprobamos que la casilla es distinta de 0 en todos los casos
    if sudoku[fila][columna] != 0:
        if fila == 8 and columna == 8:
            return True
        elif columna < 8:
            resolverSudoku(sudoku, fila, columna + 1)
        else:
            resolverSudoku(sudoku, fila + 1, columna)
    else:
        for i in range(1, 9, 1):
            if not esFactible(sudoku, fila, columna, i):
                sudoku[fila][columna] = i
                if fila == 8 and columna == 8:
                    return True
                elif columna < 8:
                    esSol = resolverSudoku(sudoku, fila, columna + 1)
                else:
                    esSol = resolverSudoku(sudoku, fila + 1, columna)
                if esSol:
                    return True
        sudoku[fila][columna] = 0
        return False


sol = resolverSudoku(sudoku, 0, 0)
if sol:
    for i in range(9):
        for j in range(9):
            print(sudoku[i][j], ' ', end='')
        print()
