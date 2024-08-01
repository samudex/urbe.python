a = 3.2
b = 2.2 + 1
print(a == b)

print('*' * 40)

a = 3.2
b = 2.2 + 1.2
print(a == b)
#da false, que raro

print(a)
print(b)
#b tiene un decimal muy pequeño. Es un valor exacto pero impreciso

print('*' * 40)
#Opcion 1 metodo format
b_str = format(b, '.1f')
print(float(b_str))
print(a == float(b_str))

print('*' * 40)
#Opcion 2 metodo round
b_rounded = round(b, 1)
print(b_rounded)
print(a == b_rounded)

print('*' * 40)
print('Opcion 3')
#Opcion 3 Valor absoluto y margen de error
x = 3.2
y = 2.2 + 1
print(abs(x - y) < 0.00001)

print('*' * 40)
print('Opcion 4 (la mejor)')
#Opcion 4 Is Close
#import math
#math.isclose()
from math import isclose


print(isclose(x, y))
print(isclose(a, b))