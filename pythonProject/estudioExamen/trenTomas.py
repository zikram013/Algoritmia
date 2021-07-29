"""
2
5 3
1
1
2
3
3
10 4
1
1
1
1
2
2
3
3
3
4
"""


def BB(listaVagones, vagonAnalizar, ini, fin):
    if ini > fin:
        return False
    mid = (ini + fin) // 2
    if listaVagones[mid] == vagonAnalizar and listaVagones[mid - 1] != vagonAnalizar:
        return mid
    elif listaVagones[mid] < vagonAnalizar:
        return BB(listaVagones, vagonAnalizar, mid+1, fin)
    else:
        return BB(listaVagones, vagonAnalizar, ini, mid-1)


def dyv(listaVagones, vagonAnalizar):
    posicionElement = BB(listaVagones, vagonAnalizar, 0, len(listaVagones) - 1)
    restPosition = listaVagones.count(vagonAnalizar) -1 + posicionElement
    print(posicionElement,restPosition)


casosPrueba = int(input())
for i in range(casosPrueba):
    vagones, vagonAnalizar = map(int, input().strip().split())
    listaVagones = list()
    for j in range(vagones):
        vagon = int(input())
        listaVagones.append(vagon)
    if listaVagones.sort() == listaVagones:
        dyv(listaVagones, vagonAnalizar)
    else:
        listaVagones.sort()
        dyv(listaVagones, vagonAnalizar)
