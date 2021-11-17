from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.vote import vote
from . import models
from .database import engine
from .routers import post, user, auth, vote
from .config import settings

#models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)


@app.get("/", include_in_schema=False)
def root():
    return {"message": "welcome to my api bro"}