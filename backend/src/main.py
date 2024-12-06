from fastapi import FastAPI

import pymongo

from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# username = os.getenv("MONGO_USER")
# password = os.getenv("MONGO_PASSWORD")
# host = os.getenv("MONGO_HOST")
# port = int(os.getenv("MONGO_PORT"))
#
# myclient = pymongo.MongoClient(f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin")
#
# mydb = myclient["mydatabase"]
#
# mycol = mydb["customers"]
#
# mydict = { "name": "John", "address": "Highway 37" }
#
# x = mycol.insert_one(mydict)
#
# print(x)

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}