from pydantic.main import BaseModel


class UserBase(BaseModel):
    username: str = None
    first_name: str = None
    last_name: str = None
    middle_name: str = None
    email: str = None
    phone: str = None


class UserCreate(UserBase):
    username: str
    first_name: str
    last_name: str
    email: str


class UserUpdate(UserBase):
    pass


class UserMain(UserBase):
    id: int

    class Config:
        orm_mode = True
