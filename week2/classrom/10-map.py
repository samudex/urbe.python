"""
el map es un metodo realiza una operacion a cada elemento de una lista y devuelve una nueva lista
Se utiliza cuando quieres transformar cada elemento de una colección de datos de manera independiente.
    map(función, iterable)

map: Transforma cada elemento de la lista de manera independiente. Ejemplo: Duplicar cada número en una lista.
filter: Selecciona elementos que cumplen con una condición. Ejemplo: Filtrar números pares de una lista.
reduce: Combina todos los elementos de una lista en un solo valor. Ejemplo: Sumar todos los números en una lista.
"""

numbers = [1, 2, 3, 4, 5, 10, 12]

print(list(map(lambda x: x + 1, numbers)))
# si no pongo list, imprime la direccion de memoria de la lista


# str --> es un tipado
def to_lower(text: str):
    return text.lower()


names = ["Ronald", "Alejandro", "JohAN"]

name_list = list(map(to_lower, names))
print(name_list)


pares = list(map(lambda num: num if num % 2 == 0 else None, numbers))
print(pares)

# -----------------------------------------------------------------------

users = [
    {"name": "Ronald", "lastname": "Abu Saleh"},
    {"name": "Leonardo", "lastname": "Abu Saleh"},
    {"name": "Johan", "lastname": "Paz"},
]

# con map devolver una lista que solo tenga los apellidos "Abu Saleh"


def process_user(user):
    if user["lastname"] == "Abu Saleh":
        user["lastname"] = "Perez"
        return user
    return user


# print(list(map(lambda user: user if user['lastname'] == 'Abu Saleh' else None, users)))

print(list(map(process_user, users)))
