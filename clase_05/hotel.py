class Hotel():
    def __init__(self, numero_maximo_de_huespedes, lugares_de_estacionamiento):
        self.numero_maximo_de_huespedes = numero_maximo_de_huespedes
        self.lugares_de_estacionamiento = lugares_de_estacionamiento
        self.huespedes = 0

    def anadir_huespedes(self, cantidad_de_huespedes):
        self.huespedes += cantidad_de_huespedes

    def checkout(self, cantidad_de_huespedes):
        self.huespedes -= cantidad_de_huespedes

    def ocupacion_total(self):
        return self.huespedes

hotel_ica = Hotel(numero_maximo_de_huespedes=50, lugares_de_estacionamiento=2)
print(f'El número de huespedes es: {hotel_ica.ocupacion_total()}')
hotel_ica.anadir_huespedes(50)
print(f'El número de huespedes es: {hotel_ica.ocupacion_total()}')
hotel_ica.checkout(30)
print(f'El número de huespedes es: {hotel_ica.ocupacion_total()}')

# print(hotel_ica.numero_maximo_de_huespedes)
# print(hotel_ica.lugares_de_estacionamiento)
