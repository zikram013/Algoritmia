print("Niños barrio")
n = int(input())
contador_repeticiones = 0

nombres = []
for i in range(n):
    nombres.append(input())

print("intentos de nombre")
intentos = int(input())
nombresIntentos = []
for i in range(intentos):
    nombresIntentos.append(input())

for i in nombresIntentos:
    for j in nombres:
        if i == j:
            contador_repeticiones = contador_repeticiones + 1
    if contador_repeticiones == 0:
        print("Nuevo")
    else:
        print(contador_repeticiones)
    contador_repeticiones = 0