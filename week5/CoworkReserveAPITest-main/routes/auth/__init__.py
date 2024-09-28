from fastapi import APIRouter, Depends, HTTPException, status

# database
from sqlalchemy.orm import Session
from database.deps import get_db

# models
from models.user import User
from models.admin import Admin

# schemas
from schemas.user import UserRegister, UserLogin
from schemas.admin import AdminLogin

# utils
from utils.bcrypt import encrypt_password, check_password
from utils.jwt import create_token, decode_token


router = APIRouter(prefix='/auth', tags=['auth'])


@router.post('/register')
def register(user: UserRegister, db: Session = Depends(get_db)):
    # buscar usuario por email
    user_by_email = db.query(User).filter(User.email == user.email).first()

    # verificar si el usuario existe
    if user_by_email:
        raise HTTPException(
            status_code=status.HTTP_202_ACCEPTED,
            detail={'message': 'El usuario se encuentra registrado'}
        )
    
    # encriptar contraseña
    hashed_password = encrypt_password(user.password)

    # crear usuario que registraremos en base de datos
    new_user = User(
        name=user.name,
        email=user.email,
        password=hashed_password
    )
    
    # registramos al usuario en base datos
    db.add(new_user)

    # guardamos ls cambios en base de datos
    db.commit()
    
    return {
        'message': 'Usuario registrado'
    }


@router.post('/user/login')
def user_login(user: UserLogin, db: Session = Depends(get_db)):
    # buscar usuario por email
    user_by_email = db.query(User).filter(User.email == user.email).first()

    # verificar si el usuario existe
    if user_by_email is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'message': 'El email ingresado no existe'}
        )
    
    if check_password(user_by_email.password, user.password) is False:
         raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'message': 'La contraseña es incorrecta'}
        )
    
    token = create_token(user_by_email.email, 'user')

    return {
        'token': token
    }


@router.post('/admin/login')
def admin_login(admin: AdminLogin, db: Session = Depends(get_db)):
    # buscar admin por email
    admin_by_email = db.query(Admin).filter(Admin.email == admin.email).first()

    # verificar si el usuario existe
    if admin_by_email is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={'message': 'El email ingresado no existe'}
        )
    
    if check_password(admin_by_email.password, admin.password) is False:
         raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail={'message': 'La contraseña es incorrecta'}
        )
    
    token = create_token(admin_by_email.email, 'admin')

    return {
        'token': token
    }




