tam = int(input())
lista = list(map(int, input().strip().split()))


def merge(izq, der, lista):
    i = d = k = 0
    while i < len(izq) and d < (len(der)):
        if izq[i] <= der[d]:
            lista[k] = izq[i]
            i += 1
        else:
            lista[k] = der[d]
            d += 1
        k += 1
    r = i if d == len(der) else d
    re = izq if d == len(der) else der

    for i in range(r, len(re)):
        lista[k] = re[i]
        k += 1


def mergesort(lista):
    if len(lista) == 1:
        return lista
    mid = len(lista) // 2
    izq = lista[:mid]
    der = lista[mid:]
    mergesort(izq)
    mergesort(der)
    merge(izq, der, lista)
    return lista


sol = mergesort(lista)
print(sol)


def metodoPivote(lista, ini, fin):
    pivot = lista[ini]
    i = ini + 1
    j = fin
    while i <= j:
        if lista[i] <= pivot:
            i += 1
        elif lista[j] > pivot:
            j -= 1
        else:
            lista[i], lista[j] = lista[j], lista[i]
            i += 1
            j -= 1
    lista[ini], lista[j] = lista[j], lista[ini]
    return j


def metodointermedio(lista, ini, fin):
    if ini > fin:
        return False
    else:
        pivote = metodoPivote(lista, ini, fin)
        metodointermedio(lista, ini, pivote - 1)
        metodointermedio(lista, pivote + 1, fin)


def quickSort(lista):
    orden = metodointermedio(lista, 0, len(lista) - 1)
    print(orden)

solQs = quickSort(lista)
print(solQs)
