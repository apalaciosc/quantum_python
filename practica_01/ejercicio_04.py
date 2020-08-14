def evaluar_divisibilidad(n, x, y):
    if n % x == 0 and n % y == 0:
        print(True)
    else:
        print(False)


n = float(input('Ingresa el numero a evaluar: '))
x = float(input('Ingresa X: '))
y = float(input('Ingresa Y: '))
evaluar_divisibilidad(n, x, y)
