# Conjunto de candidatos: n Objetos
# Funcion Solucion: cuando no puedan añadirse mas fracciones de objetos a la mochila
# Funcion de factibilidad
# Funcion objetivo: Maximizar los objetos (candidatos)que pueda metar
# Funcion de seleccion
# En esta variante del problema los objetos se pueden partir pero no repetir

n = 5
data = {'profit': [20, 30, 66, 40, 60], 'peso': [10, 20, 30, 40, 50], 'pesoMaximo': 100}


def vorazMochila(data):
    n = len(data['profit'])
    candidatos = set()
    for i in range(n):
        candidatos.add(i)
    pesoLibre = data['pesoMaximo']
    sol = [0] * n
    isSol = False
    while not isSol and candidatos:
        mejorElemento = getMejorELemento(candidatos, data)  # sacamos el de mejor ratio
        candidatos.remove(mejorElemento)
        if isFeasible(data, mejorElemento, pesoLibre):
            sol[mejorElemento] = 1.0
            pesoLibre -= data['peso'][mejorElemento]
        else:
            sol[mejorElemento] = pesoLibre / data['peso'][mejorElemento]
            isSol = True
    return sol


def getMejorELemento(candidatos, data):
    bestRatio = 0
    bestItem = 0

    for c in candidatos:
        r = data['profit'][c] / data['peso'][c]
        if r > bestRatio:
            bestRatio = r
            bestItem = c
    return bestItem


def isFeasible(data, mejorElemento, pesoLibre):
    return pesoLibre - data['peso'][mejorElemento] > 0


sol = vorazMochila(data)
print(sol)
