'''
Pedir la edad al usuario y sumarle 10
'''

#cambio de str a number

age = input ('Cual es tu edad:\n')
result1 = int(age) + 10


#cambio de str a float
print('Resultado 1:', result1)

result2 = float(age) + 10
print('Resultado 2:', result2)

#cambio de int a str
age = 25

text = 'Hola tengo: ' + str(age) + ' años'
print(text)

#-----

print('*' * 30)

empty_text = ''
print(bool(empty_text))

fulltext = 'Hola'
print(bool(fulltext))

number_a = 0
print(bool(number_a))

number_b = 1
print(bool(number_b))