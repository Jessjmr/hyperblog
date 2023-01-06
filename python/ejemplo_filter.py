def run():
  numbers = [1, 2, 3, 4, 5, 6]

  pares_f = list(filter(lambda i:i%2 == 0,numbers))
  pares_bool = list(map(lambda i:i%2 == 0,numbers))

  print(pares_f)
  print(pares_bool)


if __name__=='__main__':
  run()