def add_taxes(item):
  #Para arreglar que no modifique al array original, crea una copia y modifica la copia.
  new_item = item.copy()
  new_item['taxes'] = new_item['price'] * 0.16
  return item


def run():
  items = [{
    'product': 'camisa',
    'price': 100
  }, {
    'product': 'pantalones',
    'price': 300
  }, {
    'product': 'falda',
    'price': 200
  }]

  #Aqui Map no modifica el array original
  prices = list(map(lambda item: item['price'], items))
  print(prices)

  #Aqui map realiza modificacion del array original
  new_items = list(map(add_taxes, items))
  print(new_items)


if __name__ == '__main__':
  run()