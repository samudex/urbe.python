# creamos una funcion
def saludar():
    print('Hola amigos')


# llamamos a la función
saludar()

# funciones con parametros
def sumar(x, y):
    # validacion de x
    if x < 0 or x > 20:
        return 'El numero debe estar entre 0-20'
    
    # validcion de y
    if y < 0 or y > 20:
        return 'El numero debe estar entre 0-20'

    return x + y


print(sumar(5, 21))


# funciones con parametros por defecto

def print_name(name='Leonardo'):
    print(name)


print_name()
print_name('Ronald')

# funciones de multiples return
from random import randint

def get_random_numbers():
    x = randint(0, 100)
    y = randint(0, 100)

    return x, y


result = get_random_numbers()


print(result)
print(result[0])
print(result[1])