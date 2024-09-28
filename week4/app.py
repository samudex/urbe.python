from fastapi import FastAPI

# importando rutas
from routes.books import router as books_router
from routes.users import router as users_router

app = FastAPI()

app.include_router(books_router)
app.include_router(users_router)