
from typing import List, Optional
from fastapi import FastAPI, Response
from fastapi.responses import FileResponse
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from routes.user import user
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://chat.openai.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

app.include_router(user)
