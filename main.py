from fastapi import FastAPI

from management.user import router as user_router
from management.country import router as country_router

app = FastAPI()

app.include_router(user_router.router)
app.include_router(country_router.router)