from abc import ABC, abstractmethod

import requests

from app.core.exceptions import UnknownError


class RateConversionRepository(ABC):
    @abstractmethod
    async def get_price(
        self, from_currency: str, to_currency: str, amount: float
    ) -> float:
        ...


class CoinApiRateConversionRepository(RateConversionRepository):
    def __init__(self, api_key: str):
        self.api_key = api_key

    async def get_price(
        self, from_currency: str, to_currency: str, amount: float
    ) -> float:
        # Simulating the use of the self.api_key, as we are using a static api.
        currency_req = from_currency.lower()
        currency_parser = to_currency.lower()
        url_base = f"latest/currencies/{currency_req}.min.json"
        url_req = f"https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/{url_base}"
        try:
            response = requests.get(url_req)
            response.raise_for_status()
            response_json = response.json()
            amount_base = response_json[currency_req][currency_parser]
        except Exception:
            raise UnknownError(
                "Unknown error happened when trying to process your data."
            )
        return amount_base * amount
