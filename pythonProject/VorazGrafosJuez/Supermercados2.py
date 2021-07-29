from random import randint

supermercados,caminos = map(int, input().strip().split())

listaCarreteras = list()

for i in range(supermercados):
    listaCarreteras.append([])

for i in range(caminos):
    inicio, fin, distancia = map(int, input().strip().split())
    listaCarreteras[inicio].append((inicio, fin, distancia))
    listaCarreteras[fin].append((fin,inicio,distancia))

def recorrido(listaCarreteras):
    inical=randint(0,len(listaCarreteras)-1)
    print("empezamos en el super",inical)
    visitados=[False]*len(listaCarreteras)
    distanciaMinima=0
    visitados[inical]=True
    caminoMasCorto=[float('inf')]*len(listaCarreteras)
    superRecorridos=list()
    superRecorridos.append(inical)
    for inicio,fin,distancia in listaCarreteras[inical]:
        caminoMasCorto[fin]=distancia
    for i in range(1,len(listaCarreteras)):
        siguienteSuper,distanciaAlSuper=seleccionarSuper(visitados,caminoMasCorto)
        distanciaMinima+=distanciaAlSuper
        print(distanciaMinima)
        superRecorridos.append(siguienteSuper)
        visitados[siguienteSuper]=True
        for super in listaCarreteras[siguienteSuper]:
            inicio,fin,distancia=super
            if not visitados[fin]:
                caminoMasCorto[fin]=min(caminoMasCorto[fin],distanciaAlSuper)
    print(superRecorridos)
    return distanciaMinima

def seleccionarSuper(visitados,caminoMasCorto):
    super=None
    dist=float('inf')
    for i in range(1,len(caminoMasCorto)):
        if not visitados[i] and caminoMasCorto[i]<dist:
            super=i
            dist=caminoMasCorto[i]
    return super,dist



sol=recorrido(listaCarreteras)
print(sol)

"""
4 5
0 1 10
0 2 6
0 3 5
1 3 15
2 3 4
"""