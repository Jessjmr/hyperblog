def find_volume(length=1, width=1 , depth=1):
    return length * width * depth , width, 'hola'


def run():
    result, w, text = find_volume(width=10,depth=2)
    print(result)
    print(w)
    print(text)


if __name__=='__main__':
    run()
