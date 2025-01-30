"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import csv
def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    with open('files/input/data.csv', 'r') as file:
        data = list(csv.reader(file, delimiter='\t'))
        
    data = [fila[4] for fila in data]

    data = [fila.split(',') for fila in data]

    data = [dict([fila.split(':') for fila in fila]) for fila in data]

    llave = set([llave for fila in data for llave in fila.keys()])

    resultado = []
    for llave in llave:
        valores = [int(fila[llave]) for fila in data if llave in fila]
        resultado.append((llave, min(valores), max(valores)))

    resultado = sorted(resultado, key=lambda x: x[0])
    return resultado

print(pregunta_06())