def imprimir_mensaje(opcion):
    print(
        f"""
        Hola
        Cómo estás?
        Elegiste la {opcion}
        Adios
    """
    )
    # print('Hola!')
    # print('Cómo estás?')
    # print(f'Elegiste la opción {opcion}')
    # print('Adios')

opcion = input('Ingresa tu opción: ')
if opcion == '1' or opcion == '2' or opcion == '3' or opcion == '4':
    imprimir_mensaje(opcion)
else:
    print('Opción incorrecta.')
