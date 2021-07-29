# i apunta a menor que pivote para que este bien
# j apunta a mayores que el pivote para que este bien
# solo si se cumplen estas condiciones se intercambian la posiciones
# cuando el elemento al que apunta a la j es menor al que apunta a la i tras cruzarse se cambia la j con el pivote
from random import randint


def test_quickshort():
    print("testing")
    for i in range(10000):
        input = []
        n = randint(1, 100)
        for j in range(n):
            input.append(randint(1,100))
        copy=input[:] #Copias el mismo array en otra posicion de memoria y accedes con copy. Si modificas input no afecta a copy
        quickSort(input)
        copy.sort()
        assert copy == input
    print("done")


def quickSort(elements):
    quickSort_recursivo(0,len(elements)-1, elements) #0 marca la posicion de inicio, la posicion del final, y el array a ordenar

def partition(elements,start,end):
    pivot = elements[start]
    i = start + 1
    j = end
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

def quickSort_recursivo(start,end,elements):
    #Start es la i
    #End es la j
    #Pivote es la posicion en la que se almacena el pivote
    if start >= end:
        return
    else:
        pivote=partition(elements,start,end)
        quickSort_recursivo(start,pivote-1,elements)
        quickSort_recursivo(pivote+1,end,elements)


test_quickshort()