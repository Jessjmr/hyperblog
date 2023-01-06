import random


def run():
    ## Listas forma clásica
    numbers = []

    for element in range(1,101):
        if element % 2 == 0:
            numbers.append(element)
    
    #print(numbers)

    ## Lista forma comprehensions

    numbers_v2 = [i for i in range(1,101) if i % 2 == 0] #Sintaxis mas corta y rapida
    #print(numbers_v2)

    days = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']

    days_v2 = [dias for dias in days if dias == 'lunes' or dias == 'viernes']
    #print (days_v2)

    ### Diccionario forma clasica

    dict = {}

    for i in range(1,11):
        dict[i] = i * 2
    
    #print (dict)

    ## Diccionario forma comprehension
    
    dict_v2 = {i : i*2 for i in range(1,11)}
    #print(dict_v2)

    horas = {}

    for dias in days:
        horas[dias] = random.randint(1,8)
    
    print(horas)

    horas_v2 = {dias:random.randint(1,8) for dias in days}
    print(horas_v2)

    names = ['nico', 'zule', 'santi']
    ages = [12, 56, 98]

    #Union de listas
    list_names_ages = list(zip(names,ages))

    #Sin usar union de listas
    new_dict = {names[i] : ages[i] for i in range(len(names))}
    print(new_dict)

    #Usando union de listas
    new_dict_2 = {name:age for (name,age) in zip(names,ages)}
    print(new_dict_2)


if __name__=='__main__':
    run()
