numbers = list(range(0, 100))
# print(numbers)


def is_par(num):
    if num % 2 == 0:
        return num


result1 = list(filter(is_par, numbers))
print("Con función aparte", result1)

print("*" * 50)

result2 = list(filter(lambda x: x if x % 2 == 0 else None, numbers))
print("Con lambda y ternario", result2)

print("*" * 50)

result3 = list(filter(lambda x: x % 2 == 0, numbers))
print("Con lambda sin ternario", result3)

print("*" * 50)

# Filtrar users que sol esten en True
users = [
    {"name": "Ronald", "status": True},
    {"name": "Ronald 1", "status": True},
    {"name": "Ronald 2", "status": True},
    {"name": "Ronald 3", "status": False},
]

active_users = list(filter(lambda user: user["status"], users))
print(active_users)

# Filtrar users que sol esten en False
inactive_users = list(filter(lambda user: not user["status"], users))
print(inactive_users)
