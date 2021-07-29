# Busqueda binaria, requiere un array ordenado
v = [1, 3, 3, 3, 3, 7, 9]


def rec_bs(e, low, high,
           elements):  # Caso recursivo es cuando low and high se cruzan por lo cual cuando llegue ese momento debemos parar
    if low > high:
        return -low - 1  # Equivale a devolver falso
    mid = (low + high) // 2
    if elements[mid] == e:
        return mid
    elif e < elements[mid]:
        return rec_bs(e, low, mid - 1, elements)
    else:
        return rec_bs(e, mid + 1, high, elements)


def rec_binarySearch(e, elements):
    return rec_bs(e, 0, len(elements) - 1, elements)


index = rec_binarySearch(3, v)
if index < 0:
    print("no existe")
else:
    print(index)
