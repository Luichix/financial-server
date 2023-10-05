from enum import Enum
from pydantic import BaseModel, Field


class AmortizationType(str, Enum):
    FRENCH = "French"
    GERMAN = "German"
    AMERICAN = "American"


class FrecuencyType(str, Enum):
    PERIOD = "period"
    RATE = "rate"


class PaymentFrecuency(str, Enum):
    ANNUAL = "annual"
    SEMIANNUAL = "semiannual"
    QUARTERLY = "quarterly"
    BIMONTHLY = "bimonthly"
    MONTHLY = "monthly"
    BIWEEKLY = "biweekly"
    WEEKLY = "weekly"
    DAILY = "daily"


class FactorFrequency:
    factors = {
        "annual": 1,
        "semiannual": 2,
        "quarterly": 4,
        "bimonthly": 6,
        "monthly": 12,
        "biweekly": 26,
        "weekly": 52,
        "daily": 360,
    }

    @classmethod
    def __getitem__(cls, key):
        return cls.factors[key]


# Loan Base Params
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
    periods_number: int = Field(
        gt=0,
        title="Number of periods",
        description="Number of periods",
        alias="periodsNumber",
    )


class LoanFrecuencyParams(LoanBaseParams):
    payment_frecuency: PaymentFrecuency = Field(
        title="Payment frecuency",
        description="Diferent types of frecuency payments",
        alias="paymentFrecuency",
        default=PaymentFrecuency.MONTHLY,
    )
    interest_rate_type: PaymentFrecuency = Field(
        title="Interest Rate Type",
        description="This field determine the type of the interest rate",
        alias="interestRateType",
        default=PaymentFrecuency.ANNUAL,
    )
    periods_type: PaymentFrecuency = Field(
        title="Periods frecuency type",
        description="This field determine the frecuency type of the periods",
        alias="periodsType",
        default=PaymentFrecuency.MONTHLY,
    )
    grace_period: int = Field(
        default=0,
        ge=0,
        title="Grace period",
        description="Grace period agree the frecuency payments",
        alias="gracePeriod",
    )


class DisbursementFee(BaseModel):
    amount: float = Field(gt=0, description="The amount can be a rate or fixed price")
    is_rate: bool = Field(alias="isRate", default=False)


class AdditionalPayment(BaseModel):
    period: int
    payment_amount: float = Field(alias="paymentAmount")


class RecurringPayment(BaseModel):
    name: str
    amount: float = Field(
        gt=0, description="The amount can be a rate or fixed price", default=None
    )
    is_rate: bool = Field(alias="isRate", default=False)


class LoanExtraParams(LoanFrecuencyParams):
    additional_payments: list[AdditionalPayment] | None = Field(
        default=None, alias="additionalPayments"
    )
    recurring_payments: list[RecurringPayment] | None = None
    disbursement_fee: DisbursementFee | None = Field(
        default=None, alias="disbursementFee"
    )


# OUTPUT
class OutLoanBaseParams(BaseModel):
    fee_payment: float = Field(alias="feePayment")
    interest_payment: float = Field(alias="interestPayment")
    additional_payment: float | None = Field(default=None, alias="additionalPayment")
    recurring_payments: dict[str, float] | None = Field(
        alias="recurringPayments",
        default=None,
    )


class OutAmortizationBase(OutLoanBaseParams):
    period: int
    principal_payment: float = Field(alias="principalPayment")
    remaining_balance: float = Field(alias="remainingBalance")


class OutAmortizationExtra(OutLoanBaseParams):
    total_amount_pay: float = Field(alias="totalAmountPay")
    number_installments: int = Field(alias="numberInstallments")
    disbursement_fee: float | None = Field(
        alias="disbursementFee",
        default=None,
    )
    amortization_table: list[OutAmortizationBase] = Field(
        title="Amortization Table", alias="amortizationTable"
    )


class OutLoanAmortization(LoanFrecuencyParams, OutAmortizationExtra):
    pass
