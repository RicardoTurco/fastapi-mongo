import logging

from fastapi import APIRouter, Response, status

logger = logging.getLogger(__name__)

health_router = APIRouter()

TAG = "Health Check"


@health_router.get(
    "/health-check",
    tags=[TAG],
    summary="Check status of application.",
    description="This endpoint returns a health check of application.",
)
async def health_check(response: Response):
    """
    This endpoint returns a health check of application.

    :param response: Response of endpoint.
    :return: health check of application.
    """
    logger.info("*** starting GET health-check endpoint")
    response.status_code = status.HTTP_200_OK
    logger.info("*** finishing GET health-check endpoint")
    return {"application": True}
