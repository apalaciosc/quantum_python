def imprime_impares():
    contador = 0
    for i in range(101):
        if i % 2 != 0:
            contador += 1
            print(i)
    print(f'El número de impares es: {contador}')

imprime_impares()