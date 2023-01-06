import random

def run():
    numero_ganador = random.randint(1,100)
    numero_usuario = int(input('Ingrese un número entre el 1 y el 100: '))
    contador = 10
    while (numero_ganador != numero_usuario) and (contador-1 >= 0):
        if numero_usuario < numero_ganador:
            print('El numero es mas grande')
            numero_usuario = int(input('Ingrese otro numero: '))
        elif numero_usuario > numero_ganador:
            print('El numero es mas chico')
            numero_usuario = int(input('Ingrese otro numero: '))
        contador -= 1
    
    if contador <= 0:
        print ('Se acabaron tus vidas')
    else:
        print('Felicidades, ganaste')


if __name__=='__main__':
    run()