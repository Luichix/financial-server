from fastapi import APIRouter
from app.models.amortization import (
    AmortizationType,
    LoanBaseParams,
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
    "/generate_amortization_table",
    response_model=OutLoanAmortization,
)
def amortization_fixed_installment(
    loan_params: LoanExtendParams,
    amortization_type: AmortizationType = AmortizationType.FRENCH,
):
    return generate_amortization_table(loan_params, amortization_type)
