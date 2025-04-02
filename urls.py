from fastapi.routing import APIRouter

from app.routes.v1 import health_check
from app.routes.v1 import books

router_v1 = APIRouter(prefix="/v1")


router_v1.include_router(router=health_check.health_router)
router_v1.include_router(router=books.books_router)
