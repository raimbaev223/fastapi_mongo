# from typing import Optional
# from pydantic import BaseModel, Field
#
#
# class ChatSchema(BaseModel):
#     type: str = Field(enum=[
#         "private",
#         "global",
#         "chanel",
#         "group",
#     ])
#     createdBy: int = Field(...)
#     users: list = Field(default=[])
#     admins: list = Field(default=[])
#     messages: list = Field(default=[])
#     isDeleted: bool = Field(default=False)
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "chatId": "632f13afa0d225a6140eaa44",
#                 "createdBy": 20012,
#                 "users": [...],
#                 "admins": [...],
#                 "messages": [
#                     {
#                         "id": "632f13afa0d225a6140eaa45",
#                         "createDate": "date",
#                         "sender": "userId",
#                         "type": "text",
#                         "data": "data",
#                         "isReplied": False
#                     },
#                     {
#                         "id": "632f13afa0d225a6140eaa46",
#                         "createDate": "date",
#                         "sender": "userId",
#                         "type": "text",
#                         "data": "data",
#                         "isReplied": True,
#                         "repliedMessage": "632f13afa0d225a6140eaa45",
#                     }
#                 ],
#                 "createDate": "date",
#                 "isDeleted": False,
#             }
#         }
#
#
# class UpdateChatModel(BaseModel):
#     createdBy: Optional[int]
#     users: Optional[list]
#     admins: Optional[list]
#     messages: Optional[list]
#     isDeleted: Optional[bool]
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "id": "632f13afa0d225a6140eaa45",
#                 "createDate": "date",
#                 "sender": "userId",
#                 "type": "text",
#                 "data": "data",
#                 "isReplied": False
#             }
#         }
#
#
# class AddMessageChatModel(BaseModel):
#     user: Optional[int]
#     data: Optional[str]
#     type: Optional[str]
#     isReplied: Optional[bool]
#     repliedMessage: Optional[str]
#     isDeleted: Optional[bool]
#
#     class Config:
#         schema_extra = {
#             "example": {
#                 "chatId": "632f13afa0d225a6140eaa44",
#                 "createdBy": 20012,
#                 "users": [...],
#                 "admins": [...],
#                 "messages": [
#                     {
#                         "id": "632f13afa0d225a6140eaa45",
#                         "createDate": "date",
#                         "sender": "userId",
#                         "isReplied": False
#                     },
#                     {
#                         "id": "632f13afa0d225a6140eaa46",
#                         "createDate": "date",
#                         "sender": "userId",
#                         "isReplied": True,
#                         "repliedMessage": "632f13afa0d225a6140eaa45"
#                     }
#                 ],
#                 "createDate": "date",
#                 "isDeleted": False,
#             }
#         }
#
#
# def ResponseModel(data, message):
#     return {
#         "data": [data],
#         "code": 200,
#         "message": message,
#     }
#
#
# def ErrorResponseModel(error, code, message):
#     return {
#         "error": error,
#         "code": code,
#         "message": message,
#     }
