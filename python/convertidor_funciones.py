def convertir_moneda(tipo_pesos, valor):
    pesos = float(input("¿Cuantos pesos "+tipo_pesos+" tienes?: "))
    dolares = pesos / valor
    dolares = round(dolares,3)
    dolares = str(dolares)
    print("Usted tiene $" + dolares + " dolares")
    #return dolares


menu = """
Bienvenido al conversor de monedas $$ =D

1.- Pesos colombianos
2.- Pesos argentinos
3.- Pesos mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    convertir_moneda("pesos colombianos",3875)
elif opcion == 2:
    convertir_moneda("pesos argentinos",65)
elif opcion == 3:
    convertir_moneda("pesos mexicanos",20.75)
else:
     print("Ingrese una opción correcta")