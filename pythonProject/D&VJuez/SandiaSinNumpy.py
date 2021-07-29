from collections import Counter

longitud, cortes = map(int, input().strip().split())
matriz = list()
for i in range(longitud):
    matriz.append([0] * longitud)

for f in range(longitud):
    pepitas = str(input())
    listaPepitas = pepitas.split()
    listaPepitas = list(map(int, listaPepitas))
    for c in range(longitud):
        matriz[f][c] = int(listaPepitas[c])
potencia = cortes


def sumarMatrices(matriz, potencia):
    s = 0
    #print(matriz)
    # print(matriz)
    if (len(matriz[0])) > 1:
        for fila in matriz:
            for elem in fila:
                s += elem
    else:
        s += matriz[0][0]
    return s


def dividirMatriz(matriz, cortes, sol, potencia):
    if cortes == 0:
        p = sumarMatrices(matriz, potencia)
        sol.append(p)
    else:#
        cortes -= 1
        listaCuadrantes = list()
        # listaPepitas = list()
        # p = sumarMatrices(matriz, potencia)
        # listaPepitas.append(p)
        # Primer Cuadrante
        primerCuadrante = [row[0:len(matriz) // 2] for row in matriz[0:len(matriz) // 2]]
        listaCuadrantes.append(primerCuadrante)
        # p = sumarMatrices(primerCuadrante, potencia)
        # listaPepitas.append(p)
        # SegundoCuadrante
        segundoCuadrante = [row[len(matriz) // 2:len(matriz)] for row in matriz[0:len(matriz) // 2]]
        listaCuadrantes.append(segundoCuadrante)
        # p = sumarMatrices(segundoCuadrante, potencia)
        # listaPepitas.append(p)
        # TercerCuadrante
        tercerCuadrante = [row[0:len(matriz) // 2] for row in matriz[len(matriz) // 2:]]
        listaCuadrantes.append(tercerCuadrante)
        #p = sumarMatrices(tercerCuadrante, potencia)
        # listaPepitas.append(p)
        # CuartoCuadrante
        cuartoCuadrante = [row[len(matriz) // 2:] for row in matriz[len(matriz) // 2:]]
        listaCuadrantes.append(cuartoCuadrante)
        # p = sumarMatrices(cuartoCuadrante, potencia)
        for i in listaCuadrantes:
            dividirMatriz(i, cortes, sol, potencia)
    return sol


sol = list()
nuggets = dividirMatriz(matriz, cortes, sol, potencia)
print(min(nuggets))

"""
primer cuadrante
primerCuadrante11 = [row[0:len(matriz) // 2] for row in matriz[0:len(matriz) // 2]]
print(primerCuadrante11)
"""
"""
segundo cuadrante
primerCuadrante12 = [row[len(matriz) // 2:len(matriz)] for row in matriz[0:len(matriz) // 2]]
print(primerCuadrante12)
"""

"""
cuarto
primerCuadrante22 = [row[len(matriz)//2:] for row in matriz[len(matriz) // 2:]]
print(primerCuadrante22)
"""
"""
tercer cuadrante
primerCuadrante21 = [row[0:len(matriz)//2] for row in matriz[len(matriz)//2:]]
print(primerCuadrante21)
"""
