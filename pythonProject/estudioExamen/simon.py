"""
7 3
100 Murcia
200 Aragón
10 Cataluña
50 Andalucía
25 Cantabria
15 Madrid
55 Extremadura
10
48
99
"""
listaCam = list()
listaUmbral = list()
comu, umbral = map(int, input().strip().split())
for i in range(comu):
    camas, cam = map(str, input().strip().split())
    listaCam.append((int(camas), cam))

for i in range(umbral):
    umb = int(input())
    listaUmbral.append(umb)

listaCam.sort()


def bb(listaCam, ele, ini, fin):
    if ini > fin:
        return False
    mid = (ini + fin) // 2
    if listaCam[mid][0] == ele:
        return listaCam[mid][1]
    elif listaCam[mid -1][0] < ele < listaCam[mid][0]:
        return listaCam[mid][1]
    elif listaCam[mid][0] < ele:
        return bb(listaCam, ele, mid + 1, fin)
    else:
        return bb(listaCam, ele, ini, mid - 1)


def dyv(listaCam, ele):
    return bb(listaCam, ele, 0, len(listaCam) - 1)


for i in listaUmbral:
    ele = dyv(listaCam, i)
    print(ele)
