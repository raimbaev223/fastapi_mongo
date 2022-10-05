import motor.motor_asyncio
import os
from dotenv.main import load_dotenv


load_dotenv()
mongo_host = os.environ["MONGO_HOST"]
mongo_port = os.environ["MONGO_PORT"]
mongo_details = f'{mongo_host}:{mongo_port}'
client = motor.motor_asyncio.AsyncIOMotorClient(mongo_details)
database = client.chatFastApi
print('<<<<<< Connection with mongoDB successfully established >>>>>>')
