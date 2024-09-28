import jwt


SECRET_KEY = 'secret key'


def create_token(email: int, role: str) -> str:
    return jwt.encode(
        {'email': email, 'role': role},
        SECRET_KEY, 
        'HS256'
    )


def decode_token(token: str) -> dict:
    return jwt.decode(
        token, 
        SECRET_KEY, 
        ['HS256']
    )