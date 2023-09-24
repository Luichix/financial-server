from fastapi import FastAPI
from app.routers import amortizations

app = FastAPI()


app.include_router(amortizations.router)
