"""
5 10
Perdiz 5 20
Esparragos 3 15
Aceite 2 5
Gambas 6 13
Leon 5 10
"""
productos, carrito = map(int, input().strip().split())
diccionarioProductos = dict()
diccionarioProductos['Nombre'] = []
diccionarioProductos['Peso'] = []
diccionarioProductos['Importancia'] = []
diccionarioProductos['tope'] = carrito

for i in range(productos):
    nombre, peso, valor = map(str, input().strip().split())
    diccionarioProductos['Nombre'].append(nombre)
    diccionarioProductos['Peso'].append(int(peso))
    diccionarioProductos['Importancia'].append(int(valor))

print(diccionarioProductos)

valorTope = 0
minValor = 0
pesoTope = 0
ini = 0
listaConProductos = list()


def esSolucion(diccionarioProductos, pesoTope):
    return pesoTope + min(diccionarioProductos['Peso']) > diccionarioProductos['tope']


def esFactible(diccionarioProductos, i, pesoTope, listaConProductos):
    return diccionarioProductos['Peso'][i] + pesoTope <= diccionarioProductos['tope'] and \
           diccionarioProductos['Nombre'][i] not in listaConProductos


def carrito(diccionarioProductos, listaConProductos, valorTope, pesoTope, minValor, ini, lista):
    if esSolucion(diccionarioProductos, pesoTope):
        lista.append(valorTope)
        if valorTope>minValor:
            minValor=valorTope
    else:
        exito = False
        for i in range(ini, len(diccionarioProductos['Nombre'])-1):
            if esFactible(diccionarioProductos, i, pesoTope, listaConProductos):
                pesoTope += diccionarioProductos['Peso'][i]
                valorTope += diccionarioProductos['Importancia'][i]
                listaConProductos.append(diccionarioProductos['Nombre'][i])
                [minValor, lista] = carrito(diccionarioProductos, listaConProductos, valorTope, pesoTope, minValor, i,
                                            lista)
                if not exito:
                    pesoTope -= diccionarioProductos['Peso'][i]
                    valorTope -= diccionarioProductos['Importancia'][i]
                    listaConProductos.remove(diccionarioProductos['Nombre'][i])
    return minValor, lista


lista = list()
[minValor, lista] = carrito(diccionarioProductos, listaConProductos, valorTope, pesoTope, minValor, ini, lista)
print(max(lista))
print(minValor)
