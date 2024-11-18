from collections import namedtuple
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