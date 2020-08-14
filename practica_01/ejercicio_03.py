def speed(velocidad):
	resultado = int(velocidad * 27.7778)
	print(f'El resultado es: {resultado}')


velocidad = float(input('Ingresa la velocidad en KM/Hora: '))
speed(velocidad)