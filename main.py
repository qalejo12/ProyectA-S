from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    name: str
    last_name: str
    cedula: int

users_list = [User(id=1, name="Alejo", last_name="Quintero", cedula= 2112243),
                User(id=2, name="Luis", last_name="Lopez", cedula= 1482634),
                User(id=3, name="Carlos", last_name="rueda", cedula= 2376534)]

@app.get("/usersjson")
async def users():
    return [{"name": "Alejo", "last_name": "Quintero", "cedula": 2112243},
            {"name": "Luis", "last_name": "Lopez", "cedula": 1482634},
            {"name": "Carlos", "last_name": "rueda", "cedula": 245365465}]

@app.get("/users")
async def users():
    return users_list

@app.get("/user/{id}")
async def users(id: int):
    return searchUser(id)

@app.get("/userquery/")
async def users(id: int):
    return searchUser(id)


def searchUser(id):
    users = filter(lambda User: User.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se a podido encontrar dicho id"}


