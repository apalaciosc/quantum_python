# Calcular el factorial de un numero

def factorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        print(f'Se está multiplicando {resultado} por {i}')
        resultado *= i
    return resultado

numero = int(input('Ingresa un número: '))
print(factorial(numero))
