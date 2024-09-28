'''
La comprehension de diccionario es similar a la comprehension de listas, pero en vez de usar [] usa {}
La comprehension se usa para transformar un diccionario en otro, reemplazar for loops (anidados) o funciones anonimas (lambda) con map(), filter() y reduce()

'''

data = {"name": "Ronald",
        "lastname": "Abu Saleh"}

# print(data.items())

result = {key: value for (key, value) in data.items()}
print(result)

result2 = {key + "1": value + "adef" for (key, value) in data.items()}
print(result2)
