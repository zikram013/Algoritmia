from collections import deque

# Ordenacion topologica
# Se pueden quitar los padres dado que no son utilziados
# Debemos realizar un diccionario donde en cada nodo se le asigna una lista con aquellas componenentes a las que accede
g = {
    0: [],
    1: [],
    2: [3],
    3: [1],
    4: [0, 1],
    5: [2, 0]
}

g2 = {
    "calcetines": ["zapatos"],
    "pantalon": ["zapatos", "cinturon"],
    "camisa": ["cinturon", "jersey"],
    "zapatos": [],
    "cinturon": [],
    "jersey": []
}


def ordenacion_topologica(g):
    data = {
        "grafo": g,
        "estado": {},  # Si esta visitado o no. Almacena el nodo y su valor
        "padre": {},  # Nodo anterior desde el que accedemos
        "d": {},  # Vector d, nos indica cuando los visitamos
        "tiempo": 0,  # Momento en el que se realiza el paso
        "f": {},  # Nos indica cuando todos los nodos adyacentes estan visitados
        "lista": deque()  # Bicola para almacenar los datos introduciendolos por la izquierda
    }
    for k in g.keys():
        data["estado"][k] = "No visitado"
        data["padre"][k] = None
        data["d"][k] = 0
        data["f"][k] = 0
    for k in g.keys():
        if data["estado"][k] == "No visitado":
            ##if data["d"][k] == 0 and data["f"][k] == 0: ambas formas son validas
            topologico_visita(data, k)
    return data["lista"]


def topologico_visita(data, k):
    data["estado"][k] = "Visitado"
    data["tiempo"] = data["tiempo"] + 1
    data["d"][k] = data["tiempo"]
    for ady in data["grafo"][k]:
        if data["estado"][ady] == "No visitado":
            data["padre"][ady] = k
            topologico_visita(data, ady)
    data["estado"][k] = "Fin"
    data["tiempo"] = data["tiempo"] + 1
    data["f"][k] = data["tiempo"]
    data["lista"].appendleft(k)


print(ordenacion_topologica(g))
