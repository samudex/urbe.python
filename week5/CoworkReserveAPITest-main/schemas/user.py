from pydantic import BaseModel, EmailStr, Field


class UserRegister(BaseModel):
    name: str = Field(max_length=127)
    email: EmailStr = Field(max_length=127)
    password: str = Field(max_length=127)


class UserLogin(BaseModel):
    email: EmailStr = Field(max_length=127)
    password: str = Field(max_length=127)