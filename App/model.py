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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


from DISClib.ADT.orderedmap import keySet
import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import mergesort as mg
from time import strptime
from time import process_time
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
               'medios': None,
               'artists': None,
               'cids': None,
               'cidname': None,
               'artistDate': None,
               'nacionalidad': None,
               'dates': None}

    catalog['artworks'] = lt.newList('SINGLE_LINKED', compareObjectIds)

    catalog['medios'] = mp.newMap(21251,
                                   maptype='CHAINING',
                                   loadfactor=2.0,
                                   comparefunction=compareMedium)

    catalog['artists'] = mp.newMap(15300,
                                   maptype='CHAINING',
                                   loadfactor=2.0,
                                   comparefunction=compareyear)

    catalog['artistDate'] = mp.newMap(15300,
                                   maptype='CHAINING',
                                   loadfactor=2.0,
                                   comparefunction=compareyear)

    catalog['nacionalidad'] = mp.newMap(130, 
                                    maptype='CHAINING',
                                    loadfactor=2.0,
                                    comparefunction=compareyear)

    catalog['cids'] = mp.newMap(15300,
                                   maptype='CHAINING',
                                   loadfactor=2.0,
                                   comparefunction=compareyear)
    
    catalog['cidname'] = mp.newMap(15300,
                                   maptype='CHAINING',
                                   loadfactor=2.0,
                                   comparefunction=compareyear)

    catalog['departamentos'] = mp.newMap(1000,
                                    maptype='CHAINING',
                                    loadfactor=2.0)

    catalog['dates'] = mp.newMap(1000,
                                    maptype='CHAINING',
                                    loadfactor=2.0)
    return catalog



# Funciones para agregar informacion al catalogo

def AddArtworks(catalog, artwork):
    lt.addLast(catalog['artworks'], artwork)
    addnacionality(catalog, artwork)
    addall(catalog, artwork)
    addartworksbyauthor(catalog, artwork)
    addname(catalog, artwork)
    addareas(catalog, artwork)

def AddArtists(catalog, artist):
    mp.put(catalog['artists'], artist["DisplayName"], lt.newList("ARRAY_LIST"))
    addlistyear(catalog, artist)
    addcids(catalog, artist)



def addlistyear(catalog, artist):
    years = catalog["artistDate"]
    if mp.contains(years, artist["BeginDate"]):
        lista = mp.get(years, artist["BeginDate"])["value"]
        lt.addLast(lista, artist)
        mp.put(years, artist["BeginDate"], lista)
    else:
        lst = lt.newList('ARRAY_LIST')
        lt.addLast(lst, artist)
        mp.put(years, artist["BeginDate"], lst)
    return catalog


def addnacionality(catalog, artwork):
    id = artwork["ConstituentID"]
    ids = catalog["cids"]
    nat = catalog['nacionalidad']
    pos = id.strip('[]').split(', ')
    size = len(pos)
    i = 0
    while i < size:
        nac = mp.get(ids, pos[i])['value']
        if mp.contains(nat, nac):
            g = mp.get(nat, nac)['value']
            lt.addLast(g, artwork)
            mp.put(nat, nac, g)
        else:
            lista = lt.newList("ARRAY_LIST")
            lt.addLast(lista, artwork)
            mp.put(nat, nac, lista)
        i +=1      
    return catalog


def addcids(catalog, artist):
    id = artist["ConstituentID"]
    mp.put(catalog['cids'], id, artist['Nationality'])
    mp.put(catalog['cidname'], id, artist['DisplayName'])
    return 


def addartworksbyauthor(catalog, artwork):
    idname = catalog['cidname']
    names = catalog['artists']
    ids = artwork['ConstituentID']
    pos = ids.strip('[]').split(', ')
    size = len(pos)
    i = 0
    while i < size:
        nombre = mp.get(idname, str(pos[i]))['value']
        g = mp.get(names, nombre)['value']
        lt.addLast(g, artwork)
        mp.put(names, nombre, g)
        i +=1   
    return catalog

