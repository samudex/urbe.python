from fastapi import APIRouter, Depends, HTTPException, status

# database
from sqlalchemy.orm import Session
from database.deps import get_db

# models
from models.user import User
from models.admin import Admin
import models.coworking as coworking_model

# schemas
from schemas.user import UserRegister, UserLogin
from schemas.admin import AdminLogin
import schemas.coworking as coworking_schema

# utils
from utils.bcrypt import encrypt_password, check_password
from utils.jwt import create_token, decode_token, check_jwt


router = APIRouter(prefix='/coworking', tags=['coworking'])


@router.get('/')
def get_coworkings(name: str = '', price_by_hour: float = 0.0, is_available: int = 1, db: Session = Depends(get_db)):
    # try:
    #     if token_payload['role'] != 'admin':
    #         raise HTTPException(
    #             status_code=status.HTTP_401_UNAUTHORIZED,
    #             detail={'message': 'Unauthorized'}
    #         )
    # except Exception as e:
    #     # logger_utils.logger.debug(str(e))
    #     raise HTTPException(
    #         status_code=status.HTTP_401_UNAUTHORIZED,
    #         detail={'message': 'Unauthorized'}
    #     )

    try:
        query = db.query(coworking_model.Coworking).filter(coworking_model.Coworking.name.like(
            f'{name}%')).where(coworking_model.Coworking.is_available == is_available)

        if price_by_hour != 0.0:
            query.where(coworking_model.Coworking.price_by_hour ==
                        price_by_hour)

        coworkings = query.all()
    except Exception as e:
        # logger_utils.logger.debug(str(e))
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={'message': 'Server internal error'}
        )

    return coworkings
