class Carro():
	def __init__(self, color, marca, anio):
		self.color = color
		self.marca = marca
		self.anio = anio

	def avanzar(self):
		print(f'Mi auto de color: {self.color} está avanzando')


auto_1 = Carro('rojo', 'Toyota', '2000')
auto_2 = Carro('negro', 'Hunday', '2010')
auto_3 = Carro('plomo', 'Toyota', '1990')
auto_1.avanzar()
auto_2.avanzar()
auto_3.avanzar()
