"""
4
2
1 5 2 7
3
1 2 2 3 3 4
3
1 2 1 3 2 3
7
1 4 3 6 2 8 4 8 5 10 8 12 12 20
"""

casos = int(input())
dictActividades = dict()
dictActividades['Actividad'] = []
dictActividades['Programa'] = []
for i in range(casos):
    numeroActivides = int(input())
    dictActividades['Actividad'].append(numeroActivides)
    momentos = list(map(int, input().strip().split()))
    dictActividades['Programa'].append(momentos)


def dameTarea(actividad, programa, listaTareasHechas, listaTareaFin, i):
    tarea = -1
    ultimaTarea = 0
    if len(listaTareaFin) > 0:
        ultimaTarea = listaTareaFin[-1]
    sol = False
    for j in range(i, len(programa)):
        if j % 2 == 0:
            if programa[j] >= ultimaTarea:
                tarea = j
                sol=True
                break
    return tarea,sol


def voraz(actividad, programa):
    candidatos = set()
    tareas = 0
    listaTareaInicio = list()
    listaTareaFin = list()
    listaTareasHechas = list()
    sol = False
    i = 0
    while i < len(programa):
        tarIni,sol = dameTarea(actividad, programa, listaTareasHechas, listaTareaFin, i)
        if sol:
            tareas += 1
            listaTareasHechas.append(programa[tarIni])
            listaTareaFin.append(programa[tarIni+1])
        i += 2
    return listaTareasHechas


for i in range(casos):
    sol = voraz(dictActividades['Actividad'][i], dictActividades['Programa'][i])
    print(sol)
