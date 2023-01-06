def suma_con_rango(min,max):
    suma=0
    for i in range(min,max):
        suma += i
    return suma


def run():
    resultado1 = suma_con_rango(1,50)
    print(resultado1)
    resultado2 = suma_con_rango(resultado1,resultado1 * 2)
    print(resultado2)
    


if __name__=='__main__':
    run()