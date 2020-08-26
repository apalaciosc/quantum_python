class Terrestre():
    def __init__(self):
        pass

    def desplazar(self):
        print('El animal está caminando.')

class Acuatico():
    def __init__(self):
        pass

    def desplazar(self):
        print('El animal está nadando.')

    def saludar(self):
        print('El animal saluda.')

class Cocodrilo(Acuatico, Terrestre):
    def __init__(self):
        pass

coco = Cocodrilo()
coco.desplazar()
coco.saludar()
