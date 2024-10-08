# Daniel Prieto 22457319
# Mini sistema bancario, programacion orientada a objetos con python.

class Persona:
    def __init__(self, nombre, apellido, cedula):
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula


class Usuario(Persona):
    def __init__(self, nombre, apellido, cedula, nombre_usuario, contrasena):
        super().__init__(nombre, apellido, cedula)
        self.nombre_usuario = nombre_usuario
        self.contrasena = contrasena
        self.cuenta = None


class Cuenta:
    def __init__(self, numero_cuenta, saldo):
        self.numero_cuenta = numero_cuenta
        self.saldo = saldo

    def depositar(self, amount):
        if amount > 0:
            self.saldo += amount
            print("Depósito exitoso.")
        else:
            print("Monto de depósito inválido.")

    def retirar(self, amount):
        if amount > 0 and amount <= self.saldo:
            self.saldo -= amount
            print("Retiro exitoso.")
        else:
            print("Fondos insuficientes o monto de retiro inválido.")


class SistemaBancario:
    def __init__(self):
        self.users = []  # almacenará objetos de clase Usuario
        self.session = None  # inicialmente no hay sesion iniciada
        self.load_default_users()

    def load_default_users(self):
        user1 = Usuario("John", "Doe", "26275576", "johndoe", "123456")
        user2 = Usuario("Ryan", "Smith", "25645888", "ryansmith", "123456")
        self.users.append(user1)
        self.users.append(user2)

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        for user in self.users:
            if user.nombre_usuario == username and user.contrasena == password:
                self.session = user.cedula
                print(f"Bienvenido {user.nombre} {user.apellido}")
                return
        print("Usuario o contraseña incorrecto.")

    def logout(self):
        self.session = None
        print("Sesión cerrada.")

    def get_logged_in_user(self):
        for user in self.users:
            if user.cedula == self.session:
                return user
        return None

    def is_account_number_unique(self, account_number):
        for user in self.users:
            if user.cuenta and user.cuenta.numero_cuenta == account_number:
                return False
        return True

    def create_bank_account(self):
        user = self.get_logged_in_user()
        if user.cuenta is None:
            while True:
                account_number = input("Número de cuenta (12 digitos): ")
                if len(account_number) != 12 or not account_number.isdigit():
                    print("La cuenta bancaria debe poseer 12 digitos.")
                    continue
                if self.is_account_number_unique(account_number):
                    break
                else:
                    print(
                        "El número de cuenta ya existe, por favor intente otro número")
            initial_balance = self.get_valid_amount("Saldo inicial: ")
            user.cuenta = Cuenta(account_number, initial_balance)
            print("Cuenta de banco creada exitosamente.")
        else:
            print("Actualmente ya tienes una cuenta de banco.")

    def get_valid_amount(self, prompt):
        while True:
            try:
                amount_str = input(prompt).replace(',', '.')
                amount = float(amount_str)
                if amount < 0:
                    print("El monto no puede ser negativo.")
                    continue
                if len(str(amount).split(".")[1]) > 2:
                    print("El monto no puede tener más de 2 decimales.")
                    continue
                return amount
            except ValueError:
                print("Por favor, ingrese un número válido.")

    def deposit(self):
        user = self.get_logged_in_user()
        if user.cuenta:
            amount = self.get_valid_amount("Monto a depositar: ")
            user.cuenta.depositar(amount)
        else:
            print("Usted no posee una cuenta de banco.")

    def withdraw(self):
        user = self.get_logged_in_user()
        if user.cuenta:
            amount = self.get_valid_amount("Monto a retirar: ")
            user.cuenta.retirar(amount)
        else:
            print("Usted no posee una cuenta de banco.")

    def transfer(self):
        user = self.get_logged_in_user()
        if user.cuenta:
            recipient_id = input("Cédula del destinatario: ")
            if recipient_id == user.cedula:
                print("No puedes transferirte dinero a ti mismo.")
                return
            recipient_user = None
            for u in self.users:
                if u.cedula == recipient_id:
                    recipient_user = u
                    break
            if recipient_user and recipient_user.cuenta:
                amount = self.get_valid_amount("Monto a transferir: ")
                if amount > 0 and amount <= user.cuenta.saldo:
                    user.cuenta.retirar(amount)
                    recipient_user.cuenta.depositar(amount)
                    print("Transferencia exitosa.")
                else:
                    print("Fondos insuficientes o monto inválido.")
            else:
                print("Destinatario no encontrado o no posee una cuenta de banco.")
        else:
            print("Usted no posee una cuenta bancaria.")

    def main(self):
        while True:
            if self.session is None:
                self.login()
            else:
                user = self.get_logged_in_user()
                print(
                    f"\n*******\nUsuario Actual: {user.nombre} {user.apellido}")
                if user.cuenta:
                    print(f"Saldo Actual: $ {user.cuenta.saldo:.2f}")
                else:
                    print("Usted no posee cuenta bancaria.")
                print("\nMenú principal:")
                print("1. Crear cuenta bancaria")
                print("2. Depositar efectivo")
                print("3. Retirar efectivo")
                print("4. Transferencia electrónica")
                print("5. Cerrar Sesión")
                option = input("Seleccione una opción: ")
                if option == "1":
                    self.create_bank_account()
                elif option == "2":
                    self.deposit()
                elif option == "3":
                    self.withdraw()
                elif option == "4":
                    self.transfer()
                elif option == "5":
                    self.logout()
                else:
                    print("Opción invalida. Intente nuevamente.")


if __name__ == "__main__":
    banking_system = SistemaBancario()
    banking_system.main()
