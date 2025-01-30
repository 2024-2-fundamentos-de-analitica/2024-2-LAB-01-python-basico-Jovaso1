"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}

    """
    with open('files/input/data.csv', 'r') as file:
        data = list(csv.reader(file, delimiter='\t'))
    
    dict_data = {}

    for fila in data:
        letras = fila[3].split(',')
        for letra in letras:
            if letra in dict_data:
                dict_data[letra]+=int(fila[1])
            else:
                dict_data[letra]=int(fila[1])
    
    dict_data = dict(sorted(dict_data.items()))
    
    return dict_data

print(pregunta_11())