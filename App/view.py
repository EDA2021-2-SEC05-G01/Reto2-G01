﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
import sys
import controller
from DISClib.ADT import list as lt
assert cf
from DISClib.ADT import map as mp


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""


# FUNCIONES PARA LA IMPRESIÓN DE RESULTADOS

def printcornarttist(retorno, anio1, anio2):
    size = lt.size(retorno)
    print("\nLa cantidad de artistas que nacieron entre " + str(anio1) + " y "
        + str(anio2) + " es: " + str(size))
    print("Muestra de los artistas nacidos en este rango: ")
    if size:
        i = 1
        nw = lt.newList()
        while i <= 3:
            lt.addLast(nw, lt.getElement(retorno, i))
            i += 1
        i = size - 2
        while i <= size:
            lt.addLast(nw, lt.getElement(retorno, i))
            i += 1
        for x in lt.iterator(nw):
            print("\n Nombre: " + x["DisplayName"] + "\n Año de Nacimiento: " + x["BeginDate"] + 
                "\n Año de Fallecimiento: " + x["EndDate"] + "\n Nacionalidad: " + x["Nationality"]
                + "\n Género: " + x["Gender"] + "\n")
    else:
        print("No se encontraron artistas en este rango de fechas")




def printMenu():
    print("\nBienvenido")
    print("1- Inicializar el catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Buscar a los autores nacidos en un rango de años")
    print("Lab 6 \n4- Contar el número total de obras de una Nacionalidad")
    print("0- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        catalog = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(catalog)
        print("\nObras Cargadas: " + str(lt.size(catalog["artworks"])))
        print("Artistas Cargados: " + str(lt.size(catalog["artists"])))
        print("Años Cargados: " + str(mp.size(catalog["artistDate"])))
        print("Medios Cargados: " + str(mp.size(catalog["medios"])))
        print("C ids caragados: " + str(mp.size(catalog["Cids"])))
        print("Nacionalidades cargadas: " + str(mp.size(catalog["nacionalidad"])))

    elif int(inputs[0]) == 3:
        anio1 = int(input("Ingrese el año inicial a consultar: \n"))
        anio2 = int(input("Ingrese el año final a consultar: \n"))
        retorno = controller.cronartist(catalog, anio1, anio2)
        printcornarttist(retorno, anio1, anio2)
        
    elif int(inputs[0]) == 4:
        nac = input("Ingrese la nacionalidad a consultar: \n")
        print("La cantidad de obras de la nacionalidad " + nac + 
                ": " + str(lt.size(mp.get(catalog["nacionalidad"], nac)['value'])))
        
    else:
        print("Cerrando aplicación... ")
        sys.exit(0)
sys.exit(0)
