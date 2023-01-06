def message_creator(text):
    text = text.lower()
    if text == 'computadora':
        text_response = 'Con mi computadora puedo programar usando Python'
    elif text == 'celular':
        text_response = 'En mi celular puedo aprender usando la app de Platzi'
    elif text == 'cable':
        text_response = '¡Hay un cable en mi bota!'
    else:
        text_response = 'Artículo no encontrado'
    return text_response 

text = 'cable'
response = message_creator(text)
print(response)