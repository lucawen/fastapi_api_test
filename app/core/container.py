from dependency_injector import containers, providers

from app.repository import CoinApiRateConversionRepository
from app.services import RateConversionBaseService

from app.core.config import settings


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "app.api.v1.endpoints.conversion",
        ]
    )

    rate_conversion_repository = providers.Factory(
        CoinApiRateConversionRepository, api_key=settings.COIN_API_TOKEN
    )

    rate_conversion_service = providers.Factory(
        RateConversionBaseService, rate_repository=rate_conversion_repository
    )
