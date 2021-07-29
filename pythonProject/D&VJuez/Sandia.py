"""
8 2
0 0 0 1 1 1 0 0
1 0 1 0 0 0 1 0
0 0 1 0 1 0 0 0
0 1 0 0 0 1 0 1
1 1 0 0 1 0 1 1
0 1 0 1 0 0 1 0
0 0 1 0 1 0 1 0
0 0 0 1 0 0 1 0
"""
"""
8 1
0 0 0 1 1 1 0 0
1 0 1 0 0 0 1 0
0 0 1 0 1 0 0 0
0 1 0 0 0 1 0 1
1 1 0 0 1 0 1 1
0 1 0 1 0 0 1 0
0 0 1 0 1 0 1 0
0 0 0 1 0 0 1 0
"""
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

print(matriz)
primerCuadrante = [row[0:len(matriz) // 2] for row in matriz[0:len(matriz) // 2]]
print(primerCuadrante)