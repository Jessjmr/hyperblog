def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3
    }
    print(mi_diccionario['llave1'])
    print(mi_diccionario['llave2'])
    print(mi_diccionario['llave3'])

    poblacion_paises = {
        'Argentina': 44_938_712,
        'Brasil': 210_147_125,
        'Colombia': 50_372_424
    }

    #for pais in poblacion_paises.keys():
    #    print(pais)
    
    #for poblacion in poblacion_paises.values():
    #    print(poblacion)

    for pais, poblacion in poblacion_paises.items():
        print(f'{pais} tiene {poblacion} habitantes')


if __name__=='__main__':
    run()