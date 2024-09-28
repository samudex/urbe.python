numbers = [1,2,3,4,5]

#Append (agregar valor)
numbers.append('text')
print(numbers)

# insert indica el indice donde quieres insertar
numbers.insert(1, 7)
print(numbers)

#remove
numbers.remove(7)
print(numbers)

#eliminar el 'text'
#numbers.remove('text')
#eliminar el ultimo valor
del numbers[len(numbers) - 1]
print(numbers)

# reverse
numbers.reverse()
print(numbers)