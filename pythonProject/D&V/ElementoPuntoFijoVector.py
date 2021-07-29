"""
Se pide desarrollar un método que encuentre (si existe)
un elemento que sea un punto fijo en el vector. El punto
fijo será un elemento cuyo valor sea igual al del índice
en el que se encuentra

Precondiciones:
- El vector está ordenado
- No hay elementos repetidos
"""

# Busqueda binaria, requiere un array ordenado
v = [-3, -2, -1, 0, 1, 5]


def findIndexRec(start, end, elements):
    if start > end:
        return -1
    else:
        mid = (start + end) // 2
        if mid == elements[mid]:
            return mid
        elif elements[mid] < mid:
            return findIndexRec(mid + 1, end, elements)
        else:
            return findIndexRec(start, mid - 1, elements)


def findIndexPoint(v):
    return findIndexRec(0, len(v) - 1, v)


index = findIndexPoint(v)
print(index)
