def run():
    set_countries = {'col','mex','bol'}
    print(set_countries)
    print(type(set_countries))

    set_numbers = {1, 2, 2, 3, 443, 23}
    print(set_numbers)

    set_types = {1, 'hola', False, 12.12} #Forma explicita
    print(set_types)

    set_from_string = set('hola') #Forma implicita}
    print(set_from_string)
    

if __name__=='__main__':
    run()
