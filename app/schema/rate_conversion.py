from typing import Literal

from pydantic import BaseModel, Field

Currency = Literal['USD', 'BRL', 'EUR', 'BTC', 'ETH']


class RateConversion(BaseModel):
    amount: float = Field(description="Amount to convert")
    value_from: Currency = Field(description="Currency code to convert from")
    value_to: Currency = Field(description="Currency code to convert to")


class RateConversionResult(BaseModel):
    requested_amount: float
    value_from: Currency
    value_to: Currency
    amount_converted: float
