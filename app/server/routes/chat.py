from fastapi import APIRouter, Body, Query
from fastapi.encoders import jsonable_encoder

from ..models.chat_entity import (
    add_chat,
    get_chat,
    get_all_chats,
    add_message_to_chat
)
from ..models.chat import (
    ErrorResponseModel,
    ResponseModel,
    ChatSchema,
    UpdateChatModel,
    # AddMessageChatModel,
)

router = APIRouter()


@router.post("/", response_description="Chat data added into the database")
async def create_chat(chat: ChatSchema = Body(...)):
    chat = jsonable_encoder(chat)
    new_chat = await add_chat(chat)
    if new_chat.get("error") == "Chat Already added":
        return ErrorResponseModel("An error occurred.", 409, "Chat already added.")
    return ResponseModel(new_chat, "Chat added successfully.")


@router.get("/", response_description="Chats retrieved")
async def get_chats():
    users = await get_all_chats()
    if users:
        return ResponseModel(users, "Chats data retrieved successfully")
    return ResponseModel(users, "Empty list returned")


@router.get("/{id}", response_description="Chat data retrieved")
async def get_chat_data(id: str):
    user = await get_chat(id)
    if user:
        return ResponseModel(user, "Chat data retrieved successfully")
    return ErrorResponseModel("An error occurred.", 404, "Chat doesn't exist.")


# @router.patch("/{id}")
# async def add_message(id: str, req: AddMessageChatModel = Body(...)):
#     req = {k: v for k, v in req.dict().items() if v is not None}
#     updated_chat = await add_message_to_chat(id, req)
#     if updated_chat:
#         return ResponseModel(
#             "Chat with ID: {} updated successful".format(id),
#             "Chat updated successfully",
#         )
#     return ErrorResponseModel(
#         "An error occurred",
#         404,
#         "There was an error updating the chat data.",
#     )


# @router.delete("/{id}", response_description="User data deleted from the database")
# async def delete_user_data(id: int):
#     deleted_user = await delete_user(id)
#     if deleted_user:
#         return ResponseModel(
#             "User with ID: {} removed".format(id), "User deleted successfully"
#         )
#     return ErrorResponseModel(
#         "An error occurred", 404, "User with id {0} doesn't exist".format(id)
#     )
