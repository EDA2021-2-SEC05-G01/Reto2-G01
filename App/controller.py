"""
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
 """

import config as cf
import model
import csv
from time import process_time


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de Obras.

def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    catalog = model.newCatalog()
    return catalog


# Funciones para la carga de datos

def loadData(catalog):
    """
    Carga los datos de los archivos y cargar los datos en la
    estructura de datos
    """
    loadArtists(catalog)
    loadArtworks(catalog)


def loadArtworks(catalog):
    """
    Carga las obras del museo.
    """
    artfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artfile, encoding='utf-8'))
    for obra in input_file:
        model.AddArtworks(catalog, obra)

def loadArtists(catalog):
    """
    Carga los artistas de las obras.
    """
    artfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artfile, encoding='utf-8'))
    for artist in input_file:
        model.AddArtists(catalog, artist)


# Funciones de ordenamiento

def compareDates(medios):
    model.compareDates(medios)
    return medios

def mayor(obras):
    o = model.mayor(obras)
    return o

# Funciones de consulta sobre el catálogo

def cronartist(catalog, anio1, anio2):
    model.compareArtistsDates(catalog)
    retorno = model.cronartist(catalog, anio1, anio2)
    return retorno

def comparedateacquired(catalog, finc, ffin):
    retorno = model.comparedateacquired(catalog, finc, ffin)
    return retorno

def getmediums(catalog, autor):
    medios = model.getmediums(catalog, autor)
    return medios

def calculartransporte(catalog, departamento):
    mapa = model.calculartransporte(catalog, departamento)
    return mapa

def obtenerPorNacionalidad(catalog):
    return model.getNacion(catalog)

