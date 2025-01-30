"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    with open('files/input/data.csv', 'r') as file:
        data = list(csv.reader(file, delimiter='\t'))
    
    dict_data = {}
    
    for fila in data:

        llave = fila[0]
        valores = [int(par.split(':')[1]) for par in fila[4].split(',')]

        if llave in dict_data:
            dict_data[llave]+=sum(valores)
        else:
            dict_data[llave]=sum(valores)
    
    dict_data = dict(sorted(dict_data.items()))
    return dict_data

print(pregunta_12())