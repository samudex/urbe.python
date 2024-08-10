# asserts muestran un error pero sigue ejecutando el programa

def suma(x, y):
    return x + y

assert suma(10, 20) == 30, 'Error'

# excepciones

try:
    global app = 10
except SyntaxError as e:
    print()
    print(str(e))

print('el programa continua')