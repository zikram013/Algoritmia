from random import randint


def test_mergesort():
    print("testing")
    for i in range(10000):
        input = []
        n = randint(1, 100)
        for j in range(n):
            input.append(randint(1, 100))
        copy = input[
               :]  # Copias el mismo array en otra posicion de memoria y accedes con copy. Si modificas input no afecta a copy
        mergeSort(input)
        copy.sort()
        assert copy == input
    print("done")


def mergeSort(elements):
    if len(elements) < 2:
        return
    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]
    mergeSort(left)
    mergeSort(right)
    merge(left, right, elements)


def merge(first, second, output):
    k = f = s = 0
    while f < len(first) and s < len(second):
        if first[f] <= second[s]:
            output[k] = first[f]
            f += 1
        else:
            output[k] = second[s]
            s += 1
        k += 1

    r = f if s == len(second) else s
    reminder = first if s == len(second) else second

    for i in range(r, len(reminder)):
        output[k] = reminder[i]
        k += 1


test_mergesort()
