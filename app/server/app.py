from fastapi import FastAPI
from .routes.user import router as UserRouter
from .description import tags_metadata


app = FastAPI(openapi_tags=tags_metadata)


app.include_router(UserRouter, tags=["User"], prefix="/user")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this fantastic app!"}
