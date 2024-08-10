'''
Se utiliza list comprehension cuando se quiere crear una nueva lista basada en valores de una lista existente. Esto con el fin de FILTRAR elementos según un valor dado.

newlist = [expression for item in iterable if condition == True]

ejemplo:
newlist = [x for x in fruits if x !="apple"]
'''

users = [
    {"name": "Ronald", "status": True},
    {"name": "Ronald 1", "status": True},
    {"name": "Ronald 2", "status": True},
    {"name": "Ronald 3", "status": False},
]

# Filtrar users que sol esten en True
# active_users = [user for user in users if user['status'] == True]
active_users = [user for user in users if user["status"]]
print(active_users)


person = {"name": "Leonardo", "age": 26}

# spread operator. Se trae solo el contenido del diccionario y no altera la variable original.
# diccionario es con **, lista es con *
person1 = {**person}
print(person1)

# filtrar tareas por titulo
tasks = [
    {"title": "Aprender Python"},
    {"title": "Aprender JavaScript"},
    {"title": "Cocinar"},
]

search_text = "aprender"

coincidences = [task for task in tasks if search_text.lower() in task["title"].lower()]
print(coincidences)

# cambiar el nombre de "Ronald 1" -> "Ronald 10"
modified_users = [
    {**user, "name": "Ronald 10" if user["name"] == "Ronald 1" else user["name"]}
    for user in users
    if user["status"]
]
print(modified_users)

print("*" * 50)

developer = {"name": "Michaell", "language": "Python"}

new_developer = {**developer, "language": "C#", "age": 25}
print("Developer", developer)
print("New Developer", new_developer)

print("*" * 50)

# spread operator con listas
a = [1, 2]
b = [*a, 3, 4, 5]

print("A", a)
print("B", b)

# swith in Python (match)
x = 10

match x:
    case 1:
        print("1")
    case 2:
        print("2")
    case 3:
        print("3")
    case _:
        print("default")
