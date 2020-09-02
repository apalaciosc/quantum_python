def obtener_numero_turco(numero):
    numeros = {
        '0': 'sıfır',
        '1': 'bir',
        '2': 'iki',
        '3': 'üç',
        '4': 'dört',
        '5': 'beş',
        '6': 'altı',
        '7': 'yedi',
        '8': 'sekiz',
        '9': 'dokuz',
        '10': 'on',
        '20': 'yirmi',
        '30': 'otuz',
        '40': 'kırk',
        '50': 'elli',
        '60': 'altmış',
        '70': 'yetmiş',
        '80': 'seksen',
        '90': 'doksan'
    }
    num = str(numero)
    if numero >= 10 and numero % 10 != 0:
        primera_llave = f'{num[0]}0'
        primer_numero = numeros[primera_llave]
        ultima_llave = f'{num[1]}'
        segundo_numero = numeros[ultima_llave]
        resultado = f'{primer_numero} {segundo_numero}'
    else:
        numero = numeros[num]
        resultado = str(numero)

    return resultado


print(obtener_numero_turco(1))
print(obtener_numero_turco(13))
print(obtener_numero_turco(27))
print(obtener_numero_turco(38))
print(obtener_numero_turco(77))
print(obtener_numero_turco(94))
