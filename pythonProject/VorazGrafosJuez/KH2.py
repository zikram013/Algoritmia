universos, carreteras = map(int, input().strip().split())

listaCarreteras = list()

for i in range(universos):
    listaCarreteras.append([])

for i in range(carreteras):
    inicio, fin, enemigos = map(int, input().strip().split())
    listaCarreteras[inicio].append((inicio, fin, enemigos))



def recorrido(listaCarreteras, origen):
    minEnemies = [float('inf')] * len(listaCarreteras)
    visitados = [False] * len(listaCarreteras)
    minEnemies[origen] = 0
    visitados[origen] = True

    for inicio, fin, enemigos in listaCarreteras[origen]:
        minEnemies[fin] = enemigos
    for i in range(1, len(listaCarreteras)):
        siguienteMundo = minimoEnemigos(minEnemies, visitados)
        visitados[siguienteMundo] = True
        for inicio, fin, enemigos in listaCarreteras[siguienteMundo]:
            minEnemies[fin] = min(minEnemies[fin], minEnemies[inicio] + enemigos)

    return minEnemies


def minimoEnemigos(minEnemies, visitados):
    minEnemy = float('inf')
    index = 0
    for i in range(1, len(minEnemies)):
        if not visitados[i] and minEnemies[i] < minEnemy:
            minEnemy = minEnemies[i]
            index = i
    return index



sol = recorrido(listaCarreteras, 0)
print(sol)