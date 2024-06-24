from fastapi import APIRouter

from src.api.routes.host import router as host_router

router = APIRouter()

router.include_router(host_router, prefix="/hosts")
