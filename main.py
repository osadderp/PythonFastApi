from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

#main
app=FastAPI()

#array
items=[]

#array for class user
useres=[]

class User(BaseModel):
    id:int=0
    firtName:str=None
    lastName:str=None
    

@app.get("/")
def root():
    #return ("Hola soy FastApi.")
    return{"Hola":"Soy FastApi"}

@app.post("/items")
def add(item: str):
    items.append(item)
    return items

@app.get("/listItems")
def listItems():
    return items#items[1]


@app.get("/item")
def item(id:int):
    return items[id]

@app.get("/item/{id}")
def item(id:int):
    try:
      item=items[id]
    except Exception as e:
       raise HTTPException(status_code=404,detail="Not Found")#return(f"Ocurrió un error: {e}")
    return item

@app.post("/addUser")
def addUser(addUser:User):
    useres.append(addUser)
    return useres

