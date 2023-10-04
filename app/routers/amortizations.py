from typing import Annotated
from fastapi import APIRouter, Query
from fastapi.responses import RedirectResponse
from app.models.amortization import (
    AmortizationType,
    LoanExtraParams,
    OutLoanAmortization,
)
from app.services.amortization_service import (
    generate_amortization_table,
)

router = APIRouter()


@router.get("/")
async def root():
    return RedirectResponse(url="/docs/")


@router.post(
    "/amortization_table",
    response_model=OutLoanAmortization,
)
def amortization_table(
    loan_params: LoanExtraParams,
    amortization_type: Annotated[
        AmortizationType, Query(alias="amortizationType")
    ] = AmortizationType.FRENCH,
):
    return generate_amortization_table(loan_params, amortization_type)
