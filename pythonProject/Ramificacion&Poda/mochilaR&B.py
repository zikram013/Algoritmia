from queue import PriorityQueue

from numpy.ma import copy


def InicializarDatos():
    datos = {}
    datos['N'] = 4
    datos['W'] = 15
    datos['valor'] = [10, 10, 12, 18]
    datos['peso'] = [2, 4, 6, 9]
    datos['v/p'] = [5., 2.5, 2., 2.]
    return datos


def solucionInicial(datos):
    sol = {}
    sol['elems'] = [-1] * datos['N']
    sol['peso'] = 0
    sol['valor'] = 0
    i = 0
    while i < datos['N'] and sol['peso'] < datos['W']:
        if sol['peso'] + datos['peso'][i] <= datos['W']:
            sol['elems'][i] = 1
            sol['peso'] += datos['peso'][i]
            sol['valor'] += datos['valor'][i]
        i += 1
    return sol

def generarTuplaVacia(datos):
    tupla = {}
    tupla['elems'] = [-1] * datos['N']
    tupla['tope'] = 0
    tupla['valor'] = 0
    tupla['peso'] = 0
    tupla['cota'] = datos['W'] * datos['v/p'][0]


def asignar(tupla, valor, datos):
    tupla['elems'][tupla['tope']] = valor
    tupla['valor'] += valor * datos['valor'][tupla['tope']]
    tupla['peso'] += valor * datos['peso'][tupla['tope']]
    if tupla['tope'] == datos['N'] - 1:
        tupla['cota'] = tupla['valor']
    else:
        tupla['cota'] = tupla['valor'] + datos['v/p'][tupla['tope'] + 1] * (datos['W'] - tupla['peso'])
    tupla['tope'] += 1
    return tupla


def complecciones(tupla, datos):
    # Dos posibilidades (se incluye o no el objeto en la solucion):
    hijos = []
    for i in range(2):
        h = copy.deepcopy(tupla)
        asignar(h, i, datos)
        hijos.append(h)
    return hijos

def esSolucion(tupla):
    return tupla['tope'] == len(tupla['elems'])

def esFactible(tupla, datos):
    return tupla['peso'] <= datos['W']


def RamificacionYPoda(datos):
    solMejor = solucionInicial(datos) #algoritmo voraz
    tupla = generarTuplaVacia(datos)
    iden = 0
    qp = PriorityQueue()
    print(tupla['cota'])
    qp.put(
        (-tupla['cota'], iden, tupla)
    )
    id += 1
    while not qp.empty():
        priority, ide, tupla = qp.get()  # Sol es el nodo de prioridad max
        if esSolucion(tupla):
            if tupla['valor'] > solMejor['valor']:
                solMejor = tupla  # Se actualiza SolMejor
        elif tupla['cota'] > solMejor['valor']:  # Criterio de poda
            hijos = complecciones(tupla, datos)
            for hijo in hijos:
                if esFactible(hijo, datos) and tupla['cota'] > solMejor['valor']:
                    qp.put((-hijo['cota'], iden, hijo))
                    id += 1
    print("Nodos explorados:", iden)
    return solMejor




def main():
    datos = InicializarDatos()
    sol = RamificacionYPoda(datos)
    print('La mejor solucion es:', sol)


main()