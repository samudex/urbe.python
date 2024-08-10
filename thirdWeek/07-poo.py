class Person:
    def __init__(self, name, lastname,age):
        self.name = name
        self.lastname = lastname
        self._age = age

person1 = Person ('Ronald', 'Abu Saleh',25)
# print(person1.name)
# print(person1.lastname)
print(f'{person1.name}{person1.lastname}')

person2 = Person ('Daniel', 'Prieto',31)
print(f'{person2.name}{person2.lastname}')

#----------------

class Developer(Person):
    __salary = 1000

    #un piso es protegido, dos pisos es privado y no se puede usar fuera de la clase. sin piso es publica.
    def __init__(self,name,lastname,age,position,code):
        super().__init__(name,lastname,age)
        self.position = position
        self.__code = code

    def print_code(self):
        return self.__code
    
    def set_salary(self,new_salary: float):
        self.__salary = new_salary

developer1 = Developer('Brayan','Paz',22,'Engineer',142)
print(developer1.name, developer1.lastname, developer1.position, developer1._age)

#print(developer1.__code)

