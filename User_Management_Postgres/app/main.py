from fastapi import FastAPI
from app.routers import users
from app.routers import auth

app = FastAPI(title="User Management API")

app.include_router(auth.router)
app.include_router(users.router)