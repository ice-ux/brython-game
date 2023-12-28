from datetime import date
from pydantic import BaseModel, Field


class UserBase(BaseModel):
    username : str
    password : str
    email : str
    registrationdate : date


    class Config:
        from_attributes = True






