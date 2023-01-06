eleccion = int(input("Seleccione 1 para pasar de pesos mexicanos a dolares y 2 para pasar de dolares a pesos mexicanos: "))
if eleccion == 1:
    pesos_mexicanos = float(input("¿Cuantos pesos mexicanos tienes?: "))
    valor_dolar = 20.75
    dolares = pesos_mexicanos / valor_dolar
    dolares = round(dolares,3)
    dolares = str(dolares)
    print("Usted tiene $" + dolares + " dolares")
if eleccion == 2:
    dolares = float(input("¿Cuantos dolares tienes?: "))
    valor_peso_mexicano = 20.75
    peso_mexicano = dolares * valor_peso_mexicano
    peso_mexicano = round(peso_mexicano,3)
    peso_mexicano = str(peso_mexicano)
    print("Usted tiene $" + peso_mexicano + " pesos mexicanos")