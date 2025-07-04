from fastapi import FastAPI
from api.v1 import views

app = FastAPI()

app.include_router(views.router, prefix="/api/v1/tasks", tags=["tasks"])
