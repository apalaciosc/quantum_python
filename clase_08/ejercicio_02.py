# abc#d##c

def limpiar_cadena(cadena):
    lista = list(cadena)
    resultado = []
    if len(cadena) > 0:
        for i in lista:
            if i == '#':
                if len(resultado) > 0:
                    resultado.pop()
            else:
                resultado.append(i)

    cadena_final = ''.join(resultado)
    print(cadena_final)

limpiar_cadena("abc#d##c")
limpiar_cadena("abc##d######")
limpiar_cadena("#######")
limpiar_cadena("")
