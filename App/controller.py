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
    loaddNacionality(catalog)


def loadArtworks(catalog):
    """
    Carga los libros del archivo.  Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """
    artfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(artfile, encoding='utf-8'))
    for obra in input_file:
        model.AddArtworks(catalog, obra)

def loadArtists(catalog):
    """
    Carga los libros del archivo.  Por cada libro se indica al
    modelo que debe adicionarlo al catalogo.
    """
    artfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(artfile, encoding='utf-8'))
    for artist in input_file:
        model.AddArtists(catalog, artist)

def loaddNacionality(catalog):
    model.nacionality(catalog)

# Funciones de ordenamiento

def compareDates(catalog, medio):
    model.compareDates(catalog, medio)
    return catalog

# Funciones de consulta sobre el catálogo

def cronartist(catalog, anio1, anio2):
    model.compareArtistsDates(catalog)
    retorno = model.cronartist(catalog, anio1, anio2)
    return retorno
