"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/input/data.csv', 'r') as file:
        data = list(csv.reader(file, delimiter='\t'))
        
    data = data[1:]
    data = sorted(data, key=lambda x: x[0])
    resultado = []
    
    for i in range(len(data)):
        if i == 0:
            letra = data[i][0]
            max_valor = int(data[i][1])
            min_valor = int(data[i][1])
        elif data[i][0] != letra:
            resultado.append((letra, max_valor, min_valor))
            letra = data[i][0]
            max_valor = int(data[i][1])
            min_valor = int(data[i][1])
        else:
            max_valor = max(max_valor, int(data[i][1]))
            min_valor = min(min_valor, int(data[i][1]))
    
    resultado.append((letra, max_valor, min_valor))
    return resultado

print(pregunta_05())