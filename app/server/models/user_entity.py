from datetime import datetime
from ..database import database

Users = database.get_collection("users")
# helpers


def user_helper(user) -> dict:
    result = {
        "id": str(user["_id"]),
        "email": str(user["email"]),
        "userId": user["userId"],
        "isDeleted": user["isDeleted"],
        "createDate": user["createDate"],
    }
    if user.get("updateDate"):
        result["updateDate"] = user["updateDate"]
    return result


# Retrieve all users present in the database
async def get_all_users(skip, limit):
    users = []
    async for user in Users.find({"isDeleted": False}).skip(skip).limit(limit):
        users.append(user_helper(user))
    return users


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    old_user = await Users.find_one(
        {
            "userId": user_data["userId"],
            "email": user_data["email"],
            "isDeleted": False,
        })
    if old_user:
        return "User Already added"
    user_data["createDate"] = datetime.now()
    user = await Users.insert_one(user_data)
    new_user = await Users.find_one(
        {
            "_id": user.inserted_id,
        }
    )
    return user_helper(new_user)


# Retrieve a user with a matching ID
async def get_user(id: int) -> dict:
    user = await Users.find_one(
        {
            "userId": int(id),
            "isDeleted": False,
        }
    )
    if user:
        return user_helper(user)


# Update a user with a matching ID
async def update_user(id: int, data: dict):
    # Return false if an empty request body is sent.
    if len(data) < 1:
        return False
    user = await Users.find_one(
        {
            "userId": int(id),
            "isDeleted": False,
        }
    )
    if user:
        updated_user = await Users.update_one(
            {
                "userId": int(id),
                "isDeleted": False,
            }, {
                "$set": data,
            }
        )
        if updated_user:
            return True
        return False


# Delete a user from the database
async def delete_user(id: int):
    user = await Users.find_one(
        {
            "userId": int(id),
            "isDeleted": False,
        }
    )
    if user:
        await Users.update_one(
            {
                "userId": int(id),
                "isDeleted": False,
            },
            {
                "$set": {
                    "isDeleted": True,
                    "updateDate": datetime.now(),
                }
            }
        )
        return True
