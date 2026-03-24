from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    username: str
    email: str
    password: str = Field(min_length=6, max_length=72)

class UserLogin(BaseModel):
    username: str
    password: str

class UserResponse(BaseModel):
    id: int
    username: str
    email: str

    class Config:
        from_attributes = True
