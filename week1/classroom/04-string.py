# tipo 1 de concatenacion

age = str(30)

text = 'Hola, mi edad es de ' + age + ' años'
print(text)

# tipo 2 de concatenacion (string formatting)

name = 'Daniel'
age = 31
sport = 'futbo'

result = 'Hola, mi nombre es {} y tengo {} años'.format(name, age)

print(result)

# tipo 3 de concatenacion (string formatting) Pythonista

result2 =f'Hola mi nombre es {name}, tengo {age + 1} años y me gusta el {sport}'
print(result2)

