from fastapi import APIRouter

from app.api.v1.endpoints.conversion import router as conversion_router

routers = APIRouter()
router_list = [conversion_router]

for router in router_list:
    router.tags = routers.tags.append("v1")
    routers.include_router(router)
