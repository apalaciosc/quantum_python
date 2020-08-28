import os
# Imprimir nombres de los archivos en una lista de una determinada ruta
listado = os.listdir('/Users/apc/Downloads')
for i in listado:
    print(i)
print(listado)

# Listar los archivos a manera de objeto DirEntry
escaneo = os.scandir('/Users/apc/Downloads')
with escaneo as entries:
    for entry in entries:
        print(entry.path)

listado = os.listdir('/Users/apc/Downloads')
for i in listado:
    if os.path.isdir(os.path.join('/Users/apc/Downloads', i)):
        print(i)


try:
    os.mkdir('/Users/apc/Desktop/quantum_python/clase_07/test_1')
except FileExistsError:
    print('El directorio ya existe.')

try:
    os.rename('/Users/apc/Desktop/quantum_python/clase_07/test_1', '/Users/apc/Desktop/quantum_python/clase_07/test_2')
except:
    print('Hubo un error.')

print(os.getcwd())

