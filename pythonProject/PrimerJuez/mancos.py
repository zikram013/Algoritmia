jugadores = int(input())
puntuacion = []
contador = 0
for i in range(jugadores):
    puntuacion.append(int(input()))

for j in puntuacion:
    contador = contador + j

media = contador / jugadores
jugadores_cumplen = list(filter(lambda v: v >= media, puntuacion))
print(jugadores_cumplen)