def addall(catalog, art):
    dates = catalog['dates']
    dep = catalog["departamentos"]
    medios = catalog["medios"]

    if mp.contains(medios, art["Medium"]):
        lista = mp.get(medios, art["Medium"])["value"]
        lt.addLast(lista, art)
        mp.put(medios, art["Medium"], lista)
    else:
        lst = lt.newList('ARRAY_LIST')
        lt.addLast(lst, art)
        mp.put(medios, art["Medium"], lst)

    if mp.contains(dates, art['DateAcquired']):
        lista = mp.get(dates, art['DateAcquired'])['value']
        lt.addLast(lista, art)
        mp.put(dates, art["DateAcquired"], lista)
    else:
        lst = lt.newList('ARRAY_LIST')
        lt.addLast(lst, art)
        mp.put(dates, art["DateAcquired"], lst)

    if mp.contains(dep, art["Department"]):
        lista = mp.get(dep, art["Department"])["value"]
        lt.addLast(lista, art)
        mp.put(dep, art["Department"], lista)
    else:
        lst = lt.newList('ARRAY_LIST')
        lt.addLast(lst, art)
        mp.put(dep, art["Department"], lst)

    return catalog

def addname(catalog, artwork):
    idname = catalog['cidname']
    ids = artwork['ConstituentID']
    pos = ids.strip('[]').split(', ')
    i = 0
    names = ''
    for name in pos:
        names += ' ' + str(mp.get(idname, name)['value'])
    artwork['ConstituentID'] = names
    return catalog

def addareas(catalog, obra):
    if obra["Diameter (cm)"] != '':
        area = areacirculo(obra["Diameter (cm)"])
    elif obra["Depth (cm)"] != '' and obra["Depth (cm)"] != "0" and obra["Width (cm)"] != '' and obra["Width (cm)"] != "0" and obra["Height (cm)"] != '' and obra["Height (cm)"] != "0":
        area = areacubo(obra["Width (cm)"], obra["Height (cm)"], obra["Depth (cm)"])
    elif obra["Width (cm)"] != '' and obra["Width (cm)"] != "0" and obra["Height (cm)"] != '' and obra["Height (cm)"] != "0":
        area = areacuadrado(obra["Width (cm)"], obra["Height (cm)"])
    else:
        area = 0
    if obra['Weight (kg)'] != '':
        area = area + float(obra['Weight (kg)'])
    obra["area"] = area
    return catalog

# Funciones para creacion de dato

# Funciones de consulta

def comparedates(id, entry):
    identry = me.getKey(entry)
    if id == '' or identry == '':
        return  -1
    if (strptime(id, "%Y-%m-%d") == strptime(identry, "%Y-%m-%d")):
        return 0
    elif (strptime(id, "%Y-%m-%d") > strptime(identry, "%Y-%m-%d")):
        return 1
    else:
        return -1

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

def compareConstituentsID(id1, id2):
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


