from fastapi import FastAPI
from app.api.api import router
from app.db.database import engine, Base
from app.db import models


app = FastAPI(title="ISKCON Lalitpur Backend")

Base.metadata.create_all(bind=engine)


app.include_router(router)