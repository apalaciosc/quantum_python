def convertir_moneda(tipo_de_cambio, moneda):
    monto = float(input(f'Hola, ingresa tu monto en {moneda}: '))
    monto_dolares = round(monto * tipo_de_cambio, 2)
    print(f'El monto en dólares es: {monto_dolares}')

mensaje = """
Hola, este es un conversor de monedas
Ingresa cualquier de estas 3 opciones:
1 = Soles - Dolares
2 = Euros - Dolares
3 = Pesos Colombianos - Dolares
"""

print(mensaje)
opcion = int(input('Ingresa la opción: '))
if opcion == 1:
    convertir_moneda(0.28, 'soles')
elif opcion == 2:
    convertir_moneda(1.19, 'euros')
elif opcion == 3:
    convertir_moneda(0.00027, 'pesos colombianos')
