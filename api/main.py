from fastapi import FastAPI, HTTPException
from sqlmodel import SQLModel, Field
from typing import List, Optional 
app = FastAPI()

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    contrasena: str  



db_users = [
    User(id=1, username="user1", contrasena="pass1"),
    User(id=2, username="user2", contrasena="abc12"), 
    User(id=3, username="user3", contrasena="21cba")
]


#crear
@app.post("/user")
def crearuser(user: User ):
    db_users.append(user)
    return user

#login

@app.post("/login")
def login (user_data: User):
    for u in db_users:
        if u.username == user_data.username and u.contrasena == user_data.contrasena:   #u.username es lo que ingresa, y username lo que tenemos 
            return{"status": "success", "mensaje": "Login exitoso"}
    raise HTTPException(status_code=401, detail="Credenciales incorrectas")

#uno por uno 
@app.get("/users/{user_id}") 
def un_user(user_id: int):
    for u in db_users:
        if u.id == user_id: ###aqui  
            return u
    raise HTTPException(status_code=404, detail="Usuario no encontrado")



#todos en lista 
@app.get("/user")
def todoususario():
    return db_users


#editar
@app.put("/user/{user_id}")
def actuuser(user_id: int, updated_data: User):
    for u in db_users:
        if u.id== user_id:
            user.username= update_data.username
            user.contrasena= update_data.contrasena
            return {"mensjae": "Usuario actualizado", "user": u}

    


#eliminar
@app.delete("/user/{user_id}")
def deletduser(user_id: int):
    for u in db_users:
        if u.id == user_id:  #### aqui 
            db_users.remove(u)
            return{"Mensaje": f"Usuario eliminado{user_id}"}





###### para la api en terminal 


#python3 -m venv venv 
#source venv/bin/activate
#python -m pip install requests
#fastapi dev

## errores 

#pip install sqlmodel 