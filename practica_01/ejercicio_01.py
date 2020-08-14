def hello(nombre):
    tamano_nombre = len(nombre)
    if tamano_nombre >= 1:
        print(f'Hola, {nombre}')
    else:
        print('Hola, mundo!')

nombre = input('Escribe tu nombre: ')
hello(nombre)
