from extrangeria import *


def test_lee_datos_extranjeria(datos):
    print( f"El total de tatos de extrangeria es: {len(datos)}")

def test_secciones_distritos_con_extranjeros_nacionalidades(registros, paises):
    registros_paises = secciones_distritos_con_extranjeros_nacionalidades(registros, paises)
    print(f"los tregistros de los paises {paises} son un total de: {len(registros_paises)}")
    print(registros_paises[:5])

def test_total_extranjeros_por_pais(registros):
    print(total_extranjeros_por_pais(registros))

def test_barrio_mas_multicultural(registros):
    resultado = barrio_mas_multicultural(registros)
    print("TEST DE LA FUNCIÓN barrio_mas_multicultural:")
    print(f"El barrio más multicultural de sevilla es {resultado}")
    print("##############################################################")

def test_barrio_con_mas_extranjeros(registros, tipo= None):
    resultado = barrio_con_mas_extranjeros(registros, tipo)
    print("TEST DE LA FUNCIÓN barrio_con_mas_extranjeros:")
    print(f"El barrio con más residentes extranjeros es {resultado}.")
    print(f"El barrio con más hombres residentes extranjeros es {resultado}.")
    print(f"El barrio con más mujeres residentes extranjeras es {resultado}.")
    print(f"##############################################################")

def test_pais_mas_representado_por_distrito(registros):
    resultado = pais_mas_representado_por_distrito(registros)
    print("TEST DE LA FUNCIÓN pais_mas_representado_por_distrito:")
    print("Los países con más residentes en cada distrito son los siguientes:")
    for clave, valor in resultado.items():
        print(f"Distrito: {clave} => {valor}")
    
    print("##############################################################")


if __name__ == "__main__":
    datos = lee_datos_extranjeria("LAB-Extranjeria\data\extranjeriaSevilla.csv")
    #test_lee_datos_extranjeria(datos)
    #test_secciones_distritos_con_extranjeros_nacionalidades(datos, ["ALEMANIA","ITALIA"])
    #test_barrio_mas_multicultural(datos)
    #test_barrio_con_mas_extranjeros(datos, tipo= None)
    #test_barrio_con_mas_extranjeros(datos, tipo= "Hombres")
    #test_barrio_con_mas_extranjeros(datos, tipo= "Mujeres")
    test_pais_mas_representado_por_distrito(datos)
