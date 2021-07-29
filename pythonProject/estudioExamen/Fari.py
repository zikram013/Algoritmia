# N numero de clientes
# C indican el numero de calles que los conectan
# cliente1 , cliente 2 y el coste
"""
10 19
0 4 517
0 9 600
1 7 105
1 8 956
2 4 231
2 8 250
2 9 182
3 4 569
3 8 352
4 5 868
4 7 578
4 9 116
5 6 785
5 7 563
5 9 492
6 9 609
7 8 217
7 9 161
8 9 880
sol=551
"""
clientes, calles = map(int, input().strip().split())
listaClientes = list()
for i in range(clientes):
    listaClientes.append([])
for i in range(calles):
    c1, c2, coste = map(int, input().strip().split())
    listaClientes[c1].append((c1, c2, coste))
    # listaClientes[c2].append((c2,c1,coste))


def actualizarComponente(componente, viejo, nuevo):
    tam = len(componente)
    for c in range(tam):
        if componente[c] == viejo:
            componente[c] = nuevo


def kruskal(listaClientes):
    componentes = list(range(len(listaClientes)))
    count = len(listaClientes)
    sumaCoste = 0
    listaNodos = []
    for ady in listaClientes:
        for inicio, fin, peso in ady:
            if inicio < fin:
                listaNodos.append((peso, inicio, fin))
    listaNodos.sort()
    i = 0
    while (len(listaNodos) > i) and (count > 1):
        peso, inicio, fin = listaNodos[i]
        if componentes[inicio] != componentes[fin]:
            sumaCoste += peso
            count -= 1
            actualizarComponente(componentes, componentes[inicio], componentes[fin])
        i += 1

    return sumaCoste


sol = kruskal(listaClientes)
if sol / 5 > sol // 5:
    print((sol // 5) + 1)
else:
    print(sol//5)
