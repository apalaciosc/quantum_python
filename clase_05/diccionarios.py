# mi_diccionario = {
#     'llave1': 1,
#     'llave2': 10,
#     'llave3': 'Hola Mundo'
# }
# variable_x = mi_diccionario['llave3']
# print(variable_x)

poblacion_paises = {
    'Argentina': 44912123,
    'Brasil': 2100121212,
    'Colombia': 531231
}
for pais, poblacion in poblacion_paises.items():
    print(f'El pais: {pais} tiene una población de: {poblacion}')

# for pais in poblacion_paises.keys():
#     print(pais)

# for pais in poblacion_paises.values():
#     print(pais)

# print(poblacion_paises['Brasil'])
