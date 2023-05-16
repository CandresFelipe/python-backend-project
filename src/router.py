from fastapi import APIRouter

from item.routes import router as item_router

router = APIRouter()

router.include_router(router=item_router, prefix="/create-item", tags=["create-item"])
