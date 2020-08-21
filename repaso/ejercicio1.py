# Realizar la tabla de multiplicar de un numero entre 0 y 10.
def tabla_multiplicar(numero):
    if numero >= 0 and numero <= 10:
        print(f'Tabla del {numero}')
        for i in range(13):
            print(i * numero)
    else:
        print('Número incorrecto. Debes ingresar un número del 0 al 10')

numero = int(input('Ingresa un número: '))
tabla_multiplicar(numero)
