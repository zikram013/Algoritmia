import copy


def esFactible(sol, sillas, nodo):
    return nodo not in sol['listaInsercion'] or (nodo == 0 and len(sol['listaInsercion']) == len(sillas))


def esSolucion(sol, sillas, nodo):
    return nodo == 0 and len(sol['listaInsercion']) == len(sillas) + 1


def buscarDistMax(sol, sillas, nodo):
    cam = 0
    if sol['maxDistancia'] < sillas[nodo][2]:
        sol['maxDistancia'] = sillas[nodo][2]
    return cam


def caminoMaximo(sol, sillas, nodo, listaCandidatos, maxi, listaVaciaSolu,candidatos):
    if esSolucion(sol, sillas, nodo):
        if sol['maxDistancia'] > maxi:
            maxi = sol['maxDistancia']
            listaVaciaSolu = copy.deepcopy(sol['listaInsercion'])
        #print(maxi)
        #print(listaVaciaSolu)
    else:
        exito = False
        can=1
        for ini, end, dist in sillas[nodo]:
            if esFactible(sol, sillas, end):
                sol['listaInsercion'].append(end)
                #print(sol['listaInsercion'])
                # distmax=buscarDistMax(sol,sillas)
                sol['maxDistancia'] += dist
                #print(sol['maxDistancia'])
                [sol, maxi, listaVaciaSolu] = caminoMaximo(sol, sillas, end, listaCandidatos, maxi, listaVaciaSolu,candidatos)
                sol['listaInsercion'].pop()
                sol['maxDistancia'] -= dist
    return sol, maxi, listaVaciaSolu


def initDict():
    sol = dict()
    sol['listaInsercion'] = list()
    sol['distanciaMinima'] = float('inf')
    sol['maxDistancia'] = 0
    return sol



puestos, candidatos = map(int, input().strip().split())
puntos = puestos * (candidatos - 1)
sillas = list()
for i in range(puestos):
    sillas.append([])
for i in range(puntos):
    s1, s2, distancia = map(int, input().strip().split())
    sillas[s1].append((s1, s2, distancia))
    sillas[s2].append((s2, s1, distancia))

listaCandidatos = [-1] * candidatos
sol = initDict()
# sol['listaInsercion'] = [-1] * puestos
nodo = 0
maxi = 0
sol['listaInsercion'].append(nodo)
listaVaciaSolu = list()
[sol, maxi, listaVaciaSolu] = caminoMaximo(sol, sillas, nodo, listaCandidatos, maxi, listaVaciaSolu,candidatos)
print("tope",maxi)
print(listaVaciaSolu)

"""
5 3
0 1 266
0 2 298
0 3 702
0 4 489
1 2 564
1 3 822
1 4 755
2 3 859
2 4 191
3 4 668
"""
