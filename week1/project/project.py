# by danielprieto - https://github.com/samudex

studentsData = [
    {
        "Cedula": 22457319,
        "Nombre": "Daniel",
        "Apellido": "Prieto",
        "Nota1": 20,
        "Nota2": 20,
        "Nota3": 20,
        "Promedio": 20,
    }
]

while True:
    print("\nPrograma para Gestionar Estudiantes Universitarios.")
    print("1. Registrar estudiante")
    print("2. Listado de estudiantes")
    print("3. Eliminar estudiante")
    print("4. Salir")

    try:
        option = int(input("Escriba un número y presione enter.\n"))
    except ValueError:
        print("Debe ser un numero entero")
        continue

    # 1- Registrar estudiante
    if option == 1:
        cedula = 0

        while True:
            try:
                cedula = int(input("Ingrese la cedula del estudiante a registrar:\n"))
            except ValueError:
                print("Debe ser un numero entero")
                continue
            if cedula >= 0:
                print(f"Ingresate: {cedula}")
                break
            else:
                print("Debe ser un numero entero")

        name = input("Nombre\n")
        while not name:
            name = input("Nombre\n")

        lastname = input("Apellido\n")
        while not lastname:
            lastname = input("Apellido\n")

        grade1 = 0

        while True:
            try:
                grade1 = float(input("Primera nota\n"))
            except ValueError:
                print("Debe ser un valor entre 0.0 y 20")
                continue
            if grade1 >= 0.0 and grade1 <= 20.0:
                break
            else:
                print("Debe ser un valor entre 0.0 y 20")

        grade2 = 0

        while True:
            try:
                grade2 = float(input("Segunda nota\n"))
            except ValueError:
                print("Debe ser un valor entre 0.0 y 20")
                continue
            if grade2 >= 0.0 and grade2 <= 20.0:
                break
            else:
                print("Debe ser un valor entre 0.0 y 20")

        grade3 = 0

        while True:
            try:
                grade3 = float(input("Tercera nota\n"))
            except ValueError:
                print("Debe ser un valor entre 0.0 y 20")
                continue
            if grade1 >= 0.0 and grade3 <= 20.0:
                break
            else:
                print("Debe ser un valor entre 0.0 y 20")

        average = (grade1 + grade2 + grade3) / 3

        # Añadir datos del estudiante al diccionario
        studentsData.append(
            {
                "Cedula": cedula,
                "Nombre": name,
                "Apellido": lastname,
                "Nota1": grade1,
                "Nota2": grade2,
                "Nota3": grade3,
                "Promedio": format(average, ".1f"),
            }
        )
        print("Estudiante registrado exitosamente.")

    # 2- Listado de estudiantes
    elif option == 2:
        print("Listado de estudiantes")
        # print(studentsData)
        for i in range(len(studentsData)):
            print(studentsData[i])
        if not studentsData:
            print("No hay estudiantes registrados.")

    # 3- Eliminar estudiante
    elif option == 3:
        if studentsData:
            hasBeenDeleted = False
            studentId = int(input("Ingrese la cedula del estudiante a eliminar\n"))
            for i in range(len(studentsData)):
                if studentsData[i]["Cedula"] == studentId:
                    del studentsData[i]
                    hasBeenDeleted = True
                    print("Estudiante eliminado exitosamente.")
                    break
            if hasBeenDeleted == False:
                print("Cédula no encontrada.")
        else:
            print("No hay estudiantes que se puedan eliminar.")

    # 4- Salir
    elif option == 4:
        print("¡Hasta luego!")
        break

    else:
        print("Opcion invalida")
