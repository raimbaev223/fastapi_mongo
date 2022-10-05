from fastapi import FastAPI
from .routes.user import router as UserRouter
from .routes.chat import router as ChatRouter
from .description import tags_metadata



app = FastAPI(openapi_tags=tags_metadata)

app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(ChatRouter, tags=["Chat"], prefix="/chat")


@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to ChatAPI!"}