def compareyear(medio, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (medio == str(identry)):
        return 0
    else:
        return -1

def cronartist(catalog, anio1, anio2):
    years = catalog["artistDate"]
    i = int(anio1)
    lista = lt.newList()
    while i <= anio2:
        i = str(i)
        if mp.contains(years, i):
            med = mp.get(years, i)["value"]
            for n in lt.iterator(med):
                lt.addLast(lista, n)
        i = int(i) + 1
    return lista


def getmediums(catalog, autor):
    obras = mp.get(catalog["artists"], autor)['value']
    medios = mp.newMap(lt.size(obras)+3,
                        maptype='CHAINING',
                        loadfactor=2.0,
                        comparefunction=compareMedium)
    for art in lt.iterator(obras):
        if mp.contains(medios, art["Medium"]):
            lista = mp.get(medios, art["Medium"])['value']
            lt.addLast(lista, art)
            mp.put(medios, art["Medium"], lista)
        else:
            lista = lt.newList("ARRAY_LIST")
            lt.addLast(lista, art)
            mp.put(medios, art["Medium"], lista)

    return medios

def comparedateacquired(catalog, finc, ffin):
    finc = strptime(finc, "%Y-%m-%d")
    ffin = strptime(ffin, "%Y-%m-%d")
    key = mp.keySet(catalog['dates'])
    lst = lt.newList("ARRAY_LIST")
    purchase = 0
    for k in lt.iterator(key):
        if k != '' and strptime(k, "%Y-%m-%d") >= finc and strptime(k, "%Y-%m-%d") <= ffin:
            for n in lt.iterator(mp.get(catalog['dates'], k)['value']):
                lt.addLast(lst, n)
                if n["CreditLine"] == 'Purchase':
                    purchase += 1
    comparedates(lst)
    lt.addLast(lst, purchase)
    return lst


def calculartransporte(catalog, departamento):
    precio = 0
    mapa = mp.newMap(5, maptype="CHAINING", loadfactor=2.0)
    peso = 0
    if mp.contains(catalog['departamentos'], departamento):
        obras = mp.get(catalog['departamentos'], departamento)['value']
        for art in lt.iterator(obras):
            area = float(art['area'])
            pr = 0
            if area != 0:
                pr += area * 72
                precio += round(pr, 3)
            else:
                pr = 48
                precio += pr
            art['transporte'] = round(pr, 3)
            if art["Weight (kg)"] != "":
                peso += float(art["Weight (kg)"])
    mp.put(mapa, "peso", peso)
    mp.put(mapa, "precio", round(precio, 3))
    compareprecio(obras)
    ls = cincoprimeros(obras)
    mp.put(mapa, "costosas", ls)
    comparedates(obras)
    ls = cincoprimeros(obras)
    mp.put(mapa, "antiguas", ls)
    return mapa

# Funciones utilizadas para comparar elementos dentro de una lista

def compareDate(art1, art2):
    if art1['Date'] != '' and art2['Date'] != '':
        return float(art1['Date']) < float(art2['Date'])

def compareedates(art1, art2):
    if art1['DateAcquired'] != '' and art2['DateAcquired'] != '':
        return strptime(art1['DateAcquired'], "%Y-%m-%d") < strptime(art2['DateAcquired'], "%Y-%m-%d")


def compareArtistDate(art1, art2):
    return float(art1) < float(art2)

def mayor(medios):
    mayor = 0
    r = None
    for n in lt.iterator(mp.keySet(medios)):
        if lt.size(mp.get(medios, n)['value']) > mayor:
            mayor = lt.size(mp.get(medios, n)['value'])
            r = n
    return r

def compareprecios(obra1, obra2):
    return float(obra1['transporte']) > float(obra2['transporte'])


def cincoprimeros(lista):
    if lt.size(lista) > 5:
        i = 1
        lst = lt.newList("ARRAY_LIST")
        while i <= 5:
            x = lt.getElement(lista, i)
            lt.addLast(lst, x)
            i += 1
        return lst

    else:
        i = 1
        lst = lt.newList("ARRAY_LIST")
        while i <= lt.size(lista):
            x = lt.getElement(lista, i)
            lt.addLast(lst, x)
            i += 1
        return lst




# Funciones de ordenamiento


def compareDates(mayor):
    mg.sort(mayor, compareDate)

def compareArtistsDates(catalog):
    years = catalog["artistDate"]
    med = mp.keySet(years)
    mg.sort(med, compareArtistDate)

def comparedates(lst):
    mg.sort(lst, compareedates)

def compareprecio(lst):
    mg.sort(lst, compareprecios)


# Funciones de aritmática y cálculos

def areacirculo(diametro):
    diam = cmam(diametro)
    area = (3.1416)*((float(diam)/2)**2)
    return area

def areacuadrado(ancho, alto):
    anc = cmam(ancho)
    alt = cmam(alto)
    area = float(anc)*float(alt)
    return area

def areacubo(ancho, alto, profundidad):
    anc = cmam(ancho)
    alt = cmam(alto)
    pro = cmam(profundidad)
    area = float(anc)*float(alt)*float(pro)
    return area

def cmam(numero):
    numero = float(numero)
    m = numero/100
    return m