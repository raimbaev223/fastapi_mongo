from ..database import database

users_collection = database.get_collection("users_collection")
# helpers


def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "email": str(user["email"]),
        "userId": user["userId"],
        "isDeleted": user["isDeleted"],
    }


# Retrieve all users present in the database
async def retrieve_users():
    users = []
    async for user in users_collection.find({"isDeleted": False}):
        users.append(user_helper(user))
    return users


# Add a new user into to the database
async def add_user(user_data: dict) -> dict:
    old_user = await users_collection.find_one(
        {
            "userId": user_data["userId"],
            "email": user_data["email"],
            "isDeleted": False,
        })
    if old_user:
        return "User Already added"
    user = await users_collection.insert_one(user_data)
    new_user = await users_collection.find_one(
        {
            "_id": user.inserted_id,
            "isDeleted": False,
        }
    )
    return user_helper(new_user)


# Retrieve a user with a matching ID
async def retrieve_user(id: int) -> dict:
    user = await users_collection.find_one(
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
    user = await users_collection.find_one(
        {
            "userId": int(id),
            "isDeleted": False,
        }
    )
    if user:
        updated_user = await users_collection.update_one(
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
    user = await users_collection.find_one(
        {
            "userId": int(id),
            "isDeleted": False,
        }
    )
    if user:
        await users_collection.update_one(
            {
                "userId": int(id),
                "isDeleted": False,
            },
            {
                "$set": {
                    "isDeleted": True,
                }
            }
        )
        return True
