import copy
from queue import PriorityQueue


def InicializarDatos():
    datos = {}
    datos['N'] = 5
    datos['dist'] = [[0, 29, 20, 21, 16],
                     [29, 0, 15, 29, 28],
                     [20, 15, 0, 15, 14],
                     [21, 29, 15, 0, 4],
                     [16, 28, 14, 4, 0]]
    datos['nombres'] = ['maastricht', 'aachen', 'heerlen', 'sittard', 'geleen']

    # Para cada ciudad guardamos la distancia de la más cercana
    # (usaremos esto para establecer y actualizar la cota)
    datos['minimos'] = [float('inf')] * datos['N']
    for i in range(datos['N']):
        for j in range(datos['N']):
            if 0 < datos['dist'][i][j] < datos['minimos'][i]:
                datos['minimos'][i] = datos['dist'][i][j]

    return datos


def GenerarTuplaVacia(datos):
    solucion = {}
    solucion['cota'] = sum(datos['minimos'])
    solucion['elems'] = [-1] * datos['N']
    solucion['coste'] = 0
    # partimos del vertice 0
    solucion['elems'][0] = 0
    solucion['visitados'] = {0}
    solucion['tope'] = 1
    return solucion


def esSolucion(sol):
    return sol['tope'] == len(sol['elems'])


def SolucionVorazInicial(datos):
    sol = GenerarTuplaVacia(datos)

    # Criterio voraz: ir a la mas cercana
    actual = sol['elems'][sol['tope'] - 1]
    for i in range(1, datos['N']):
        mejor = -1
        cercana = float('inf')
        for adj in range(1, datos['N']):
            if adj not in sol['visitados'] and 0 < datos['dist'][actual][adj] < cercana:
                mejor = adj
                cercana = datos['dist'][actual][adj]
        assert mejor != -1
        asignar(sol, mejor, datos)
        actual = mejor
    return sol


def asignar(sol, sig, datos):
    # Incluimos el vertice siguiente en la solucion
    # y la arista anterior-siguiente en el coste
    ant = sol['elems'][sol['tope'] - 1]  # vertice anterior
    sol['coste'] += datos['dist'][ant][sig]
    sol['cota'] += datos['dist'][ant][sig] - datos['minimos'][ant]

    # visitar vertice
    sol['elems'][sol['tope']] = sig
    sol['visitados'].add(sig)
    if sol['tope'] == datos['N'] - 1:
        # incluir arista al vertice inicial
        sol['coste'] += datos['dist'][sig][0]
        sol['cota'] += datos['dist'][sig][0] - datos['minimos'][sig]
        assert sol['cota'] == sol['coste']

    sol['tope'] += 1
    return sol


def compleccionesFactibles(sol, datos):
    actual = sol['elems'][sol['tope'] - 1]

    listaHijos = []
    for siguiente in range(datos['N']):
        if siguiente not in sol['visitados'] and siguiente != actual:
            hijo = copy.deepcopy(sol)
            asignar(hijo, siguiente, datos)
            listaHijos.append(hijo)

    return listaHijos


def visualizar(tupla, datos):
    tupla = tupla[:]  # copiamos los datos para no modificarlos
    tupla.append(tupla[0])  #
    print("Recorrido del viajante:\n  ", end="")
    for i in range(len(tupla) - 1):
        print(datos['nombres'][tupla[i]], end=" --")
        print(datos['dist'][tupla[i]][tupla[i + 1]], end="--> ")

    print(datos['nombres'][tupla[0]])


def RamificacionYPoda(datos):
    solMejor = SolucionVorazInicial(datos)  # Algoritmo voraz
    sol = GenerarTuplaVacia(datos)  # Tupla parcial inicialmente vacía
    q = PriorityQueue()
    identificador = 0
    q.put((sol['cota'], identificador, sol))  # se añade la sol inicial (prioridad, id, sol)
    identificador += 1
    while not q.empty():
        priority, idsol, sol = q.get()  # Sol es el nodo de prioridad max
        if esSolucion(sol):
            if sol['coste'] < solMejor['coste']:
                solMejor = sol  # Se actualiza SolMejor
        else:
            if sol['cota'] < solMejor['coste']:  # Criterio de poda
                hijos = compleccionesFactibles(sol, datos)
                for hijo in hijos:
                    if hijo['cota'] < solMejor['coste']:
                        q.put((hijo['cota'], identificador, hijo))
                        identificador += 1
    # print("Explorados:", identificador)
    return solMejor


# Pog Ppal:
datos = InicializarDatos()
sol = RamificacionYPoda(datos)
print('La mejor solucion es:', sol)

visualizar(sol['elems'], datos)