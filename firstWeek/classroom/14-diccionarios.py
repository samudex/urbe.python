person = {
    'name': 'Ronald',
    'age': 26,
    'job': 'Developer'
}
print(person)
print(type(person))

# Obtener un valor
print(person['name'])

# Actualizar
person['job'] = 'Professor'
print(person)

# añadir propiedad
person['sport'] = 'futbol'
print(person)

# remover propiedad
del person['sport']
print(person)