"""
4
CCUCGGCGGGCA
CCUCGGCGCU
CCUCAGCG
CCUCAGCAUC
"""
numeroMutaciones = int(input())
dictMutaciones = dict()
dictMutaciones['NumeroMutaciones'] = numeroMutaciones
dictMutaciones['Mutacion'] = []
dictMutaciones['Longitud'] = []
for i in range(numeroMutaciones):
    mutacion = str(input())
    dictMutaciones['Mutacion'].append(mutacion)
    dictMutaciones['Longitud'].append(len(mutacion))

print(dictMutaciones)


def prefijo(candidatos, dictMutaciones, i):
    palabra = dictMutaciones['Mutacion'][0]
    letra = palabra[i]
    sol = True
    for j in range(1, dictMutaciones['NumeroMutaciones']):
        palabra = dictMutaciones['Mutacion'][j]
        com = palabra[i]
        if letra == com:
            sol = False
        else:
            sol = True
            break
    return letra, sol


def vorazMutacion(dictMutaciones):
    candidatos = set()
    n = min(dictMutaciones['Longitud'])
    for i in range(n):
        candidatos.add(i)
    letras = list()
    sol = False
    i = 0
    while not sol and i < len(candidatos):
        comprobarLetra, sol = prefijo(candidatos, dictMutaciones, i)
        letras.append(comprobarLetra)
        i += 1
    if sol:
        letras.pop()
    return letras


sol = vorazMutacion(dictMutaciones)
print(sol)
