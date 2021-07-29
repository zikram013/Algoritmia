

universos, carreteras = map(int, input().strip().split())

listaCarreteras = list()

for i in range(universos):
    listaCarreteras.append([])

for i in range(carreteras):
    inicio, fin, enemigos = map(int, input().strip().split())
    listaCarreteras[inicio].append((inicio, fin, enemigos))



def recorrido(listaCarreteras,origen):
    visitados=[False]*len(listaCarreteras)
    visitados[origen]=True
    enemies=0
    minEnemies=[float('inf')]*len(listaCarreteras)
    recorridoMundos=list()
    recorridoMundos.append(origen)
    for inicio,fin,enemigos in listaCarreteras[origen]:
        minEnemies[fin]=enemies
    for i in range(1,len(listaCarreteras)):
        siguienteMundo,enemigos=seleccion(visitados,minEnemies)
        enemies+=enemigos
        recorridoMundos.append(siguienteMundo)
        if siguienteMundo!=None:
            visitados[siguienteMundo] = True
            for mundo in listaCarreteras[siguienteMundo]:
                inicio,fin,enemigos=mundo
                if not visitados[fin]:
                    minEnemies[fin]=min(minEnemies[fin] , enemigos)
        else:
            print(len(recorridoMundos))
            print(recorridoMundos)
            return enemies
    print(len(recorridoMundos))
    print(recorridoMundos)
    return enemies


def seleccion(visitados,minEnemies):
    siguienteMundo=None
    enemigos=float('inf')
    for i in range(len(minEnemies)):
        if not visitados[i] and minEnemies[i]<enemigos:
            siguienteMundo=i
            enemigos=minEnemies[i]

    return siguienteMundo,enemigos



sol = recorrido(listaCarreteras, 0)
print(sol)