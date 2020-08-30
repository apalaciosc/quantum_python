def espacios(lista):
    palabra = ''
    resultado = []
    for i in lista:
        palabra += i
        resultado.append(palabra)
    print(resultado)

espacios(['i', 'have', 'no', 'space'])

# ['i', 'have', 'no', 'space']
# ['i', 'ihave', 'ihaveno', 'ihavenospace']

