from fastapi import FastAPI
from .api import v1_api_router
from .core import settings
from starlette.middleware.cors import CORSMiddleware


app = FastAPI()

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS_ALLOW_ALL:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
else:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


app.include_router(v1_api_router)
