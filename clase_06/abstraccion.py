class Lavadora():
    def __init__(self):
        pass

    def lavar(self, temperatura='fria'):
        self._llenar_tanque_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()
        print('FIN.')

    def _llenar_tanque_agua(self, temperatura):
        print(f'Llenando el tanque con agua: {temperatura}')

    def _anadir_jabon(self):
        print('Añadiendo jabón a la lavadora.')

    def _lavar(self):
        print('Lavando la ropa...')

    def _centrifugar(self):
        print('Centrifugando')

lavadora = Lavadora()
lavadora.lavar()
