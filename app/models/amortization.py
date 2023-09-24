from pydantic import BaseModel


class LoanBaseParams(BaseModel):
    principal: float
    annual_interest_rate: float
    num_years: int


class LoanSinglePeriodsParams(BaseModel):
    principal: float
    annual_interest_rate: float
    num_payments: int


class LoanVariablePeriodsParams(LoanBaseParams):
    payments_schedule: list[dict]


class LoanAnnuitiesParams(LoanBaseParams):
    pass


class LoanConstantCapitalParams(LoanBaseParams):
    pass


class LoanPeriodGraceParams(LoanBaseParams):
    grace_period_months: int


class IrregularPayment(BaseModel):
    month: int
    payment_amount: float


class LoanIrregularParams(LoanBaseParams):
    irregular_payments: list[IrregularPayment]


class AdditionalPayment(BaseModel):
    month: int
    payment_amount: float


class LoanAdditionalPaymentsParams(LoanBaseParams):
    additional_payments: list[AdditionalPayment]
