def pluck(objetos, propiedad):
    resultado = []
    for objeto in objetos:
        if propiedad in objeto:
            resultado.append(objeto[propiedad])
        else:
            resultado.append(None)
    print(resultado)

print('Prueba 1')
pluck([{'a':1}, {'a':2}], 'a')

print('Prueba 2')
pluck([{'a':1, 'b':3}, {'a':2}], 'b')
