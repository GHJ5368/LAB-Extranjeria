from collections import namedtuple
from collections import defaultdict
import csv

RegistroExtranjeria = namedtuple('RegistroExtranjeria', 'distrito,seccion,barrio,pais,hombres,mujeres')

def lee_datos_extranjeria(ruta_fichero):
    res =[]

    with open(ruta_fichero, "r", encoding="utf-8") as f:
        lector = csv.reader(f)
        next(lector)
        for  distrito,seccion,barrio,pais,hombres,mujeres in lector:
            hombres= int(hombres)
            mujeres= int(mujeres)

            res.append( RegistroExtranjeria(distrito.strip(),seccion.strip(),barrio.strip(),pais.strip(),hombres,mujeres) )
    
    return res


def secciones_distritos_con_extranjeros_nacionalidades(registros, paises):
    res = set()
    for r in registros:
        if r.pais in paises:
            res.add(  (r.distrito, r.seccion) )
    
    return sorted(res)
    # Si ordenamos por seccion: sorted(res, key= lambda x:x[1])

def total_extranjeros_por_pais(registros):
    res = dict()
    for r in registros:
        if r.pais in res:
            res[r.pais] += r.hombres + r.mujeres
        else:
            res[r.pais] = r.hombres + r.mujeres

    return sorted(res.items(), key= lambda x:x[1], reverse=True)

def top_n_extranjeria(registros, n=3):
    extrangeros_por_pais = total_extranjeros_por_pais(registros)
    return extrangeros_por_pais[:n]

def total_paises_por_barrio(registros):
    res = defaultdict(set)
    for r in registros:
        res[r.barrio].add(r.pais)
    '''
    si fuera un diccionario normal:

    if r.pais in res:
        res[r.barrio].add(r.pais)
    else:
        res[r.barrio] = set( [r.pais] )
    '''

    return res

def barrio_mas_multicultural(registros): 
    paises_por_barrio = total_paises_por_barrio(registros)
    
    return max( paises_por_barrio.items(), key= lambda x: len(x[1]) )[0]
    # return max( paises_por_barrio, key= lambda x: len( paises_por_barrio.get(x) ) )

def barrio_con_mas_extranjeros(registros, tipo=None):
    res = defaultdict(int)
    
    for r in registros:
    
        if tipo is None:
            res[r.barrio] += r.hombres + r.mujeres

        elif tipo.lower() == "hombres":
            res[r.barrio] += r.hombres 
        
        elif tipo.lower() == "mujeres":
            res[r.barrio] += r.mujeres
    
    '''

    ########## OTRA FORMA ##########

    if tipo is None:
        
        for r in registros:
            res[r.barrio] += r.hombres + r.mujeres
    
    elif tipo.lower() == "Hombres":
        
        for r in registros:
            res[r.barrio] += r.hombres 
    
    elif tipo.lower() == "Mujeres":
        
        for r in registros:
            res[r.barrio] += r.mujeres
    '''
    return max( res, key= lambda x: res.get(x) )
    
def registros_por_distrito(registros):
    res = defaultdict(list)
    for r in registros:
        res[r.distrito].append(r)

    return res

def pais_mas_representado_por_distrito(registros):
    registros_agrupados = registros_por_distrito(registros)
    resultado = defaultdict(str)

    for clave, valor in registros_agrupados.items():
        pais = max(total_extranjeros_por_pais(valor), key= lambda x: x[1])[0]
        resultado[clave] = pais

    return resultado


