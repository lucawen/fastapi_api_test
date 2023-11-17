from typing import Literal

from pydantic import BaseModel, Field

Currency = Literal['USD', 'BRL', 'EUR', 'BTC', 'ETH']


class RateConversion(BaseModel):
    """Rate conversion transaction data."""

    amount: float = Field(description="Amount to convert")
    value_from: Currency = Field(description="Currency code to convert from")
    value_to: Currency = Field(description="Currency code to convert to")


class RateConversionResult(BaseModel):
    """A result data for the rate conversion.

    Contains the requested data and the result."""

    requested_amount: float
    value_from: Currency
    value_to: Currency
    amount_converted: float
