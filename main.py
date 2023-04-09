import os.path
from fastapi import FastAPI, Response, Request, Form, status
from pydantic import BaseModel
from fastapi.responses import RedirectResponse

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

root = os.path.dirname(os.path.abspath(__file__))
app = FastAPI()

class Page(BaseModel):
    Url: str

@app.get("/")
async def page():
    with open(os.path.join(root, 'index.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")


@app.post('/submit')
async def add(request: Request, url: str = Form(...)):
    options = webdriver.ChromeOptions()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-extensions')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get(url)

    time.sleep(1)
    return RedirectResponse(url=app.url_path_for("page"),status_code=status.HTTP_303_SEE_OTHER)

@app.post('/index')
async def add():
    with open(os.path.join(root, 'page.html')) as fh:
        data = fh.read()
    return Response(content=data, media_type="text/html")
































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



