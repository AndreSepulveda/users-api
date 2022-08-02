from fastapi import FastAPI

from management.user import router as user_router

app = FastAPI()

app.include_router(user_router.router)