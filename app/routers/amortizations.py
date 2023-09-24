from fastapi import APIRouter
from app.models.amortization import (
    LoanSinglePeriodsParams,
    LoanVariablePeriodsParams,
    LoanAnnuitiesParams,
    LoanConstantCapitalParams,
    LoanPeriodGraceParams,
    LoanIrregularParams,
    LoanAdditionalPaymentsParams,
)
from app.services.amortization_service import (
    generate_amortization_table_annuities,
    generate_amortization_table_constant_principal,
    generate_amortization_table_cuota_decreciente,
    generate_amortization_table_cuota_fija,
    generate_amortization_table_intereses_fijos,
    generate_amortization_table_irregular,
    generate_amortization_table_variable_periods,
    generate_amortization_table_with_additional_payments,
    generate_amortization_table_with_grace_period,
)

router = APIRouter()


@router.get("/")
async def root():
    return {"Hello": "Hello World"}


@router.post("/generate_amortization_table_cuota_fija", response_model=list[dict])
def amortization_cuota_fija(loan_params: LoanSinglePeriodsParams):
    return generate_amortization_table_cuota_fija(loan_params)


@router.post(
    "/generate_amortization_table_cuota_decreciente", response_model=list[dict]
)
def amortization_cuota_decreciente(loan_params: LoanSinglePeriodsParams):
    return generate_amortization_table_cuota_decreciente(loan_params)


@router.post("/generate_amortization_table_intereses_fijos", response_model=list[dict])
def amortization_intereses_fijos(loan_params: LoanSinglePeriodsParams):
    return generate_amortization_table_intereses_fijos(loan_params)


@router.post("/generate_amortization_table_variable_periods", response_model=list[dict])
def amortization_variable_periods(
    loan_params: LoanVariablePeriodsParams,
):
    return generate_amortization_table_variable_periods(loan_params)


@router.post("/generate_amortization_table_annuities", response_model=list[dict])
def amortization_annuities(loan_params: LoanAnnuitiesParams):
    return generate_amortization_table_annuities(loan_params)


@router.post(
    "/generate_amortization_table_constant_principal", response_model=list[dict]
)
def amortization_constant_principal(
    loan_params: LoanConstantCapitalParams,
):
    return generate_amortization_table_constant_principal(loan_params)


@router.post(
    "/generate_amortization_table_with_grace_period", response_model=list[dict]
)
def amortization_with_grace_period(loan_params: LoanPeriodGraceParams):
    return generate_amortization_table_with_grace_period(loan_params)


@router.post("/generate_amortization_table_irregular", response_model=list[dict])
def amortization_irregular(loan_params: LoanIrregularParams):
    return generate_amortization_table_irregular(loan_params)


@router.post(
    "/generate_amortization_table_with_additional_payments", response_model=list[dict]
)
def amortization_with_additional_payments(
    loan_params: LoanAdditionalPaymentsParams,
):
    return generate_amortization_table_with_additional_payments(loan_params)
