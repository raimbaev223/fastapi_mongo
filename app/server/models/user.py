from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    email: EmailStr = Field(...)
    userId: int = Field(...)
    isDeleted: bool = Field(default=False)

    class Config:
        schema_extra = {
            "example": {
                "email": "jdoe@x.ex",
                "userId": 20012,
                "isDeleted": False
            }
        }


class UpdateUserModel(BaseModel):
    email: Optional[EmailStr]
    userId: Optional[int]
    isDeleted: Optional[bool]

    class Config:
        schema_extra = {
            "example": {
                "email": "jdoe@x.ex",
                "userId": 20012,
                "isDeleted": False
            }
        }


def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message,
    }
