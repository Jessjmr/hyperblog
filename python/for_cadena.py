def recorrer(frase):
    for caracter in frase:
        print(caracter.upper())


def run():
    #nombre = input('Escribe tu nombre: ')
    #recorrer(nombre)
    frase = input('Escribe una frase: ')
    recorrer(frase)


if __name__=='__main__':
    run()