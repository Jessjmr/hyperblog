import functools


#Suma es la suma de los valores anteriores
def accum(suma,item):
  print('suma ==> ',suma)
  print('item ==> ',item)
  return suma + item


def run():
  numbers = [1, 2, 3, 4]
  result = functools.reduce(accum, numbers)
  print(result)


if __name__=='__main__':
  run()