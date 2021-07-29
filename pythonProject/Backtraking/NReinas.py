# 0 1 2 3 fila
# [1,0,3,2]
# -1 -1 -1 -1
# -1 -1 -1 -1
# -1 -1 -1 -1
# -1 -1 -1 -1

def inicializarSolucion(N):
    return [-1] * N


def esSolucion(sol, fila):
    return fila >= len(sol)


def esFactible(sol, fila, columna):
    factible = True
    i = 1
    while factible and i <= fila:
        factibleColumna = (sol[fila - i] != columna)
        factibleDiagonal1 = (sol[fila - i] != columna - i)
        factibleDiagonal2 = (sol[fila - i] != columna + i)
        factible = factibleColumna and factibleDiagonal1 and factibleDiagonal2
        i += 1

    return factible


def NReinasVA(sol, fila):
    if esSolucion(sol, fila):
        exito = True
    else:
        exito = False
        columna = 0
        while not exito and columna < len(sol):
            if esFactible(sol, fila, columna):
                sol[fila] = columna
                [sol, exito] = NReinasVA(sol, fila + 1)
                # Imprime reinas de forma factible
                if not exito:
                    sol[fila] = -1
            # else para soluciones no factibles
            columna += 1

    return sol, exito


reinas = 4  # Inicializar Datos
sol = inicializarSolucion(reinas)
fila = 0
[sol, exito] = NReinasVA(sol, fila)
print(sol)
if exito:
    print("sol")
else:
    print("sin solucion")
