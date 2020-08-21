# Hacer un programa que lea las calificaciones de un alumno en 10 asignaturas,
# las almacene en un vector y calcule e imprima su media
def calcular_media(lista):
    suma = 0
    for i in lista:
        suma += i
    numero_de_notas = len(lista)
    return suma/numero_de_notas


lista = [
    15,
    20,
    10,
    10,
    3,
    18,
    19,
    10,
    12,
    10,
    20,
    12
]

print(calcular_media(lista))
