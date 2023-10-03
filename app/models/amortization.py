from enum import Enum
from pydantic import BaseModel, Field


class AmortizationType(str, Enum):
    FRENCH = "French"
    GERMAN = "German"
    AMERICAN = "American"


class LoanBaseParams(BaseModel):
    principal: float = Field(
        gt=0, title="Loan Capital", description="Principal amount of the loan"
    )
    interest_rate: float = Field(
        gt=0,
        title="Interest rate",
        description="This value has been greater than 0",
        alias="interestRate",
    )
    num_payments: int = Field(
        gt=0,
        title="Number of payments",
        description="Number of months of payment",
        alias="numPayments",
    )


class AdditionalPayment(BaseModel):
    month: int
    payment_amount: float = Field(alias="paymentAmount")


class LoanInsurance(BaseModel):
    name: str
    amount: float = Field(
        gt=0, description="The amount can be a rate or fixed price", default=None
    )
    is_rate: bool = Field(alias="isRate", default=False)


class DisbursementFee(BaseModel):
    amount: float = Field(gt=0, description="The amount can be a rate or fixed price")
    is_rate: bool = Field(alias="isRate", default=False)


class LoanExtendParams(LoanBaseParams):
    grace_period_months: int = Field(
        default=0, ge=0, title="Grace period months", alias="gracePeriodMonths"
    )
    additional_payments: list[AdditionalPayment] | None = Field(
        default=None, alias="additionalPayments"
    )
    insurances: list[LoanInsurance] | None = None
    disbursement_fee: DisbursementFee | None = Field(
        default=None, alias="disbursementFee"
    )


class AmortizationBase(BaseModel):
    month: int
    monthly_payment: float = Field(alias="monthlyPayment")
    principal_payment: float = Field(alias="principalPayment")
    interest_payment: float = Field(alias="interestPayment")
    remaining_balance: float = Field(alias="remainingBalance")


class AmortizationExtend(AmortizationBase):
    additional_payment: float | None = Field(default=None, alias="additionalPayment")
    insurances: dict[str, float] | None = None


class OutLoanAmortization(LoanBaseParams):
    total_monthly_payment: float = Field(
        alias="totalMonthlyPayment",
    )
    total_interest_payment: float = Field(
        alias="totalInterestPayment",
    )
    total_additional_payment: float | None = Field(
        alias="totalAdditionalPayment",
        default=None,
    )
    total_insurances: dict[str, float] | None = Field(
        alias="totalInsurances",
        default=None,
    )
    commission: float | None = Field(
        alias="commission",
        default=None,
    )
    amortization_table: list[AmortizationExtend] = Field(alias="amortizationTable")
