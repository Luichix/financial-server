from typing import Annotated
from fastapi import APIRouter, Query
from app.models.calculator import FinancialParams, CalculationType

from app.services.calculator_service import calculate_interest_simple

router = APIRouter()


@router.post("/calculate_simple_interest")
def calculate_interest_simple_router(
    financial_params: FinancialParams,
    calculation_type: Annotated[
        CalculationType, Query(alias="calculationType")
    ] = CalculationType.INTEREST,
) -> float:
    return calculate_interest_simple(
        financial_params=financial_params, calculation_type=calculation_type
    )
