menu = """
Bienvenido al conversor de monedas $$ =D

1.- Pesos colombianos
2.- Pesos argentinos
3.- Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    pesos_colombianos = float(input("¿Cuantos pesos colombianos tienes?: "))
    valor_dolar = 3875
    dolares = pesos_colombianos / valor_dolar
    dolares = round(dolares,3)
    dolares = str(dolares)
    print("Usted tiene $" + dolares + " dolares")
elif opcion == 2:
    pesos_argentinos = float(input("¿Cuantos pesos argentinos tienes?: "))
    valor_dolar = 65
    dolares = pesos_argentinos / valor_dolar
    dolares = round(dolares,3)
    dolares = str(dolares)
    print("Usted tiene $" + dolares + " dolares")
elif opcion == 3:
    pesos_mexicanos = float(input("¿Cuantos pesos mexicanos tienes?: "))
    valor_dolar = 20.75
    dolares = pesos_mexicanos / valor_dolar
    dolares = round(dolares,3)
    dolares = str(dolares)
    print("Usted tiene $" + dolares + " dolares")
else:
    print("Ingrese una opción correcta")