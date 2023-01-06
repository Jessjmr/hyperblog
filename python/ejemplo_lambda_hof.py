#def increment (x):
#  return x + 1

#def hof(x,func):
#  return x + func(x)


def run():

  #Version lambda de la funcion increment que esta arriba
  #increment = lambda x : x + 1
  
  hof = lambda x,func : x + func(x)
  result = hof(2,lambda x : x + 1)
  print(result)


if __name__=='__main__':
  run()