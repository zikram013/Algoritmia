"""
7
1 2 3 4 5 6 7
3
3
10
2
"""
enemigosOleada = int(input())
nivelEnemigoOleada = list(map(int, input().strip().split()))
casosPrueba = int(input())
listaCasosPrueba = list()
for i in range(casosPrueba):
    caso = int(input())
    listaCasosPrueba.append(caso)
print(nivelEnemigoOleada)
print(listaCasosPrueba)


def bb(nivelEnemigoOleada, ele, ini, fin):
    if ini > fin:
        return ini
    mid = (ini + fin) // 2
    if nivelEnemigoOleada[mid] == ele:
        return mid+1
    elif ele < nivelEnemigoOleada[mid]:
        return bb(nivelEnemigoOleada, ele, ini, mid - 1)
    else:
        return bb(nivelEnemigoOleada, ele, mid + 1, fin)


def dyv(nivelEnemigoOleada, ele):
    return bb(nivelEnemigoOleada, ele, 0, len(nivelEnemigoOleada) - 1)


for i in listaCasosPrueba:
    sol = dyv(nivelEnemigoOleada, i)
    print(sol)
    contador = 0
    for i in range(sol):
        contador += nivelEnemigoOleada[i]

    print(sol, " ", contador)
