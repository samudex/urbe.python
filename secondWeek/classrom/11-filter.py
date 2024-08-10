"""
range es similar a un for tradicional, donde el primer valor es el valor de inicio, el segundo es el stop y el tercero es opcional e indica de cuanto en cuanto es el incremento del valor. Esto crea un rango de valores. Se diferencia de una lista porque usa parentesis en vez de brackets
() parentheses  or round brackets
[] brackets     or square brackets
{} curly braces or curly brackets
<> chevrons     or angle brackets
"""

numbers = list(range(0, 100))
# print(numbers)


def is_par(num):
    if num % 2 == 0:
        return num


"""
filter() Filtra elementos de una lista (o cualquier iterable) que cumplen con una condición específica.
Se utiliza cuando quieres seleccionar solo los elementos que cumplen con una condición

El metodo filter recibe dos parametos: el primero es una funcion a ejecutar y el segundo un rango de valores iterable.
Si en el iterable se cumple la condicion de la funcion, se añade a una nueva lista.

"""

result1 = list(filter(is_par, numbers))
print("Con función aparte", result1)

print("*" * 50)

result2 = list(filter(lambda x: x if x % 2 == 0 else None, numbers))
print("Con lambda y ternario", result2)

print("*" * 50)

result3 = list(filter(lambda x: x % 2 == 0, numbers))
print("Con lambda sin ternario", result3)

print("*" * 50)

# Filtrar users que sol esten en True
users = [
    {"name": "Ronald", "status": True},
    {"name": "Ronald 1", "status": True},
    {"name": "Ronald 2", "status": True},
    {"name": "Ronald 3", "status": False},
]

active_users = list(filter(lambda user: user["status"], users))
print(active_users)

# Filtrar users que sol esten en False
inactive_users = list(filter(lambda user: not user["status"], users))
print(inactive_users)
