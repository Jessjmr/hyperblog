def ciclo_potencia (potencia,base):
    contador = 0
    while contador <= potencia:
        potencia_base = base**contador
        print (f'{base} elevado a la {contador} es: {potencia_base}')
        #print (str(base)+' elevado a la ' + str(contador) + ' es: ' + str(potencia_base))
        contador += 1


def run():
    base = int(input('Ingrese una base: '))
    potencia = int(input('Ingrese una potencia: '))
    ciclo_potencia(potencia,base)
    

if __name__ == '__main__':
    run()