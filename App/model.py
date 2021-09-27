﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

def newCatalog():
    """ Inicializa el catálogo de libros

    Crea una lista vacia para guardar todos los libros

    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion

    Retorna el catalogo inicializado.
    """
    catalog = {'artworks': None,
               'medios': None}

    catalog['artworks'] = lt.newList('SINGLE_LINKED', compareObjectIds)

    catalog['medios'] = mp.newMap(138.112,
                                   maptype='CHAINING',
                                   loadfactor=2.0,
                                   comparefunction=compareMedium)

    return catalog



# Funciones para agregar informacion al catalogo

def AddArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    addlistmedium(catalog, artwork)


# def addMediumartwork(catalog, artwork):
#     try:
#         medios = catalog["medios"]
#         if (artwork["Medium"] != ''):
#             medio = artwork["Medium"]
#         else:
#             medio = "unknown"

#         exitsmedium = mp.contains(medios, medio)

#         if exitsmedium:
#             entry = mp.get(medios, medio)
#             hmmm = me.getValue(entry)
#         else:
#             hmmm =  newMedium(medio)
#             mp.put(medios, medio, hmmm)
#         lt.addLast(hmmm["Medium", medio])
#     except Exception:
#         return None

def addlistmedium(catalog, artwork):
    obras = catalog["artworks"]
    medios = catalog["medios"]
    if mp.contains(medios, artwork["Medium"]):
        lista = mp.get(medios, artwork["Medium"])["value"]
        lt.addLast(lista, artwork)
        mp.put(medios, artwork["Medium"], lista)
    else:
        lst = lt.newList('ARRAY_LIST')
        lt.addLast(lst, artwork)
        mp.put(medios, artwork["Medium"], lst)
    return catalog




# Funciones para creacion de datos

# Funciones de consulta

def compareObjectIds(id1, id2):
    """
    Compara dos Objects ids de dos obras
    """
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareMedium(medio, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (medio == str(identry)):
        return 0
    else:
        return -1


def topnantiguas(catalog, medio, top):
    medios = catalog["medios"]
    med = mp.get(medios, medio)["value"]
    retorno = lt.newList()
    centinela = 1
    while top >= centinela:
        lt.addLast(retorno, lt.getElement(med, centinela))
        centinela += 1
    return retorno


# Funciones utilizadas para comparar elementos dentro de una lista

def compareDate(art1, art2):
    if art1['Date'] != '' and art2['Date'] != '':
        return float(art1['Date']) < float(art2['Date'])


# Funciones de ordenamiento


def compareDates(catalog, medio):
    medios = catalog["medios"]
    med = mp.get(medios, medio)["value"]
    mg.sort(med, compareDate)
