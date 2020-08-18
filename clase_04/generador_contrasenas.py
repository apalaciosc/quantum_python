import random

def generar_contrasena():
    mayusculas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    minusculas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    simbolos = ['!', '#', '$', '&', '/', '(', ')', '%']
    numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    caracteres = mayusculas + minusculas + simbolos + numeros

    contrasena = []

    for i in range(25):
        caracter_random = random.choice(caracteres)
        contrasena.append(caracter_random)

    contrasena = "".join(contrasena)
    return contrasena


nueva_contrasena = generar_contrasena()
print(f'Tu nueva contraseña es: {nueva_contrasena}')
