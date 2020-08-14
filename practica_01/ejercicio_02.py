def area_or_perimeter(longitud, ancho):
    if longitud == ancho:
        area = longitud ** 2
        print(f'El area del cuadrado es: {area}')
    else:
        perimetro = longitud + ancho + longitud + ancho
        print(f'El perimetro del rectangulo es: {perimetro}')

longitud = float(input('Ingresa la longitud: '))
ancho = float(input('Ingresa el ancho: '))
area_or_perimeter(longitud, ancho)
