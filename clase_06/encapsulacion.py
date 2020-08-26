class Coordenada():
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y
    @property
    def x(self):
        return self._x
    @x.setter
    def x(self, coor_x):
        if coor_x < 0:
            raise ValueError('No es una coordenada válida para X')
        else:
            self._x = coor_x
    @property
    def y(self):
        return self._y
    @y.setter
    def y(self, coor_y):
        if coor_y < 0:
            raise ValueError('No es una coordenada válida para Y')
        else:
            self._y = coor_y
    def distance(self, coor):
        if isinstance(coor, Coordenada):
            res_x = (self._x + coor.x)** 2
            res_y = (self._y + coor.y)** 2
            resultado = (res_x + res_y)** 1 / 2
            return resultado
        raise ValueError('No es una coordenada válida.')

coord_1 = Coordenada()
coord_1.x = 1
coord_1.y = 1
print(coord_1.x)
print(coord_1.y)

coord_2 = Coordenada()
coord_2.x = 50
coord_2.y = 10
print(coord_2.x)
print(coord_2.y)
print(coord_1.distance(coord_2))
