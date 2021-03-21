from typing import List, Optional
from pydantic import BaseModel


class HomeWorkBase(BaseModel):
    title: str
    description: Optional[str] = "-"

class HomeWorkCreate(HomeWorkBase):
    pass


class HomeWork(HomeWorkBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    home_works: List[HomeWork] = []

    class Config:
        orm_mode = True