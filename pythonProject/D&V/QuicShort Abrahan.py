
from random import randint


def partition(elements, start, end):
    pivot = elements[start]
    i = start + 1 # mi código i es left
    j = end # mi código j es right
    while i <= j:
        if elements[i] <= pivot:
            i += 1
        elif elements[j] > pivot:
            j -= 1
        else:
            elements[i], elements[j] = elements[j], elements[i]
            i += 1
            j -= 1
    elements[start], elements[j] = elements[j], elements[start]
    return j


#start -> i
#end -> j
#pivot -> posición en la que se almacenará el pivotte
def quicksort_rec(start, end, elements):
    if start >= end:
        return
    #elements = [9,4,17,21,34,6,0-5,56,14,8,43]
    #partition
    #       -> pivote = 9
    # reordena[6,4,8,-5,0, 9,34,21,56,14,17,43]
    #devuelve -> 6
    pos_pivot = partition(elements, start, end)
    quicksort_rec(start, pos_pivot - 1, elements)
    quicksort_rec(pos_pivot + 1, end, elements)

def quicksort(elements):
    quicksort_rec(0, len(elements) - 1, elements)

def test_quickSort():

    print("Testing ...", end = "")
    for i in range(10000):
        input = []
        n = randint(1, 100)
        for j in range(n):
            input.append(randint(1, 100))
        copy = input[:]
        quicksort(input)
        copy.sort()
        assert copy == input
    print("Done")

test_quickSort()

