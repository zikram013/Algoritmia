# La primera linea contiene un numero entero que indica el numero de clientes
import sys

pedidos = int(input())
# Contienen dos enteros C y T que identifcan el cliente y el tiempo que se tarda
diccionarioClientes = {}
for i in range(pedidos):
    cliente, tiempo = map(int, input().strip().split())
    diccionarioClientes[cliente] = tiempo


# print(diccionarioClientes)
def tiempoMinimo(diccionarioClientes):
    candidatos = set()
    realizados = []
    n = len(diccionarioClientes)
    for i in range(1, n + 1, 1):
        candidatos.add(i)
    for i in range(n):
        realizados.append(True)
    tiempo = 0
    while candidatos:
        mejorTarea = getMejorTarea(candidatos, diccionarioClientes)
        realizados[mejorTarea - 1] = False
        dameTiempo = contarTiempo(realizados, diccionarioClientes)
        tiempo = tiempo + dameTiempo
        candidatos.remove(mejorTarea)
    return tiempo


def getMejorTarea(candidatos, diccionarioClientes):
    tareaMenorTiempo = sys.maxsize
    for c in candidatos:
        tiempo = diccionarioClientes[c]
        if tiempo < tareaMenorTiempo:
            tareaMenorTiempo = tiempo
            mejorTarea = c
    return mejorTarea


def contarTiempo(realizados, diccionarioClientes):
    contar = 0
    contador = 1
    for i in realizados:
        if i == False:
            contar += diccionarioClientes[contador]
        contador += 1
    # print(contar)
    return contar


sol = tiempoMinimo(diccionarioClientes)
print(sol)
