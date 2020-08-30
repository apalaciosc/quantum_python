# 1|    |12
# 3|   |10
# 4|   |8
# 7|   |6
# 9|   |4
# 11|   |2

# 1|   |6
# 3|   |4
# 5|   |2


# [1, 3, 5]
# [2, 4, 6]

def over_the_road(numero_casa, longitud_calle):
    casas_izquierda = []
    casas_derecha = []
    c = 1
    while True:
        if c % 2 == 0:
            casas_derecha.append(c)
        else:
            casas_izquierda.append(c)

        if len(casas_derecha) == longitud_calle and len(casas_izquierda) == longitud_calle:
            break
        c += 1

    casas_derecha.sort(reverse=True)
    if numero_casa % 2 == 0:
        indice = casas_derecha.index(numero_casa)
        print(casas_izquierda[indice])
    else:
        indice = casas_izquierda.index(numero_casa)
        print(casas_derecha[indice])


over_the_road(1, 3) #  6
over_the_road(3, 3) #  4
over_the_road(2, 3) #  5
over_the_road(3, 5) #  8


