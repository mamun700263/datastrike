from fastapi import FastAPI
from routers.amazon import search as amazon_search_router

app = FastAPI()

app.include_router(amazon_search_router.router)
