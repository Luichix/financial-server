from fastapi import APIRouter
from app.models.amortization import (
    LoanBaseParams,
    LoanExtendParams,
    OutLoanAmortization,
)
from app.services.amortization_service import (
    generate_amortization_table_constant_principal,
    generate_amortization_table_fixed_installment,
    generate_amortization_table_only_interest,
)

router = APIRouter()


@router.get("/")
async def root():
    return {"Hello": "Hello World"}


@router.post(
    "/generate_amortization_table_fixed_installment", response_model=OutLoanAmortization
)
def amortization_fixed_installment(loan_params: LoanExtendParams):
    return generate_amortization_table_fixed_installment(loan_params)


@router.post(
    "/generate_amortization_table_constant_principal", response_model=list[dict]
)
def amortization_constant_principal(
    loan_params: LoanBaseParams,
):
    return generate_amortization_table_constant_principal(loan_params)


@router.post("/generate_amortization_table_only_interest", response_model=list[dict])
def amortization_fixed_interest(loan_params: LoanBaseParams):
    return generate_amortization_table_only_interest(loan_params)
