from ..database import database
from bson.objectid import ObjectId
from datetime import datetime

Chats = database.get_collection("chats")
# helpers


def chat_helper(chat) -> dict:
    result = {
        "id": str(chat["_id"]),
        "createdBy": chat["createdBy"],
        "users": chat["users"],
        "admins": chat["admins"],
        # "messages": chat["messages"],
        "createDate": chat["createDate"],
        "isDeleted": chat["isDeleted"],
    }
    if chat.get("updateDate"):
        result["updateDate"] = chat["updateDate"]
    return result


# Retrieve all chats present in the database
async def get_all_chats():
    chats = []
    async for chat in Chats.find({"isDeleted": False}):
        chats.append(chat_helper(chat))
    return chats


# Add a new chat into to the database
async def add_chat(chat_data: dict) -> dict:
    old_chat = Chats.find(
        {
            "createdBy": chat_data["createdBy"],
            "users": {
                "$eq": [chat_data["users"]],
            },
            "isDeleted": False,
        })
    if old_chat:
        return {"error": "Chat Already added"}
    chat_data["createDate"] = datetime.now()
    chat_data["users"].append(chat_data["createdBy"])

    if chat_data["type"] == "private":
        chat_data["admins"] = sorted(chat_data["users"])
        chat_data["messages"] = [
            {
                "sender": chat_data["createdBy"],
                "data": f"Chat created by {chat_data['createdBy']}",
                "type": "text",
                "isReplied": False,
                "createDate": datetime.now(),
                "isDeleted": False,
            }
        ]

    chat = await Chats.insert_one(chat_data)
    new_chat = await Chats.find_one(
        {
            "_id": chat.inserted_id,
        }
    )
    return chat_helper(new_chat)


# Retrieve a user with a matching ID
async def get_chat(id: str) -> dict:
    chat = await Chats.find_one(
        {
            "_id": ObjectId(id),
            "isDeleted": False
        }
    )
    print(chat)
    if chat:
        return chat_helper(chat)
    else:
        return False


# Add message to chat
async def add_message_to_chat(id: str, data: dict) -> dict:
    if len(data) < 1:
        return False
    chat = await Chats.find_one(
        {
            "_id": ObjectId(id),
            "users": {
                "$in": [data["user"]],
            },
            "isDeleted": False,
        }
    )
    if not chat:
        return False
    await Chats.update_one(
        {
            "_id": ObjectId(id),
            "users": {
                "$in": [data["user"]],
            },
            "isDeleted": False,
        },
        {
            "$push": {
                "messages": {
                    "chatId": ObjectId(id),
                    "sender": data["user"],
                    "data": data["data"],
                    "type": data["type"],
                    "isReplied": data["isReplied"],
                    "repliedMessage": ObjectId(data["repliedMessage"]),
                    "createDate": datetime.now(),
                    "isDeleted": False,
                }
            }
        }
    )
    return True


# # Update a user with a matching ID
# async def update_user(id: int, data: dict):
#     # Return false if an empty request body is sent.
#     if len(data) < 1:
#         return False
#     user = await Chats.find_one(
#         {
#             "userId": int(id),
#             "isDeleted": False,
#         }
#     )
#     if user:
#         updated_user = await Chats.update_one(
#             {
#                 "userId": int(id),
#                 "isDeleted": False,
#             }, {
#                 "$set": data,
#             }
#         )
#         if updated_user:
#             return True
#         return False
#
#
# # Delete a user from the database
# async def delete_user(id: int):
#     user = await Chats.find_one(
#         {
#             "userId": int(id),
#             "isDeleted": False,
#         }
#     )
#     if user:
#         await Chats.update_one(
#             {
#                 "userId": int(id),
#                 "isDeleted": False,
#             },
#             {
#                 "$set": {
#                     "isDeleted": True,
#                 }
#             }
#         )
#         return True
