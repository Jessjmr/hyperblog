def es_primo(numero):
    factorial_numero = 1
    for i in range(1,numero):
        factorial_numero = i * factorial_numero
    teorema_wilson = factorial_numero + 1
    if teorema_wilson % numero == 0:
        print ("Es primo")
    else:
        print ("No es primo")

def run():
    numero = int(input('Ingrese un número: '))
    es_primo(numero)


if __name__=='__main__':
    run()