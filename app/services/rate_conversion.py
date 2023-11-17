from abc import ABC, abstractmethod
from app.schema.rate_conversion import RateConversion, RateConversionResult

from app.repository.rate_conversion import RateConversionRepository


class RateConversionService(ABC):
    @abstractmethod
    async def get_price(self, conversion_data: RateConversion) -> float:
        """Get the price conversion from two currencies.

        Args:
            conversion_data (RateConversion): A rate conversion data object that
            contains the necessary information to get the price conversion.

        Returns:
            float: the converted price.
        """
        ...


class RateConversionBaseService(RateConversionService):
    def __init__(self, rate_repository: RateConversionRepository):
        self.rate_repository = rate_repository

    async def get_price(self, conversion_data: RateConversion) -> float:
        price = await self.rate_repository.get_price(
            conversion_data.value_from, conversion_data.value_to, conversion_data.amount
        )
        return RateConversionResult(
            requested_amount=conversion_data.amount,
            value_from=conversion_data.value_from,
            value_to=conversion_data.value_to,
            amount_converted=price
        )
