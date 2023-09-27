from typing import Annotated
from fastapi import APIRouter, Query
from app.models.amortization import (
    AmortizationType,
    LoanExtendParams,
    OutLoanAmortization,
)
from app.services.amortization_service import (
    generate_amortization_table,
)

router = APIRouter()


@router.get("/")
async def root():
    return {"Hello": "Hello World"}


@router.post(
    "/amortization_table",
    response_model=OutLoanAmortization,
)
def amortization_table(
    loan_params: LoanExtendParams,
    amortization_type: Annotated[
        AmortizationType, Query(alias="amortizationType")
    ] = AmortizationType.FRENCH,
):
    return generate_amortization_table(loan_params, amortization_type)
