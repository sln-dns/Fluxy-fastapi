from fastapi import FastAPI
from users import router as users_router
from gtin_routes import router as gtin_router
app = FastAPI()

app.include_router(users_router)
app.include_router(gtin_router)

@app.get("/")
def read_root():
    return {"Hello": "World"}