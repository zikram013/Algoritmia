"""
5 3
66 24
10 21
84 14
95 98
20 22
207 75
166 85
184 82

"""

programas, pruebas = map(int, input().strip().split())
diccionarioProgramas = dict()
diccionarioProgramas['Importancia'] = []
diccionarioProgramas['Paginas'] = []
diccionarioProgramas['Baremos'] = []

for i in range(programas):
    importancia, paginas = map(int, input().strip().split())
    diccionarioProgramas['Importancia'].append(importancia)
    diccionarioProgramas['Paginas'].append(paginas)
    diccionarioProgramas['Baremos'].append(paginas / importancia)

print(diccionarioProgramas)


def dameElemento(candidatos, diccionarioProgramas):
    ratio = 0
    item = 0
    for i in candidatos:
        r = diccionarioProgramas['Baremos'][i]
        if r > ratio:
            ratio = r
            item = i
    return item


def factible(topePaginas, topeImportancia, mejorElement, diccionarioProgramas):
    return topePaginas - diccionarioProgramas['Paginas'][mejorElement] > 0 and topeImportancia - \
           diccionarioProgramas['Importancia'][mejorElement] > 0


def voraz(diccionarioProgramas, importanciaTotal, totalPaginas):
    candidatos = set()
    n = len(diccionarioProgramas['Importancia'])
    libros = [0] * n
    importa = [0] * n
    for i in range(n):
        candidatos.add(i)
    topePaginas = totalPaginas
    topeImportancia = importanciaTotal
    sol = False
    while candidatos and not sol:
        mejorElement = dameElemento(candidatos, diccionarioProgramas)
        candidatos.remove(mejorElement)
        if factible(topePaginas, topeImportancia, mejorElement, diccionarioProgramas):
            libros[mejorElement] = 1.0
            importa[mejorElement] = 1.0
            topePaginas -= diccionarioProgramas['Paginas'][mejorElement]
            topeImportancia -= diccionarioProgramas['Importancia'][mejorElement]
        else:
            libros[mejorElement] = topePaginas / diccionarioProgramas['Paginas'][mejorElement]
            importa[mejorElement] = topeImportancia / diccionarioProgramas['Importancia'][mejorElement]
            topeImportancia -= diccionarioProgramas['Importancia'][mejorElement]
            sol = True
    return libros, importa


for i in range(pruebas):
    importanciaTotal, totalPaginas = map(int, input().strip().split())
    libros, importa = voraz(diccionarioProgramas, importanciaTotal, totalPaginas)
    print(libros)
    #print(importa)
