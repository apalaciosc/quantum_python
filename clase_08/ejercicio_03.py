def sumar(numero_1, numero_2):
    num1 = str(numero_1)
    num2 = str(numero_2)
    tamano_num1 = len(num1)
    tamano_num2 = len(num2)

    if tamano_num1 == tamano_num2:
        pass
    elif tamano_num1 > tamano_num2:
        diferencia = tamano_num1 - tamano_num2
        num2 = (diferencia * '0') + num2
    else:
        diferencia = tamano_num2 - tamano_num1
        num1 = (diferencia * '0') + num1

    nuevo_tamano = len(num1) - 1
    resultado = ''
    while nuevo_tamano >= 0:
        temp = 0
        temp = int(num1[nuevo_tamano]) + int(num2[nuevo_tamano])
        resultado = str(temp) + resultado
        nuevo_tamano -= 1

    print(int(resultado))

sumar(16, 18)
sumar(26, 39)
sumar(122, 81)