# asserts muestran un error pero sigue ejecutando el programa

def suma(x, y):
    return x + y


# assert suma(10, 1) == 30, 'Error'

# excepciones
try:
    nums = [1]
    print(nums[0])
except Exception as e:
    print(str(e))
finally:
    print("codigo que se ejecuta pase lo que pase")


print("El programa continua")


# raise (errores personalizados)
def get_user_by_id(id: int | None):
    try:
        def procesar(id: int | None):
            if id is None:
                raise Exception("El id no puede estar vacio")
        procesar(id)
    except Exception as e:
        print(str(e))


get_user_by_id(None)
