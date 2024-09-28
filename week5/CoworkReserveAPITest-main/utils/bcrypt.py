import bcrypt


# decode: de bytes a string
# encode: de string a bytes


def encrypt_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()


def check_password(hashed_password: str, password: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed_password.encode())


print(encrypt_password('123456789'))
    