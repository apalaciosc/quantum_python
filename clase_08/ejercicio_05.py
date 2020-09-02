# ['i', 'have', 'no', 'space']
# ['i', 'ihave', 'ihaveno', 'ihavenospace']

# ['i', 'ihave', 'ihaveno', 'ihavenospace']
# ['Hola', 'Holaalumnos', 'Holaalumnosde', 'Holaalumnosdequantum', 'Holaalumnosdequantumspace']


def espacios(lista):
    palabra = ''
    resultado = []
    for i in lista:
        palabra += i
        resultado.append(palabra)
    print(resultado)

espacios(['i', 'have', 'no', 'space'])
espacios(['Hola', 'alumnos', 'de', 'quantum', 'space'])
