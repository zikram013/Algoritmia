universos, carreteras = map(int, input().strip().split())

listaCarreteras = list()

for i in range(universos):
    listaCarreteras.append([])

for i in range(carreteras):
    inicio, fin, enemigos = map(int, input().strip().split())
    listaCarreteras[inicio].append((inicio, fin, enemigos))


def recorrido(listaCarreteras,origen):
    numeroDeUniversos=list(range(len(listaCarreteras)))
    componentesUniversos=len(listaCarreteras)
    enemies=0
    listaDeMundosRecorridos=[]
    for mundoMasProximo in listaCarreteras:
        for mundoInicio,mundoFin,enemigos in mundoMasProximo:
            if mundoInicio<mundoFin:
                listaDeMundosRecorridos.append((enemigos,mundoInicio,mundoFin))
    listaDeMundosRecorridos.sort()
    i=0
    while(len(listaDeMundosRecorridos)>i)and (componentesUniversos>1):
        enemigos,inicio,fin=listaDeMundosRecorridos[i]
        if numeroDeUniversos[inicio]!=numeroDeUniversos[fin]:
            enemies+=enemigos
            componentesUniversos -=1
            actualizarUniversos(numeroDeUniversos,numeroDeUniversos[inicio],numeroDeUniversos[fin])
        i+=1
    return enemies


def actualizarUniversos(numeroDeUniversos,viejoId,nuevoID):
    for i in range(len(numeroDeUniversos)):
        if numeroDeUniversos[i]==viejoId:
            numeroDeUniversos[i]=nuevoID


sol = recorrido(listaCarreteras, 0)
print(sol//5)