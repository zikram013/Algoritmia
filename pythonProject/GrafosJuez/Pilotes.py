from _collections import deque

pilotes, parDePilotes = map(int, input().strip().split())
grafoPilotes = {}

for i in range(parDePilotes):
    p1, p2 = map(int, input().strip().split())
    if p1 in grafoPilotes:
        grafoPilotes[p1] += [p2]
    else:
        grafoPilotes[p1] = [p2]

    if p2 in grafoPilotes:
        grafoPilotes[p2] += [p1]
    else:
        grafoPilotes[p2] = [p1]


def recorrido_pilote(grafoPilotes):
    nodos = grafoPilotes.keys()
    recorrido = []
    visitados = set()
    cucharadas = 0
    for nodo in nodos:
        if not nodo in visitados:
            cucharadas=cucharadas+1
            recorrido_pilotes(recorrido, visitados, nodo, grafoPilotes)
    cucharadas += pilotes - len(recorrido)
    print(cucharadas)

def recorrido_pilotes(recorrido, visitados, nodo, grafoPilotes):
    cola = deque()
    visitados.add(nodo)
    cola.extend(grafoPilotes[nodo])
    recorrido.append(nodo)
    while len(cola) > 0:
        desapilado = cola.popleft()
        if not desapilado in visitados:
            visitados.add(desapilado)
            cola.extend(grafoPilotes[desapilado])
            recorrido.append(desapilado)


recorrido_pilote(grafoPilotes)
