from collections import deque
from copy import deepcopy
from queue import PriorityQueue

import numpy as np


def inicializarDatos():
    datos = np.array([[11, 12, 18, 40], [14, 15, 13, 22], [11, 17, 19, 23], [17, 14, 20, 28]])
    return datos


# sol['elems'] = [-1, -1, -1, -1]
def solVacia(datos):
    sol = {}
    sol['elems'] = [-1] * np.size(datos, 0)
    sol['coste'] = 0
    return sol


def solucionInicial(datos):
    sol = solVacia(datos)
    for i in range(len(sol['elems'])):
        sol['elems'][i] = i
        sol['coste'] += datos[i, i]
    return sol


def generarTuplaVacia(datos):
    tupla = {}
    tupla['elems'] = [-1] * np.size(datos, 0)
    tupla['tope'] = 0
    tupla['coste'] = 0
    tupla['cota'] = 0
    return tupla


def esta(tarea, tupla):
    return tarea in tupla['elems'][0:tupla['tope']]


def asignar(hijo, tarea, datos):
    hijo['elems'][hijo['tope']] = tarea
    hijo['coste'] += datos[hijo['tope'], tarea]
    hijo['tope'] += 1
    hijo['cota'] = hijo['coste']
    for i in range(hijo['tope'], np.size(datos, 0)):
        valorMin = np.inf
        for j in range(np.size(datos, 1)):
            if not esta(j, hijo) and datos[i, j] < valorMin:
                valorMin = datos[i, j]
        hijo['cota'] += valorMin
    return hijo


def buscaTareaRestante(hijo):
    encontrado = False
    i = -1
    while not encontrado and i < len(hijo['elems']):
        i += 1
        encontrado = i not in hijo['elems'][:hijo['tope']]
    return i


def compleccionesFactibles(tupla, datos):
    listaHijos = []
    for tarea in range(np.size(datos, 1)):
        hijo = deepcopy(tupla)
        if not esta(tarea, tupla):
            hijo = asignar(hijo, tarea, datos)
            if hijo['tope'] == len(hijo['elems']) - 1:
                tareaRestante = buscaTareaRestante(hijo)
                hijo = asignar(hijo, tareaRestante, datos)
            listaHijos.append(hijo)
    return listaHijos


def esSolucion(hijo):
    return hijo['tope'] == len(hijo['elems'])


def asigTareasRyP(datos):
    solMejor = solucionInicial(datos)
    tupla = generarTuplaVacia(datos)
    identificador = 0
    # q = deque()
    qp = PriorityQueue()
    # q.append(tupla)
    qp.put((tupla['cota'], identificador, tupla))
    identificador += 1
    while not qp.empty():
        (prioridad, identificador, tupla) = qp.get()
        if tupla['cota'] < solMejor['coste']:
            hijos = compleccionesFactibles(tupla, datos)
            for hijo in hijos:
                if esSolucion(hijo):
                    if hijo['coste'] < solMejor['coste']:
                        solMejor = hijo
                elif hijo['cota'] < solMejor['coste']:
                    qp.put((hijo['cota'], identificador, hijo))
                    identificador += 1

    return solMejor


# Prog Ppal:
datos = inicializarDatos()
sol = asigTareasRyP(datos)
print(sol)
