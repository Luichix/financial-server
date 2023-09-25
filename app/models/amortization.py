from pydantic import BaseModel, Field


class LoanBaseParams(BaseModel):
    principal: float = Field(
        gt=0, title="Loan Capital", description="Principal amount of the loan"
    )
    annual_interest_rate: float = Field(
        gt=0,
        title="Annual interest rate",
        description="This value has been greater than 0",
    )
    num_payments: int = Field(
        gt=0, title="Number of payments", description="Number of months of payment"
    )


class AdditionalPayment(BaseModel):
    month: int
    payment_amount: float


class LoanInsurance(BaseModel):
    name: str
    amount: float = Field(
        gt=0, description="The amount can be a rate or fixed price", default=None
    )
    is_rate: bool = False


class DisbursementFee(BaseModel):
    amount: float = Field(gt=0, description="The amount can be a rate or fixed price")
    is_rate: bool = False


class LoanExtendParams(LoanBaseParams):
    grace_period_months: int = Field(default=0, ge=0, title="Grace period months")
    irregular_payments: list[AdditionalPayment] | None = None
    insurances: list[LoanInsurance] | None = None
    disbursement_fee: DisbursementFee | None = None


class AmortizationBase(BaseModel):
    month: int
    monthly_payment: float
    principal_payment: float
    interest_payment: float
    remaining_balance: float


class AmortizationExtend(AmortizationBase):
    irregular_payment: float | None
    insurances: dict[str, float] | None = None


class OutLoanAmortization(BaseModel):
    commission: float | None
    amortization_table: list[AmortizationExtend]
