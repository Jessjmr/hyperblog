def imprimir_mensaje(opcion):
    print("Hola")
    print("Como estas")
    print("Eligiste la opción"+" "+opcion)
    print("Adios")

menu = """ Bienvenido. Elige una opción (1,2,3): """

opcion = input(menu)

if opcion == "1":
    imprimir_mensaje(opcion)
elif opcion == "2":
    imprimir_mensaje(opcion)
elif opcion == "3":
    imprimir_mensaje(opcion)
else:
    print("Escribe la opción correcta")