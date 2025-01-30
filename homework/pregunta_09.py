"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    with open('files/input/data.csv', 'r') as file:
        data = list(csv.reader(file, delimiter='\t'))
        
    data = [fila[4] for fila in data]

    data = [fila.split(',') for fila in data]

    data = [dict([fila.split(':') for fila in fila]) for fila in data]
    llaves = set([llave for fila in data for llave in fila.keys()])

    resultado = []
    for llave in llaves:
        valores = [int(fila[llave]) for fila in data if llave in fila]
        resultado.append((llave, len(valores)))
    
    resultado = sorted(resultado, key=lambda x: x[0])
    resultado = dict(resultado)
    return resultado

print(pregunta_09())