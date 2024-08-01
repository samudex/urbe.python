person = {
    'name': 'Ronald',
    'age': 26,
    'job': 'Developer'
}

# metodo de obtener
## aqui da error
#print(person['sport'])
print(person.get('sport', 'futbol'))

# metodo de actualizar 
person.update({'job':'Profesor', 'name':'jose', 'hobby':'read'})
print(person)

# metodo de eliminar que es mejor que del
person.pop('hobby')
print(person)

#borra la ultima llave
person.popitem()
print(person)