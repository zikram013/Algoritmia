# La primera linea contiene dos enteros N - participantes y gurpos
import sys

participantes, grupos = map(int, input().strip().split())

personas = {}
# Cadena de caracteres sin espacion C que indica el nombre y la edad
for i in range(participantes):
    nombre, edad = map(str, input().strip().split())
    personas[nombre] = edad


def algoritmoGrupos(personas, grupos):
    listaGrupoJoven = []
    listaGrupoMayores = []
    listaPersonaJoven = []
    listaPersonaMayores = []
    candidatos = set()
    clavesDiccionario = personas.keys()
    contador = 0
    n = len(personas)
    for i in clavesDiccionario:
        candidatos.add(i)
    while candidatos:
        len(listaGrupoJoven)
        mejorPersona = getMejorPersona(candidatos, personas, contador)
        candidatos.remove(mejorPersona)
        sumaJoven = sum(listaGrupoJoven)
        sumaViejos = sum(listaGrupoMayores)
        edadAsumar = int(personas[mejorPersona])
        # sumaJoven += edadAsumar
        # sumaViejos += edadAsumar
        # print(sumaJoven, edadAsumar)

        if sumaJoven <= edadAsumar and len(listaGrupoMayores) == 0:
            if len(listaGrupoJoven) < grupos:
                listaGrupoJoven.append(int(personas[mejorPersona]))
                listaPersonaJoven.append(mejorPersona)
            else:
                listaGrupoMayores.append(int(personas[mejorPersona]))
                listaPersonaMayores.append(mejorPersona)
        else:
            # print("entra else")
            #if len(listaGrupoMayores) < grupos:
                listaGrupoMayores.append(int(personas[mejorPersona]))
                listaPersonaMayores.append(mejorPersona)
           # else:
            #    listaGrupoJoven.append(int(personas[mejorPersona]))
             #   listaPersonaJoven.append(mejorPersona)


    # print(listaPersonaMayores)
    resultado(listaPersonaJoven, listaPersonaMayores)


def resultado(listaPersonaJoven, listaPersonaMayores):
    cadena = ""
    cadenaMayores = ""
    for i in listaPersonaJoven:
        cadena = cadena + i + " "
    for i in listaPersonaMayores:
        cadenaMayores = cadenaMayores + i + " "
    print(cadena)
    print(cadenaMayores)


def getMejorPersona(candidatos, personas, contador):
    menorEdad = sys.maxsize
    for c in candidatos:
        edad = int(personas[c])
        if edad < menorEdad:
            menorEdad = edad
            nombrePersona = c
    return nombrePersona


algoritmoGrupos(personas, grupos)
