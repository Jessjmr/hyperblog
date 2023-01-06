def run():
  try:
    print (0/0)
    assert 1 != 1, 'Uno no es igual que uno'
  except ZeroDivisionError as error:
      print(error)
  except AssertionError as error:
    print(error)

  age = 18
  if age < 18:
      raise Exception('No se permiten menores de edad')

      


if __name__=='__main__':
  run()
