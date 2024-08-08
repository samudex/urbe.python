# variavle global
number = 20


def funcion_principal():
    # variable local
    x = 10
    print(number)

    def funcion_secundaria():
        # variable anidada
        y = 20
        global z
        z = 50

        # las varibles globales se guardan en diccionario y no pueden haber 2 variables globales con el mismo nombre
        ## no se puede instanciar 2 veces
        # global z
        # z = 100

        print(number)

    funcion_secundaria()
    # print(y)


funcion_principal()
# print(x)
# print(funcion_secundaria())
# print(y)
print("Z", z)
