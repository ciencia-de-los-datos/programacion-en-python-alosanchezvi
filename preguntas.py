"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
# Leer el archivo 
Data = open("data.csv", "r").readlines()
# quitar \n
Data01=[dato.replace('\n','') for dato in Data]
# separar los componentes de cada fila
Data02=[dato.split('\t') for dato in Data01]

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """

    #seleccionar y sumar la columna dos 
    return sum([int(dato[1]) for dato in Data02])


def conteo(lista):
    return sorted([(dato,len(list(filter(lambda x: x==dato,lista )))) for dato in list(set(lista))])

# pregunta_02




def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    columns_0=[dato[0] for dato in Data02]
    return conteo(columns_0)


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    columns_0=[dato[0] for dato in Data02]
    columns_01=[dato[:2] for dato in Data02]
    return sorted([(dato,sum(list(map( lambda x: int(x[1]), list(filter(lambda x:  x[0]==dato,columns_01)))))) for dato in list(set(columns_0))] )


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    columns_2=[dato[2] for dato in Data02]
    mes=[dato[5:7] for dato in columns_2]
    return conteo(mes)


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    columns_01=[dato[:2] for dato in Data02]
    maximo=(lambda dato: max(list(map( lambda x: int(x[1]), list(filter(lambda x:  x[0]==dato,columns_01))))))
    minimo=(lambda dato: min(list(map( lambda x: int(x[1]), list(filter(lambda x:  x[0]==dato,columns_01))))))

    return sorted([(dato,maximo(dato),minimo(dato)) for dato in list(set(columns_0))] )

columns_4=[convert_dict(dato[4]) for dato in Data02]
def busqueda(valor):
    lista_values=[]
    lista_keys=[]
    for diccionario in columns_4:
            for keys,values in diccionario.items():
                lista_keys.append(keys)
                if keys==valor:
                    lista_values.append(diccionario[keys])
    return lista_values,list(set(lista_keys))     

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """  

    return sorted([(dato,min(busqueda(dato)[0]),max(busqueda(dato)[0])) for dato in keys])


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    columns_1=[dato[1] for dato in Data02]
    columns_01=[dato[:2] for dato in Data02]
    return sorted([(dato,list(map( lambda x: x[0], list(filter(lambda x:  x[1]==dato,columns_01))))) for dato in list(set(columns_1))] )


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    columns_1=[dato[1] for dato in Data02]
    columns_01=[dato[:2] for dato in Data02]

    return sorted([(dato,sorted(set(list(map( lambda x: x[0], list(filter(lambda x:  x[1]==dato,columns_01))))))) for dato in list(set(columns_1))] )


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    _,keys=busqueda('jjj')
    return sorted([(dato,min(busqueda(dato)[0]),max(busqueda(dato)[0])) for dato in keys])


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    columns_3=[dato[3] for dato in Data02]
    columns_4=[convert_dict(dato[4]) for dato in Data02]

    return [(len(dato03.split(',')),len(dato04)) for dato03,dato04 in zip(columns_3,columns_4)]


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    columns_13=[dato[1::2] for dato in Data02]
    valoresUnicos=[]
    for dato in Data02:
        valoresUnicos.extend(dato[3].split(','))
    valoresUnicos=list(set(valoresUnicos)) 
    return dict(sorted([(dato,sum(list(map( lambda x: int(x[0]), list(filter(lambda x: dato in  x[1].split(','),columns_13)))))) for dato in valoresUnicos] ))


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    columns_0=[dato[0] for dato in Data02]
    columns_4=[convert_dict(dato[4]) for dato in Data02]
    sum_columna_4=[[dato01,sum(dato04.values())]for dato01,dato04 in zip(columns_0,columns_4)]
    return dict(sorted([(dato,sum(list(map(lambda x: x[1], list(filter( lambda x : x[0]==dato,sum_columna_4 )))))) for dato in list(set(columns_0))]))
