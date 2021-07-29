import sys

# En caso de que las monedas estuvieran listadas de menor a mayor seria recorrer el array
# de forma invertida
monedas = [500, 200, 100, 50, 20, 10, 5, 2, 1]


def algoritmoDelCambio(monedas):
    precio, pagado = map(int, input().strip().split())
    candidatos = set()
    diccionarioMonedas = {}
    n = len(monedas)
    for i in range(n):
        candidatos.add(i)
    vuelta = pagado - precio
    print(vuelta)
    while vuelta > 0:
        mejorCambio = getMejorMoneda(candidatos, monedas, vuelta)
        if mejorCambio in diccionarioMonedas:
            diccionarioMonedas[mejorCambio] += 1
        else:
            diccionarioMonedas[mejorCambio] = 1
        vuelta = vuelta - mejorCambio
    return diccionarioMonedas


def getMejorMoneda(candidatos, monedas, vuelta):
    monedaMasAlta = sys.maxsize
    for c in candidatos:
        moneda = monedas[c]
        if moneda <= vuelta:
            print(moneda)
            return moneda


cambio = algoritmoDelCambio(monedas)
print(cambio)
