"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open('files/input/data.csv', 'r') as file:
        data = list(csv.reader(file, delimiter='\t'))
    contar = {}
    for fila in data:
        if fila[0] not in contar:
            contar[fila[0]] = 0
        contar[fila[0]] += int(fila[1])
    
    contar = [(letra, suma) for letra, suma in contar.items()]
    contar.sort()
    return contar

print(pregunta_03())