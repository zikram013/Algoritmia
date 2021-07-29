import copy


def inicializarDatos():
    datos = {}
    datos['N'] = 4
    datos['W'] = 8
    datos['Peso'] = [2, 3, 4, 5]
    datos['Valor'] = [3, 5, 6, 10]
    return datos


# 2,2,2 | 9
# sol['Objetos'] = [3,0,0,0]
# sol['Peso'] = 6
# sol['Valor'] = 9
# 2,3,3 | 13
# sol['Objetos'] = [1,2,0,0]
# sol['Peso'] = 8
# sol['Valor'] = 13

def inicializarSolucion(datos):
    sol = {}
    sol['Objetos'] = [0] * datos['N']
    sol['Peso'] = 0
    sol['Valor'] = 0
    return sol


# 2,2,2,2 | 12
# sol['Objetos'] = [4,0,0,0]
# sol['Peso'] = 8
# sol['Valor'] = 12
# borrar el 2
# sol['Objetos'] = [3,0,0,0]
# sol['Peso'] = 6
# sol['Valor'] = 9
def borrar(sol, i, datos):
    sol['Objetos'][i] -= 1
    sol['Peso'] -= datos['Peso'][i]
    sol['Valor'] -= datos['Valor'][i]
    return sol


# 2,2,2 | 9
# sol['Objetos'] = [3,0,0,0]
# sol['Peso'] = 6
# sol['Valor'] = 9
# introducir el 2
# sol['Objetos'] = [4,0,0,0]
# sol['Peso'] = 8
# sol['Valor'] = 12
def asignar(sol, i, datos):
    sol['Objetos'][i] += 1
    sol['Peso'] += datos['Peso'][i]
    sol['Valor'] += datos['Valor'][i]
    return sol


def esSolucion(sol, datos):
    return sol['Peso'] + min(datos['Peso']) > datos['W']


def mejor(sol1, sol2):
    if sol1['Valor'] > sol2['Valor']:
        mejor = copy.deepcopy(sol1)
    else:
        mejor = copy.deepcopy(sol2)
    return mejor


def esFactible(sol, i, datos):
    return sol['Peso'] + datos['Peso'][i] <= datos['W']


def mochilaVA(sol, mejorSol, datos, k):
    if esSolucion(sol, datos):
        mejorSol = mejor(sol, mejorSol)
    else:
        # for i in range(0, datos['N'])
        for i in range(k, datos['N']):
            if esFactible(sol, i, datos):
                sol = asignar(sol, i, datos)
                mejorSol = mochilaVA(sol, mejorSol, datos, i)
                sol = borrar(sol, i, datos)
    return mejorSol


datos = inicializarDatos()
sol = inicializarSolucion(datos)
mejorSol = inicializarSolucion(datos)
mejorSol = mochilaVA(sol, mejorSol, datos, 0)
print(mejorSol)
