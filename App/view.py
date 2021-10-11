"""
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

def printgetmediums(catalog, medios, autor):
    obras = lt.size(mp.get(catalog["artists"], autor)['value'])
    size = mp.size(medios)
    if obras:
        print("\n" + autor + " tiene " + str(obras) + " obras en el museo")
        print(autor + " usa " + str(size) + " técnicas en estas obras.")
        mayor = controller.mayor(medios)
        print('\nLa técnica más usada por ' + autor + ' es: ' + str(mayor) + ' con ' + str(lt.size(mp.get(medios, mayor)['value'])) + ' obras.')
        lista = lt.newList("ARRAY_LIST")
        i = 1
        mayor = mp.get(medios, mayor)['value']
        controller.compareDates(mayor)
        while i <= 3:
            x = lt.getElement(mayor, i)
            lt.addLast(lista, x)
            i += 1
        i = 1
        while i <= 3:
            x = lt.lastElement(mayor)
            lt.addLast(lista, x)
            lt.removeLast(mayor)
            i += 1
        for art in lt.iterator(lista):
            print('\nTítulo: ' + art["Title"] + '\nFecha de la obra: ' + art["Date"] + 
                    '\nTécnica: ' + art["Medium"] + '\nDimensiones: ' + art["Dimensions"])
    else:
        print("No se encontraron obras de ese autor")


def printMenu():
    print("\nBienvenido")
    print("1- Inicializar y cargar información el catálogo")
    print("2- Consultar a los autores nacidos en un rango de años")
    print("3- Consultar las obras adquiridas en un rango de fechas")
    print("4- Clasificar las obras de un artista por técnica")
    print("5- Clasificar las obras por la nacionalidad de sus creadores")
    print("6- Calcular costo de tranporte de un departamento")
    print("0- Salir")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("\nInicializando Catálogo ....")
        catalog = controller.initCatalog()
        print("\nCargando información de los archivos ....")
        controller.loadData(catalog)
        print("\nObras Cargadas: " + str(lt.size(catalog["artworks"])))
        print("Artistas Cargados: " + str(mp.size(catalog["artists"])))
        print("Años Cargados: " + str(mp.size(catalog["artistDate"])))
        print("Técnicas Cargadas: " + str(mp.size(catalog["medios"])))
        print("Nacionalidades cargadas: " + str(mp.size(catalog["nacionalidad"])))

    elif int(inputs[0]) == 2:
        anio1 = int(input("Ingrese el año inicial a consultar: \n"))
        anio2 = int(input("Ingrese el año final a consultar: \n"))
        retorno = controller.cronartist(catalog, anio1, anio2)
        printcornarttist(retorno, anio1, anio2)
        
    elif int(inputs[0]) == 3:
        pass
    
    elif int(inputs[0]) == 4:
        autor = input('\nIngrese el nombre del Autor que desea consultar:\n')
        medios = controller.getmediums(catalog, autor)
        printgetmediums(catalog, medios, autor)
    else:
        print("Cerrando aplicación... ")
        sys.exit(0)
sys.exit(0)
