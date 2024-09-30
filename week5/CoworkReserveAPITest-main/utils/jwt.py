import jwt

from fastapi import HTTPException, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# config
from config import CONFIG

# logger
from utils.logger import logger

TOKEN_SECRET = CONFIG['TOKEN_SECRET'] or 'Default secret'

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


def check_jwt(credentials: HTTPAuthorizationCredentials = Security(HTTPBearer())):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, TOKEN_SECRET, algorithms=['HS256'])
        return payload
    except Exception as e:
        logger.debug(str(e))
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail={'message': 'Unauthorized'}
        )
