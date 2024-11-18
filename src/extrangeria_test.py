from extrangeria import *


def test_lee_datos_extranjeria(datos):
    print( f"El total de tatos de extrangeria es: {len(datos)}")

def test_secciones_distritos_con_extranjeros_nacionalidades(registros, paises):
    registros_paises = secciones_distritos_con_extranjeros_nacionalidades(registros, paises)
    print(f"los tregistros de los paises {paises} son un total de: {len(registros_paises)}")
    print(registros_paises[:5])

def test_total_extranjeros_por_pais(registros):
    print(total_extranjeros_por_pais(registros))


if __name__ == "__main__":
    datos = lee_datos_extranjeria("LAB-Extranjeria\data\extranjeriaSevilla.csv")
    #test_lee_datos_extranjeria(datos)
    test_secciones_distritos_con_extranjeros_nacionalidades(datos, ["ALEMANIA","ITALIA"])

