from enum import Enum
from pydantic import BaseModel, Field


class CalculationType(str, Enum):
    INTEREST = "Interest"
    RATE = "Rate"
    PRINCIPAL = "Principal"
    FUTURE = "Future"
    PERIOD = "Period"


class PeriodType(str, Enum):
    YEARS = "years"
    MONTHS = "Months"
    DAYS = "Days"


class FinancialParams(BaseModel):
    principal: float | None = Field(default=None)
    interest_rate: float | None = Field(default=None)  # as a percentage
    period: int | None = Field(default=None)  # in years
    type_period: PeriodType | None = Field(default=None)
    interest: float | None = Field(default=None)
    future: float | None = Field(default=None)
