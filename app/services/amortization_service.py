from app.models.amortization import (
    AdditionalPayment,
    DisbursementFee,
    LoanBaseParams,
    LoanExtendParams,
    LoanInsurance,
    OutLoanAmortization,
)


def create_amortization_entry(
    month: int,
    monthly_payment: float,
    principal_payment: float,
    interest_payment: float,
    remaining_balance: float,
):
    return {
        "month": month,
        "monthly_payment": round(monthly_payment, 2),
        "principal_payment": round(principal_payment, 2),
        "interest_payment": round(interest_payment, 2),
        "remaining_balance": round(remaining_balance, 2),
    }


# 1 Amortization table fixed installment - system French
def generate_amortization_table_fixed_installment(
    loan_params: LoanExtendParams,
) -> OutLoanAmortization:
    """
    Calculate the amortization table with the French system.

    Args:
      principal: Loan capital.
      annual_interes_rate: Annual interest rate.
      num_payments: Number of loan payments in the period.

    Returns:
      A list with the next information for every period:
        * Period number.
        * Amortization installment.
        * Interest portion.
        * Capital amortization portion.
        * Outstanding balance.
    """
    # Extract values of loan params
    principal = loan_params.principal
    interest_rate = loan_params.annual_interest_rate / 100.0
    num_payments = loan_params.num_payments
    irregular_payments = loan_params.irregular_payments
    grace_period_months = loan_params.grace_period_months
    disbursement_fee = loan_params.disbursement_fee
    insurances = loan_params.insurances

    # Calculate the installment amortization with simplify formula for months.
    monthly_interest_rate = interest_rate / 12
    monthly_payment = (principal * monthly_interest_rate) / (
        1 - (1 + monthly_interest_rate) ** -num_payments
    )

    # Outstanding balance
    remaining_balance = principal

    # Ordenar los pagos irregulares por mes
    if irregular_payments is not None:
        irregular_payments = sorted(irregular_payments, key=lambda x: x.month)

    # Determine commission value
    if disbursement_fee is not None:
        if disbursement_fee.is_rate:
            disbursement_fee.amount *= principal

    # Define values of insurances
    if insurances is not None:
        for insurance in insurances:
            if insurance.is_rate:
                insurance.amount *= principal

    return calculate_amortization_extend_params(
        irregular_payments=irregular_payments,
        num_payments=num_payments,
        remaining_balance=remaining_balance,
        monthly_interest_rate=monthly_interest_rate,
        monthly_payment=monthly_payment,
        grace_period_months=grace_period_months,
        disbursement_fee=disbursement_fee,
        insurances=insurances,
    )


# 2 Amortization table constant principal - system German
def generate_amortization_table_constant_principal(
    loan_params: LoanBaseParams,
):
    principal = loan_params.principal
    interest_rate = loan_params.annual_interest_rate / 100.0
    num_payments = loan_params.num_payments

    monthly_interest_rate = interest_rate / 12.0
    monthly_principal_payment = principal / num_payments

    amortization_table = []
    remaining_balance = principal

    for month in range(1, num_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        remaining_balance -= monthly_principal_payment
        monthly_payment = monthly_principal_payment + interest_payment

        entry = create_amortization_entry(
            month,
            monthly_payment,
            monthly_principal_payment,
            interest_payment,
            remaining_balance,
        )

        amortization_table.append(entry)

    return amortization_table


# 3 Amorti<ation table fixed interest - system American
def generate_amortization_table_only_interest(loan_params: LoanBaseParams):
    principal = loan_params.principal
    interest_rate = loan_params.annual_interest_rate / 100.0
    num_payments = loan_params.num_payments

    monthly_interest_rate = interest_rate / 12

    interest_payment = principal * monthly_interest_rate
    monthly_payment = interest_payment

    amortization_table = []
    remaining_balance = principal

    for month in range(1, num_payments + 1):
        entry = create_amortization_entry(
            month=month,
            monthly_payment=monthly_payment,
            principal_payment=0,
            interest_payment=interest_payment,
            remaining_balance=remaining_balance,
        )

        amortization_table.append(entry)

    return amortization_table


# 8 Irregular
def calculate_amortization_extend_params(
    irregular_payments: list[AdditionalPayment] | None,
    num_payments,
    remaining_balance,
    monthly_interest_rate,
    monthly_payment,
    grace_period_months,
    disbursement_fee: DisbursementFee | None,
    insurances: list[LoanInsurance] | None,
) -> OutLoanAmortization:
    # Inicializar lista
    amortization_table = []

    # Iterate over the loan periods.
    for month in range(1, num_payments + 1 + grace_period_months):
        # Comprobar si hay un pago irregular en este mes
        if irregular_payments is not None:
            irregular_payment = next(
                (
                    payment.payment_amount
                    for payment in irregular_payments
                    if payment.month == month
                ),
                0,
            )
        else:
            irregular_payment = 0

        # Comprobar los periodos de gracia
        if month <= grace_period_months:
            interest_payment = remaining_balance * monthly_interest_rate
            principal_payment = 0
            payment_installment = 0 + interest_payment + irregular_payment
        else:
            # Calculate interest portion and principal amortization portion.
            interest_payment = remaining_balance * monthly_interest_rate
            principal_payment = monthly_payment - interest_payment
            payment_installment = monthly_payment + interest_payment + irregular_payment

        # Calculate outstanding balance.
        remaining_balance -= principal_payment

        # Add the result in amortization table.
        entry = create_amortization_entry(
            month,
            payment_installment,
            principal_payment,
            interest_payment,
            remaining_balance,
        )

        if irregular_payments is not None:
            entry["irregular_payment"] = round(irregular_payment, 2)

        if insurances is not None:
            entry["insurances"] = {}
            for insurance in insurances:
                name = insurance.name
                amount = insurance.amount

                entry["insurances"][name] = round(amount, 2)

        amortization_table.append(entry)

        result = {}

        if disbursement_fee is not None:
            result["commission"] = round(disbursement_fee.amount, 2)

        result["amortization_table"] = amortization_table

    return result
