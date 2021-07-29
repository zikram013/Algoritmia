nHabitaciones, puertas, tiempo = map(int, input().strip().split())
listgp = list()
for i in range(nHabitaciones):
    listgp.append([])
for i in range(puertas):
    ini, fin, peso = map(int, input().strip().split())
    listgp[ini].append((ini, fin, peso))
    listgp[fin].append((fin, ini, peso))


def seleccionarPuerta(distancia, visitados):
    l = float('inf')
    pos = 0
    for i in range(1, len(distancia)):
        if not visitados[i] and distancia[i] < l:
            l = distancia[i]
            pos = i
    return pos


def distra(listagp, nodoInicio):
    visitados = [False] * len(listagp)
    distancia = [float('inf')] * len(listagp)
    distancia[nodoInicio] = 0
    visitados[nodoInicio] = True
    for ini, fin, peso in listagp[nodoInicio]:
        distancia[fin] = peso
    for i in range(2, len(listagp)):
        nextPuerta = seleccionarPuerta(distancia, visitados)
        visitados[nextPuerta] = True
        for inicio, fin, peso in listagp[nextPuerta]:
            distancia[fin] = min(distancia[fin], distancia[inicio] + peso)
    print(distancia)
    return distancia


print(listgp)
sol = distra(listgp, 0)
print(sum(sol))
