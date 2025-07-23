from fastapi import FastAPI
from app.routers import transcriber

app = FastAPI(title="AI Video Creator Engine")

app.include_router(transcriber.router)
