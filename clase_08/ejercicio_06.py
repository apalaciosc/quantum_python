# pluck([
#     {'a': 1}, {'a': 2}
# ], 'a')  # -> [1,2]

# pluck([
#     {'a': 1, 'b': 3},
#     {'a': 2}
# ], 'b') # -> [3, None]


def pluck(lista, llave):
    resultado = []
    for i in lista:
        if llave in i:
            resultado.append(i[llave])
        else:
            resultado.append(None)

    print(resultado)

pluck([{'a': 1}, {'a': 2}], 'a')  # -> [1,2]
pluck([{'a':1, 'b':3}, {'a':2}], 'b')  # -> [3, None]
