# 1|   |10
# 3|   |8
# 5|   |6
# 7|   |4
# 9|   |2

class Calle():
    def casas_izquierda(self):
        casas_izquierda = []
        c = 1
        while True:
            if c % 2 != 0:
                casas_izquierda.append(c)

            if len(casas_izquierda) == self.longitud:
                break
            c += 1
        return casas_izquierda

    def casas_derecha(self):
        casas_derecha = []
        c = 1

        while True:
            if c % 2 == 0:
                casas_derecha.append(c)

            if len(casas_derecha) == self.longitud:
                break
            c += 1

        casas_derecha.sort(reverse=True)
        return casas_derecha

    def __init__(self, longitud = 3):
        self.longitud = longitud
        self._casas_izquierda = self.casas_izquierda()
        self._casas_derecha = self.casas_derecha()

    def opuesto(self, numero_casa):
        if numero_casa % 2 == 0:
            indice_casa = self._casas_derecha.index(numero_casa)
            opuesto = self._casas_izquierda[indice_casa]
        else:
            indice_casa = self._casas_izquierda.index(numero_casa)
            opuesto = self._casas_derecha[indice_casa]

        print(opuesto)


calle_1 = Calle()
calle_2 = Calle(5)

calle_1.opuesto(1) # 6
calle_1.opuesto(3) # 4
calle_1.opuesto(2) # 5
calle_2.opuesto(3) # 8
