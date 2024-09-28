# funcion de orden superior 1: fucion que recibe como parametro otra funcion


def addition(x, y):
    return x + y


def substraction(x, y):
    return x - y


def calculator(operation, x, y):
    return operation(x, y)


print(calculator(addition, 10, 20))
print(calculator(substraction, 10, 20))

# funcion de orden superior


def outer(x):
    def inner(y):
        return x + y

    return inner


output1 = outer(10)
output2 = output1(20)
print(output2)


output3 = outer(10)(20)
print(output3)
