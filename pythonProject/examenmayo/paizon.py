"""
5 7
def 0
if 1
not 2
else 3
end 4
def if
def else
if not
if else
if end
not end
else end
def
"""

pr, conex = map(int, input().strip().split())
listaPalabrasResevadas = dict()
listaPalabrasResevadas['palabra'] = []
listaPalabrasResevadas['indice'] = []
for i in range(pr):
    p, id = map(str, input().strip().split())
    listaPalabrasResevadas['palabra'].append(p)
    listaPalabrasResevadas['indice'].append(id)

listaConex = list()
for i in range(pr):
    listaConex.append([])

for i in range(conex):
    ini, fin = map(str, input().strip().split())
    listaConex[listaPalabrasResevadas['palabra'].index(ini)].append(listaPalabrasResevadas['palabra'].index(fin))
    listaConex[listaPalabrasResevadas['palabra'].index(fin)].append(listaPalabrasResevadas['palabra'].index(ini))

#print(listaConex)

inic = str(input())
og = listaPalabrasResevadas['palabra'].index(inic)
listasol = list()
soluciones = 0
listasol.append(og)


def esSolucion(listaConex, listaSol, nodo):
    return len(listaConex) + 1 == len(listaSol)


def esFactible(listaSol, listaConex, nodo):
    return nodo not in listaSol or (nodo == 0 and len(listaConex) == len(listaSol))


def hamilton(listaSol, og, listaConex, soluciones):
    if esSolucion(listaConex, listaSol, og):
        soluciones += 1
    else:
        exito = False
        for ady in listaConex[og]:
            if esFactible(listaSol, listaConex, ady):
                listaSol.append(ady)
                #print(listasol)
                soluciones = hamilton(listaSol, ady,listaConex, soluciones)
                listaSol.pop()
    return soluciones


soluciones = hamilton(listasol, og, listaConex, soluciones)
if soluciones == 0:
    print("EPIC FAIl")
else:
    print("EASY BRO")
