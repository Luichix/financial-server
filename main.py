from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class LoanParams(BaseModel):
    principal: float
    interest_rate: float

class LoanSinglePeriodsParams(LoanParams):
    num_payments: int


class LoanVariablePeriodsParams(LoanParams):
    payments_schedule: list[dict]

class LoanAnnuitiesParams(BaseModel):
    principal: float
    annual_interest_rate: float
    num_years: int

class LoanConstantCapitalParams(BaseModel):
    principal: float
    annual_interest_rate: float
    num_years: int

class LoanPeriodGraceParams(BaseModel):
    principal: float
    annual_interest_rate: float
    num_years: int
    grace_period_months: int

class IrregularPayment(BaseModel):
    month: int
    payment_amount: float

class LoanIrregularParams(BaseModel):
    principal: float
    annual_interest_rate: float
    num_years: int
    irregular_payments: list[IrregularPayment]

class AdditionalPayment(BaseModel):
    month: int
    payment_amount: float

class LoanAdditionalPaymentsParams(BaseModel):
    principal: float
    annual_interest_rate: float
    num_years: int
    additional_payments: list[AdditionalPayment]


@app.get("/")
async def root():
    return {"Hello": "Hello World"}   
#0
@app.post("/generate_amortization_table", response_model=list[dict])
def generate_amortization_table(loan_params: LoanSinglePeriodsParams):
    principal = loan_params.principal
    interest_rate = loan_params.interest_rate / 100.0
    num_payments = loan_params.num_payments

    monthly_interest_rate = interest_rate / 12.0
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    amortization_table = []
    remaining_balance = principal

    for month in range(1, num_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment

        amortization_table.append({
            "Month": month,
            "Principal Payment": principal_payment,
            "Interest Payment": interest_payment,
            "Remaining Balance": remaining_balance
        })

    return amortization_table

#1
@app.post("/generate_amortization_table_cuota_fija", response_model=list[dict])
def generate_amortization_table_cuota_fija(loan_params: LoanSinglePeriodsParams):
    principal = loan_params.principal
    interest_rate = loan_params.interest_rate / 100.0
    num_payments = loan_params.num_payments

    monthly_interest_rate = interest_rate / 12.0
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    amortization_table = []
    remaining_balance = principal

    for month in range(1, num_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment

        amortization_table.append({
            "Month": month,
            "Principal Payment": principal_payment,
            "Interest Payment": interest_payment,
            "Remaining Balance": remaining_balance
        })

    return amortization_table
#2
@app.post("/generate_amortization_table_cuota_decreciente", response_model=list[dict])
def generate_amortization_table_cuota_decreciente(loan_params: LoanSinglePeriodsParams):

    principal = loan_params.principal
    interest_rate = loan_params.interest_rate / 100.0
    num_payments = loan_params.num_payments

    monthly_interest_rate = interest_rate / 12.0
    monthly_principal_payment = principal / num_payments

    amortization_table = []
    remaining_balance = principal

    for month in range(1, num_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        remaining_balance -= monthly_principal_payment

        amortization_table.append({
            "Month": month,
            "Principal Payment": monthly_principal_payment,
            "Interest Payment": interest_payment,
            "Remaining Balance": remaining_balance
        })

    return amortization_table

#3
@app.post("/generate_amortization_table_intereses_fijos", response_model=list[dict])
def generate_amortization_table_intereses_fijos(loan_params: LoanSinglePeriodsParams):
    principal = loan_params.principal
    interest_rate = loan_params.interest_rate / 100.0
    num_payments = loan_params.num_payments

    monthly_interest_payment = (principal * interest_rate) / 12.0
    amortization_table = []

    for month in range(1, num_payments + 1):
        amortization_table.append({
            "Month": month,
            "Principal Payment": 0,  # En intereses fijos, el principal no se paga
            "Interest Payment": monthly_interest_payment,
            "Remaining Balance": principal
        })

    return amortization_table


#4
def calculate_amortization_table_with_variable_periods(principal, interest_rate, payments_schedule):
    monthly_interest_rate = interest_rate / 100.0 / 12.0
    amortization_table = []
    remaining_balance = principal

    for payment in payments_schedule:
        month = payment["month"]
        payment_amount = payment["payment_amount"]

        if month == 0:
            interest_payment = 0
            principal_payment = 0
        else:
            interest_payment = remaining_balance * monthly_interest_rate
            principal_payment = payment_amount - interest_payment

        remaining_balance -= principal_payment

        amortization_table.append({
            "Month": month,
            "Principal Payment": principal_payment,
            "Interest Payment": interest_payment,
            "Remaining Balance": remaining_balance
        })

    return amortization_table

@app.post("/generate_amortization_table_variable_periods", response_model=list[dict])
def generate_amortization_table_variable_periods(loan_params: LoanVariablePeriodsParams):
    principal = loan_params.principal
    interest_rate = loan_params.interest_rate / 100.0
    payments_schedule = loan_params.payments_schedule

    amortization_table = calculate_amortization_table_with_variable_periods(principal, interest_rate, payments_schedule)

    return amortization_table


#5
def calculate_amortization_table_annuities(principal, annual_interest_rate, num_years):
    monthly_interest_rate = annual_interest_rate / 100.0 / 12.0
    num_payments = num_years * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    amortization_table = []
    remaining_balance = principal

    for month in range(1, num_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment

        amortization_table.append({
            "Month": month,
            "Principal Payment": principal_payment,
            "Interest Payment": interest_payment,
            "Remaining Balance": remaining_balance
        })

    return amortization_table

@app.post("/generate_amortization_table_annuities", response_model=list[dict])
def generate_amortization_table_annuities(loan_params: LoanAnnuitiesParams):
    principal = loan_params.principal
    annual_interest_rate = loan_params.annual_interest_rate
    num_years = loan_params.num_years

    amortization_table = calculate_amortization_table_annuities(principal, annual_interest_rate, num_years)

    return amortization_table


#6
def calculate_amortization_table_constant_principal(principal, annual_interest_rate, num_years):
    monthly_interest_rate = annual_interest_rate / 100.0 / 12.0
    num_payments = num_years * 12
    monthly_principal_payment = principal / num_payments

    amortization_table = []
    remaining_balance = principal

    for month in range(1, num_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_principal_payment
        remaining_balance -= principal_payment

        amortization_table.append({
            "Month": month,
            "Principal Payment": principal_payment,
            "Interest Payment": interest_payment,
            "Remaining Balance": remaining_balance
        })

    return amortization_table

@app.post("/generate_amortization_table_constant_principal", response_model=list[dict])
def generate_amortization_table_constant_principal(loan_params: LoanConstantCapitalParams):
    principal = loan_params.principal
    annual_interest_rate = loan_params.annual_interest_rate
    num_years = loan_params.num_years

    amortization_table = calculate_amortization_table_constant_principal(principal, annual_interest_rate, num_years)

    return amortization_table

#7
def calculate_amortization_table_with_grace_period(principal, annual_interest_rate, num_years, grace_period_months):
    monthly_interest_rate = annual_interest_rate / 100.0 / 12.0
    num_payments = num_years * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    amortization_table = []
    remaining_balance = principal

    for month in range(1, num_payments + 1):
        if month <= grace_period_months:
            interest_payment = remaining_balance * monthly_interest_rate
            principal_payment = 0
        else:
            interest_payment = remaining_balance * monthly_interest_rate
            principal_payment = monthly_payment - interest_payment

        remaining_balance -= principal_payment

        amortization_table.append({
            "Month": month,
            "Principal Payment": principal_payment,
            "Interest Payment": interest_payment,
            "Remaining Balance": remaining_balance
        })

    return amortization_table

@app.post("/generate_amortization_table_with_grace_period", response_model=list[dict])
def generate_amortization_table_with_grace_period(loan_params: LoanPeriodGraceParams):
    principal = loan_params.principal
    annual_interest_rate = loan_params.annual_interest_rate
    num_years = loan_params.num_years
    grace_period_months = loan_params.grace_period_months

    amortization_table = calculate_amortization_table_with_grace_period(principal, annual_interest_rate, num_years, grace_period_months)

    return amortization_table

#8
def calculate_amortization_table_irregular(principal, annual_interest_rate, num_years, irregular_payments):
    monthly_interest_rate = annual_interest_rate / 100.0 / 12.0
    num_payments = num_years * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    amortization_table = []
    remaining_balance = principal
    irregular_payments = sorted(irregular_payments, key=lambda x: x["month"])  # Ordenar los pagos irregulares por mes

    for month in range(1, num_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate

        # Comprobar si hay un pago irregular en este mes
        irregular_payment = next((payment["payment_amount"] for payment in irregular_payments if payment["month"] == month), 0)

        principal_payment = monthly_payment - interest_payment + irregular_payment
        remaining_balance -= principal_payment

        amortization_table.append({
            "Month": month,
            "Principal Payment": principal_payment,
            "Interest Payment": interest_payment,
            "Irregular Payment": irregular_payment,
            "Remaining Balance": remaining_balance
        })

    return amortization_table


@app.post("/generate_amortization_table_irregular", response_model=list[dict])
def generate_amortization_table_irregular(loan_params: LoanIrregularParams):
    principal = loan_params.principal
    annual_interest_rate = loan_params.annual_interest_rate
    num_years = loan_params.num_years
    irregular_payments = loan_params.irregular_payments

    amortization_table = calculate_amortization_table_irregular(principal, annual_interest_rate, num_years, irregular_payments)

    return amortization_table


#9
def calculate_amortization_table_with_additional_payments(principal, annual_interest_rate, num_years, additional_payments):
    monthly_interest_rate = annual_interest_rate / 100.0 / 12.0
    num_payments = num_years * 12
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)

    amortization_table = []
    remaining_balance = principal

    additional_payments = sorted(additional_payments, key=lambda x: x.month)

    for month in range(1, num_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment

        for payment in additional_payments:
            if payment.month == month:
                remaining_balance -= payment.payment_amount

        amortization_table.append({
            "Month": month,
            "Principal Payment": principal_payment,
            "Interest Payment": interest_payment,
            "Additional Payment": sum(payment.payment_amount for payment in additional_payments if payment.month == month),
            "Remaining Balance": remaining_balance
        })

    return amortization_table

@app.post("/generate_amortization_table_with_additional_payments", response_model=list[dict])
def generate_amortization_table_with_additional_payments(loan_params: LoanAdditionalPaymentsParams):
    principal = loan_params.principal
    annual_interest_rate = loan_params.annual_interest_rate
    num_years = loan_params.num_years
    additional_payments = loan_params.additional_payments

    amortization_table = calculate_amortization_table_with_additional_payments(principal, annual_interest_rate, num_years, additional_payments)

    return amortization_table

