from dependency_injector.wiring import inject, Provide
from fastapi import APIRouter, Depends

from app.core.container import Container
from app.schema.rate_conversion import RateConversion, RateConversionResult
from app.services.rate_conversion import RateConversionService

router = APIRouter(
    prefix="/conversion",
    tags=["conversion"],
)


@router.get("/request", response_model=RateConversionResult)
@inject
async def request_conversion(
    data: RateConversion = Depends(),
    service: RateConversionService = Depends(
        Provide[Container.rate_conversion_service]
    ),
):
    """Request a monetary conversion between two available currencies."""
    return await service.get_price(data)
