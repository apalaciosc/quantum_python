class Automovil():
    def __init__(self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        self._estado = 'en reposo'
        self._motor = Motor(cilindros=4, tipo='gas')

    def acelerar(self, tipo='despacio'):
        if tipo == 'despacio':
            self._motor.inyecta_gasolina(3)
        else:
            self._motor.inyecta_gasolina(10)
        self._estado = 'en movimiento'

    def frenar(self):
        self._estado = 'en reposo'

class Motor():
    def __init__(self, cilindros, tipo='gasolina'):
        self.cilindros = cilindros
        self.tipo = tipo
        self._temperatura = 0
        self.gasolina = 0

    def inyecta_gasolina(self, gasolina):
        self.gasolina += gasolina


auto_1 = Automovil('Modelo X', 'Toyota', 'Amarillo')
auto_1.acelerar('rapida')
print(auto_1._estado)
print(auto_1._motor.gasolina)
auto_1.frenar()
print(auto_1._estado)
print(auto_1._motor.tipo)

# print(auto_1.modelo)
# print(auto_1.marca)
# print(auto_1.color)
# print(auto_1._motor.tipo)
