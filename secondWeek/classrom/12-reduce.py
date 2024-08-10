from functools import reduce

"""
Reduce Se utiliza cuando quieres combinar todos los elementos de una colección de datos en un solo valor.
    reduce(función, iterable)
"""


numbers = list(range(0, 100))
# print(numbers)

# devuelve el menor numero
smallest = reduce(lambda prev, next: prev if prev < next else next, numbers)
print(smallest)

# devuelve el mayor numero
biggest = reduce(lambda prev, next: prev if prev > next else next, numbers)
print(biggest)

# suma de todos ls numeros en la lista
total = reduce(lambda prev, next: prev + next, numbers)
print(total)
