numbers = [1,2,3,4,5]
print(numbers)
print(type(numbers))

random = [1, 'A', True, False]
print(random)

print(list(range(1,10)))

# --------

print('*' * 40)

##Obtener un valor
print(numbers[4])

##Obtener la ultima posicion
last_index = len(numbers) - 1
print(numbers[last_index])
print('*' * 40)

##Actualizar valores
index_five = numbers.index(5)

numbers[index_five] = 10
print(numbers)

# slicing
print(numbers[:4])
# de 4 en 4
print(numbers[::4]) 
# revisar si existe un valor en el array
print(10 in numbers)