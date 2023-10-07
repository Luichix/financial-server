from enum import Enum
from pydantic import BaseModel, Field


class TypeCalculation(str, Enum):
    PRINCIPAL = "Principal"
    RATE = "Rate"
    PERIOD = "Period"
    INTEREST = "Interest"
    FUTURE = "Future"


class FinancialCalculation(BaseModel):
    principal: float = Field(default=0)
    interest_rate: float = Field(default=0)
    period: int = Field(default=0)
    interest: float = Field(default=0)
    future: float = Field(default=0)
