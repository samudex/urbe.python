class Person:

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname

        # propiedades privadas (comienzan con _)
        self._age = age


person1 = Person('Ronald', 'Abu Saleh', 26)
print(f'{person1.name} {person1.lastname}')

person2 = Person('Leonardo', 'Villalobos', 25)
print(f'{person2.name} {person2.lastname}')

# ---------------------------------------------------

print("*" * 50)


class Developer(Person):
    __salary = 1000.0
    # un piso es protegido, dos pisos es privado y no se puede usar fuera de la clase. sin piso es publica.

    def __init__(self, name, lastname, age, position, code):
        # propiedades publicas
        super().__init__(name, lastname, age)
        self.position = position

        # propiedades privadas (comienzan con __)
        self.__code = code

    def print_code(self):
        return self.__code

    def set_salary(self, new_salary: float):
        self.__salary = new_salary

    def get_salary(self):
        return self.__salary


developer1 = Developer("Ryan", "Paz", 22, "Engineer", 142)
print(developer1.name, developer1.lastname,
      developer1.position, developer1._age)

# no puedo acceder porque es una propiedad privada
# print(developer1.__code)

# Podemos ingresar a code (propiedad privada) a traves de una funcion
print(developer1.print_code())

# setear nuevo salario
developer1.set_salary(1100)

# accediendo a una propiedad privada a travès de un metodo get
print(developer1.get_salary())
