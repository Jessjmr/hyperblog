import random

def run():
    days = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
    horas = {dias : random.randint(1,8) for dias in days}
    print(horas)

    resultado = {dia : hora for (dia,hora) in horas.items() if hora >= 4 }
    print(resultado)

    text = 'Hola, mi nombre es Jessica'
    unique = {c: text.count(c) for c in text if c in 'aeiou'}
    print(unique)


if __name__=='__main__':
    run()