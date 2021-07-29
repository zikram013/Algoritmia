"""
DyV: Ejercicio 2
Se pide encontrar la mediana de un grupo de elementos no ordenados
sin tener que ordenarlos. Vamos a considerar que la mediana sería
el elemento que ocuparía la posición (n+1)/2 si los elementos
estuvieran ordenados. [1]
Ordenar los elementos sería O(nlogn) si usamos un método de
ordenación eficiente. Si utilizamos DyV podemos tener un algoritmo
de coste O(n) EN PROMEDIO [2].
[1] Aquí nos referimos a su posición ordinal (1º, 2º, 3º, ...)
por lo que de 4 elementos su mediana sería el 2º y de 5 elementos
sería el tercero. Estos elementos se corresponden con el índice
(n-1)/2, empezando desde 0.
[2] El peor caso de este algoritmo es O(n^2), pero con
un buen pivote su complejidad sería lineal O(n).
</p>
"""
from random import randint


def median(elements):
    ordinal = (len(elements) + 1) // 2
    return kthSmallestElement(ordinal - 1, elements)


def kthSmallestElement(k, elements):
    """
    Returns the k-th smallest element from the given list.
    k=0 would be the smallest element, k=1 the second smallest,
    ..., k = n-1 the largest.
    :param k:
    :param elements:
    :return:
    """
    mid = len(elements) // 2
    pivot = elements[mid]

    smaller = [x for x in elements if x < pivot]
    # smaller = list(filter(lambda x: x < pivot, elements)) # equivalente
    if k < len(smaller):
        return kthSmallestElement(k, smaller)

    k -= len(smaller)
    equal = [x for x in elements if x == pivot]
    if k < len(equal):
        return equal[k]

    k -= len(equal)
    greater = [x for x in elements if x > pivot]
    return kthSmallestElement(k, greater)


def test():
    print("Testing... ", end="")
    for i in range(10000):
        n = randint(1, 100)
        a = [randint(0, 99) for i in range(n)]
        copy = a[:]
        copy.sort()
        # print("Sorted:", copy)
        m = median(a)
        expected = copy[(len(copy) - 1) // 2]
        # print("median:", median(a), "expected:", expected)
        assert m == expected
    print(" Done.")

test()