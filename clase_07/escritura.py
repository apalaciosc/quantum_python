# Crear y escribir en un archivo
with open('numeros.txt', 'w') as f:
    for i in range(10):
        f.write(str(i))

# Otra forma
try:
    f = open('numeros.txt', 'w')
    for i in range(10):
        f.write(str(i))
finally:
    f.close()
