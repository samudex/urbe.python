text = 'Welcome to Python course'

#Extraer la "e"
print(text[1])

print(text.index('P'))
index = text.index('Python')
print(text[index])

# includes
# does Python exists in text variable?
print('Python' in text)

to_search = 'Python'

#lower (pasar a minuscula)
print(to_search.lower() in text.lower())

#upper (pasar a mayuscula)
print(text.upper())

#count sensible a mayusculas
print(text.count('Python'))

#count sin ser sensible a mayusculas
print(text.lower().count(to_search.lower()))

#Replace
print(text.replace('Python','Javascript'))

