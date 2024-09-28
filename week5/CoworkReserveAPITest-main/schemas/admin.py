from pydantic import BaseModel, EmailStr, Field


class AdminLogin(BaseModel):
    email: EmailStr = Field(max_length=127)
    password: str = Field(max_length=127)