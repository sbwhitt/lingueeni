from fastapi.middleware.cors import CORSMiddleware
from linguee_api import api

app = api.app

origins = [
    "http://localhost:4200",
    "https://sbwhitt.github.io"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
