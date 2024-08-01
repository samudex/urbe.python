numbers = list(range(0, 5))
print(numbers)

for number in numbers:
    #print(f'Este es el numero {number}')
    
    if number == 0:
        continue
    elif number % 2 == 0:
        print(f'el numero{number} es par')
    else:
        print(f'el numero{number} es impar')