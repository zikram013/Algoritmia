# n=numero de habilidades disponibles
# m=puntos de habilidad que puede gastar
# numero habildad,ventaja y su coste
"""
5 1265
659 954 658
761 476 96
24 397 899
748 284 448
344 937 430
sol=2367
"""

"""

def getMejorHabilidad(diccionarioHabilidades, candidatos, maximo):
    aGastar = float('inf')
    for c in candidatos:
        ph = diccionarioHabilidades['Coste'][c]
        if ph < aGastar <= maximo:
            aGastar = ph
            mejorOpcion = c
    print(c)
    return c


def vorazSora(diccionarioHabilidades):
    diccionarioSolucion = {}
    diccionarioSolucion['maxVentaja'] = 0
    diccionarioSolucion['Habilidades'] = []
    maximo = diccionarioHabilidades['Tope']
    candidatos = set()
    for i in range(len(diccionarioHabilidades['Ventaja'])):
        candidatos.add(i)
    while candidatos and maximo >= 0:
        mejorHabilidad = getMejorHabilidad(diccionarioHabilidades, candidatos, maximo)
        diccionarioSolucion['Habilidades'].append(mejorHabilidad)
        diccionarioSolucion['maxVentaja'] += diccionarioHabilidades['Ventaja'][mejorHabilidad]
        maximo -= diccionarioHabilidades['Coste'][mejorHabilidad]
        candidatos.remove(mejorHabilidad)
    return diccionarioSolucion


diccionarioSolucion = vorazSora(diccionarioHabilidades)
print(diccionarioSolucion['Habilidades'])
print(diccionarioSolucion['maxVentaja'])
"""
import copy

habilidades, ph = map(int, input().strip().split())
diccionarioHabilidades = {}
diccionarioHabilidades['NumeroHabilidad'] = []
diccionarioHabilidades['Ventaja'] = []
diccionarioHabilidades['Coste'] = []
diccionarioHabilidades['Tope'] = ph

for i in range(habilidades):
    numero, ventaja, coste = map(int, input().strip().split())
    diccionarioHabilidades['NumeroHabilidad'].append(numero)
    diccionarioHabilidades['Ventaja'].append(ventaja)
    diccionarioHabilidades['Coste'].append(coste)

print(diccionarioHabilidades)
listaHabilidades = list()
ventajaMaxima = list()
costePH = list()
listaVacia = list()
vent = 0
puntosCoste = 0


def esSolucion(ventajaMaxima, puntosCoste, diccionarioHabilidades):
    return puntosCoste + min(diccionarioHabilidades['Coste']) > diccionarioHabilidades['Tope']


def esFactible(i, diccionarioHabilidades, puntosCoste,listaHabilidades):
    return diccionarioHabilidades['Coste'][i] + puntosCoste <= diccionarioHabilidades['Tope'] and diccionarioHabilidades['NumeroHabilidad'][i] not in listaHabilidades


def mochilaSora(diccionarioHabilidades, listaHabilidades, ventajaMaxima, k, puntosCoste, vent, listaVacia, costePH):
    if esSolucion(ventajaMaxima, puntosCoste, diccionarioHabilidades):
        ventajaMaxima.append(vent)
        costePH.append(puntosCoste)
        print(listaHabilidades)
        listaVacia.append(listaHabilidades)
    else:
        exito = False
        for i in range(k, len(diccionarioHabilidades['Ventaja'])):
            if esFactible(i, diccionarioHabilidades, puntosCoste,listaHabilidades):
                listaHabilidades.append(diccionarioHabilidades['NumeroHabilidad'][i])
                vent += diccionarioHabilidades['Ventaja'][i]
                puntosCoste += diccionarioHabilidades['Coste'][i]
                [listaVacia, ventajaMaxima, costePH] = mochilaSora(diccionarioHabilidades, listaHabilidades,
                                                                   ventajaMaxima, 0,
                                                                   puntosCoste, vent,
                                                                   listaVacia, costePH)
                if not exito:
                    listaHabilidades.remove(diccionarioHabilidades['NumeroHabilidad'][i])
                    vent -= diccionarioHabilidades['Ventaja'][i]
                    puntosCoste -= diccionarioHabilidades['Coste'][i]
    return listaVacia, ventajaMaxima, costePH


[listaVacia, ventajaMaxima, costePH] = mochilaSora(diccionarioHabilidades, listaHabilidades, ventajaMaxima, 0,
                                                   puntosCoste, vent,
                                                   listaVacia, costePH)

print(ventajaMaxima)
print(max(ventajaMaxima))
print(listaVacia)
print(costePH)
print(max(costePH))
