# funciones puras


def addition(x, y):
    return x + y


def to_lower(text):
    return text.lower()


print(addition(10, 20))
print(to_lower("CASA"))

# funciones impuras (modifica una variable fuera de una funcion)
users = ["Ronald"]


def add_user(name):
    users.append(name)
    return users


print(add_user("Leonardo"))
print(add_user("Jesus"))


# funcion para revertir un string
def reverse_str(word):
    return word[::-1]


print(reverse_str("Hola"))
