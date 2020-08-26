def devolver_lista_pares(cadena):
    if len(cadena) < 2 or len(cadena) > 100:
        print('Cadena no válida')
    else:
        lista = []
        c = 1
        for i in cadena:
            if c % 2 == 0:
                lista.append(i)
            c += 1
        print(lista)


cadena = input('Escribe una palabra: ')
devolver_lista_pares(cadena)

