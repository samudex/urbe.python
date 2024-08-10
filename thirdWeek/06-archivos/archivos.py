#file = open('./06-archivos/data.txt', 'r')
file = open('./data.txt', 'r')

#lee linea por linea
print(file.readline())
print(file.readline())

#lee todo el archivo
print(file.read())

#cierra el archivo
file.close()

'''
Gestion de archivos con with (cierra el archivo automaticamnete)
'''

print('lectura con with')
with open(file='./data.txt', mode='r', encoding='utf-8') as file:
    print(file.read())