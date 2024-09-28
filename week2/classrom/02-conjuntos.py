# conjuntos no aceptan listas [], solo numeros y strings
# al poner los valores sin parentesis quita los repetidos
numbers = {1, 1, 4, 5}
print(type(numbers))
print(numbers)

# al poner los valores entre parentesis no quita los repetidos, pero si quita los valores entre parentesis repetidos
values = {(1, 2, 3), (1, 2, 3)}
print(values)

# metodo add (no acepta lista, conjuntos, diccionarios), agrega los valores pero de forma desordenada
numbers.add(10)
print(numbers)

# metodo update
numbers_b = {11, 12}
numbers.update(numbers_b)
print("Conjunto actualizado:", numbers)

# metodo discard, si lo encuentra lo elimina, sino no lo elimina, no arroja error
numbers.discard(12)
print(numbers)

# metodo remove, si no encuentra el valor, da error
numbers.remove(11)
print(numbers)

# metodo pop elimina el primer valor del conjunto
print(numbers.pop())
print(numbers)

names = {"Ronald", "leonardo", "andres"}
print(names)
print(names.pop())

# metodo union
a = {1, 2, 3}
b = {4, 5, 6}
c = {7, 8, 9}

result = a.union(b, c)
print(result)
