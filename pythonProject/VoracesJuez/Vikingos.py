# dos enteros n y t que indican el numero de series disponibles y el tiempo maximo
# por serie que el usuario puede dedicar a verlas

# las siguientes n lines contienen la serie y la puntuacion y duracion

# suma de las puntuaciones

Numeroseries, tiempo = map(int, input().strip().split())

diccionarioSeries = {
    'series': [],
    'puntuacion': [],
    'duracion': [],
    'tiempoMaximo': tiempo
}

for i in range(Numeroseries):
    serie, puntuacion, duracion = (input().strip().split())
    diccionarioSeries['series'] += [serie]
    diccionarioSeries['puntuacion'] += [puntuacion]
    diccionarioSeries['duracion'] += [duracion]


def mochilaDeSeries(diccionarioSeries):
    n = len(diccionarioSeries['series'])
    candidatos = set()
    for i in range(n):
        candidatos.add(i)
    tiempoLibre = int(diccionarioSeries['tiempoMaximo'])
    valoracion = 0
    porcentajeValoracion = 0.0
    sol = [0] * n
    solucion = False
    while candidatos and tiempoLibre > 0 and not solucion:
        mejorSerie = getMejorSerie(candidatos, diccionarioSeries, tiempoLibre)
        candidatos.remove(mejorSerie)
        if factible(diccionarioSeries, mejorSerie, tiempoLibre):
            sol[mejorSerie] = 1.0
            tiempoLibre -= int(diccionarioSeries['duracion'][mejorSerie])
            valoracion += int(diccionarioSeries['puntuacion'][mejorSerie])
        else:
            #tiempoLibre -= int(diccionarioSeries['duracion'][mejorSerie])
            #print(tiempoLibre)
            porcentajeValoracion = int(tiempoLibre) / int(
                diccionarioSeries['duracion'][mejorSerie])
            sol[mejorSerie] = porcentajeValoracion
            valoracion += int(diccionarioSeries['puntuacion'][mejorSerie]) / porcentajeValoracion
            solucion = True
    return sol


def getMejorSerie(candidatos, diccionarioSeries, tiempo):
    ratio = 0
    item = 0
    for c in candidatos:
        r = int(diccionarioSeries['puntuacion'][c]) / int(diccionarioSeries['duracion'][c])
        if r > ratio:
            ratio = r
            item = c
    return item


def factible(diccionarioSeries, mejorSerie, tiempoLibre):
    return tiempoLibre - int(diccionarioSeries['duracion'][mejorSerie]) > 0


def mostrarSolucion(sol, diccionarioSeries):
    n = len(sol)
    valoracion = 0
    for i in range(0, n, 1):
        if sol[i] == 1.0:
            print(diccionarioSeries['series'][i])
            valoracion += int(diccionarioSeries['puntuacion'][i])
            #print(valoracion)
        elif sol[i] < 1.0 and sol[i] > 0:
            print(diccionarioSeries['series'][i])
            #print(int(diccionarioSeries['puntuacion'][i]) * int(sol[i]))
            valoracion += int(diccionarioSeries['puntuacion'][i]) * sol[i]
    print(int(valoracion))
    #print(sol)


sol = mochilaDeSeries(diccionarioSeries)
mostrarSolucion(sol, diccionarioSeries)
