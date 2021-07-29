# numero de miembros de la familia
# miembro de la familia, paciencia,urgencia,tiempo
"""
5
Marco 4 3 2
Irene 10 2 3
Antonio 6 9 1
Claudia 2 7 4
Maria 9 8 2
sol:
Claudia
Antonio
Maria
Marco
Irene
4
"""
import copy
import sys

familiares = int(input())
listaFamiliares = list()
for i in range(familiares):
    nombre, paciencia, urgencia, tiempo = map(str, input().strip().split())
    diccionarioFamiliar = dict()
    diccionarioFamiliar['nombre'] = nombre
    diccionarioFamiliar['paciencia'] = int(paciencia)
    diccionarioFamiliar['urgencia'] = int(urgencia)
    diccionarioFamiliar['tiempo'] = int(tiempo)
    diccionarioFamiliar['p/u'] = int(paciencia) / int(urgencia)
    listaFamiliares.append(diccionarioFamiliar)

print(listaFamiliares)


def getMejorOpcion(candidatos, listaFamiliares):
    pyu = sys.maxsize
    for c in candidatos:
        baremo = listaFamiliares[c]['p/u']
        if baremo < pyu:
            pyu = baremo
            mejorOpcion = c
    return mejorOpcion


def dameTiempo(listaIndex, listaFamiliares):
    contar = 0
    contador = 1
    for i in listaIndex:
        contar += listaFamiliares[i]['tiempo']
    return contar


def vorazFamiliar(listaFamiliares):
    candidatos = set()
    sol = list()
    listaIndex = list()
    tiempo = 0
    listaTiempo = list()
    for i in range(len(listaFamiliares)):
        candidatos.add(i)
    while candidatos:
        mejorOpcion = getMejorOpcion(candidatos, listaFamiliares)
        sol.append(str(listaFamiliares[mejorOpcion]['nombre']))
        listaIndex.append(mejorOpcion)
        contador = dameTiempo(listaIndex, listaFamiliares)
        tiempo += contador + tiempo
        listaTiempo.append(tiempo)
        candidatos.remove(mejorOpcion)
    return sol, listaIndex, listaTiempo


sol, listaIndex, listaTiempo = vorazFamiliar(listaFamiliares)
print(sol)
print(listaTiempo)
print(listaIndex)
ordenados=sorted(sol)
print(ordenados)
for i in range(len(sol)-1):
    if sol[i]==ordenados[0]:
        print(listaTiempo[i-1])
