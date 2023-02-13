
### main ###

# Documentación oficial: https://fastapi.tiangolo.com/es/

# Instala FastAPI: pip install "fastapi[all]"

from fastapi import FastAPI
from routers import products, users, basic_auth_users, jwt_auth_users, users_db
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.include_router(users.router)

app.include_router(basic_auth_users.router)

app.include_router(jwt_auth_users.router)

app.include_router(users_db.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(products.router)


# Url local: http://127.0.0.1:8000
@app.get("/")
async def root():
    return "Hola, estamos usando FastAPI!"

# Url local: http://127.0.0.1:8000/url
@app.get("/url")
async def url():
    return {"url": "https://pocho19.github.io/"}

# Inicia el server: uvicorn main:app --reload
# Detener el server: CTRL+C

# Documentación con Swagger: http://127.0.0.1:8000/docs
# Documentación con Redocly: http://127.0.0.1:8000/redoc

# Ejecución MongoDB: sudo mongod --dbpath "/path/to/data/db"
# sudo mongod --dbpath 