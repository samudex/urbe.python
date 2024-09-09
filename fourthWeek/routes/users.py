from fastapi import APIRouter
from schemas.users import User

import json


router = APIRouter(prefix='/users', tags=['users'])


@router.get('/')
def get_all_users() -> list[User]:
    """
    Obtener todos los usuarios
    """

    with open('database/db.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data['users']
