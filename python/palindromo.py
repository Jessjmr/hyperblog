def palindromo (palabra):
    palabra = palabra.lower().replace(' ','')
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False

def run():
    palabra = input("Ingrese una palabra: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print ("La palabra " + palabra + " es palindromo")
    else:
        print ("La palabra " + palabra + " no es palindromo")


if __name__ == '__main__':
    run()
