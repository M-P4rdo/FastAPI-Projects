from fastapi import FastAPI
from app.routers import products

app = FastAPI(title="User Management API")

app.include_router(products.router)