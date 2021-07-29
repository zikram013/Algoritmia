import sys
import random

n = 10
tarea = []

for i in range(n):
    tarea.append(random.uniform(44, 120))


def algoritmoVoraz(tarea):
    candidatos = set()  # Conjunto de candidatos
    n = len(tarea)
    sol = []
    for i in range(n):
        candidatos.add(i)  # los rellenas segun la cantidad de pacientes
    while candidatos:
        mejorTarea = getMejorTarea(candidatos, tarea)
        sol.append(mejorTarea)
        candidatos.remove(mejorTarea)
    return sol


def getMejorTarea(candidatos, tarea):
    tareaMenorTiempo = sys.maxsize  # Lo pone al maximo valor
    for c in candidatos:
        tiempo = tarea[c]
        if tiempo < tareaMenorTiempo:
            tareaMenorTiempo = tiempo
            mejorTarea = c
    return mejorTarea


sol = algoritmoVoraz(tarea)
print(sol)

tiempoTotal = 0
for t in sol:
    print(str(t), end="")
    tiempoTotal += tarea[t]

print("SUM: " + str(tiempoTotal))
print("SUM: " + str(tiempoTotal / n))
