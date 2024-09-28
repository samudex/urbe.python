# *args es una tupla de valores indefinidos.
# Con *args No necesito saber la cantidad de argumentos que voy a pasarle a una funcion para poder definirla.

def suma(*args):
    total = 0
    for num in args:
        total += num
    return total


print(suma(1, 2, 3, 4, 5, 7, 10))
