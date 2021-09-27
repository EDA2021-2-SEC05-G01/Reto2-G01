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

def printtopn(retorno):
    size = lt.size(retorno)
    if size:
        for obras in lt.iterator(retorno):
            print("Título: " + str(obras["Title"]) + "\n Date: " + str(obras["Date"]) + "\n"
            )
    else:
        print("No se encontró el medio solicitado o no hay suficientes obras para hacer el top")




def printMenu():
    print("Bienvenido")
    print("1- Inicializar el catálogo")
    print("2- Cargar información en el catálogo")
    print("3- La n obras más antiguas para un medio específico")
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
        print("Obras Cargadas: " + str(lt.size(catalog["artworks"])))
        print("Medios Cargados: " + str(mp.size(catalog["medios"])))
    elif int(inputs[0]) == 3:
        medio = input("Ingrese el medio a consultar: \n")
        top = int(input("Ingrese el top ? a consultar: \n"))
        retorno = controller.topnantiguas(catalog, medio, top)
        printtopn(retorno)
    else:
        sys.exit(0)
sys.exit(0)
