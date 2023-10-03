from app.models.amortization import (
    AdditionalPayment,
    AmortizationType,
    DisbursementFee,
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
        "monthlyPayment": round(monthly_payment, 2),
        "principalPayment": round(principal_payment, 2),
        "interestPayment": round(interest_payment, 2),
        "remainingBalance": round(remaining_balance, 2),
    }


# Generate amortization table
def generate_amortization_table(
    loan_params: LoanExtendParams, amortization_type: AmortizationType
) -> OutLoanAmortization:
    """
    Calculate the amortization table with the French system.

    Args:
      principal: Loan capital.
      interes_rate: Interest rate.
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
    interest_rate = loan_params.interest_rate / 100.0
    num_payments = loan_params.num_payments
    additional_payments = loan_params.additional_payments
    grace_period_months = loan_params.grace_period_months
    disbursement_fee = loan_params.disbursement_fee
    insurances = loan_params.insurances

    # Calculate the monthly insterest rate
    monthly_interest_rate = interest_rate / 12

    # Evaluate type amortization process
    if amortization_type == AmortizationType.GERMAN:
        # Calculate for amortization German
        interest_payment = None
        monthly_payment = None
        principal_payment = principal / num_payments
    elif amortization_type == AmortizationType.AMERICAN:
        # Calculate for amortization American
        interest_payment = principal * monthly_interest_rate
        monthly_payment = interest_payment
        principal_payment = 0
    else:
        # Calculate the installment amortization French
        interest_payment = None
        principal_payment = None
        monthly_payment = (principal * monthly_interest_rate) / (
            1 - (1 + monthly_interest_rate) ** -num_payments
        )

    # Outstanding balance
    remaining_balance = principal

    # Order additional payments for month
    if additional_payments is not None:
        additional_payments = sorted(additional_payments, key=lambda x: x.month)

    # Determine commission value
    if disbursement_fee is not None:
        if disbursement_fee.is_rate:
            disbursement_fee.amount *= principal

    # Define values of insurances
    if insurances is not None:
        for insurance in insurances:
            if insurance.is_rate:
                insurance.amount *= principal

    return calculate_amortization(
        additional_payments=additional_payments,
        principal=principal,
        interest_rate=interest_rate,
        num_payments=num_payments,
        remaining_balance=remaining_balance,
        monthly_interest_rate=monthly_interest_rate,
        monthly_payment=monthly_payment,
        principal_payment=principal_payment,
        grace_period_months=grace_period_months,
        disbursement_fee=disbursement_fee,
        insurances=insurances,
        amortization_type=amortization_type,
        interest_payment=interest_payment,
    )


# Calculate amortization table
def calculate_amortization(
    additional_payments: list[AdditionalPayment] | None,
    remaining_balance,
    monthly_interest_rate,
    monthly_payment: float | None,
    principal_payment: float | None,
    grace_period_months,
    disbursement_fee: DisbursementFee | None,
    insurances: list[LoanInsurance] | None,
    amortization_type: AmortizationType,
    interest_payment: float | None,
    principal: float,
    interest_rate: float,
    num_payments: int,
) -> OutLoanAmortization:
    # Initialize variables to keep track of totals
    total_monthly_payment = 0
    total_interest_payment = 0
    total_additional_payment = 0
    total_insurances = {}

    amortization_table = []

    # Iterate over the loan periods.
    for month in range(1, num_payments + 1 + grace_period_months):
        # Verify if exists an additional payment in current month
        if additional_payments is not None:
            additional_payment = next(
                (
                    payment.payment_amount
                    for payment in additional_payments
                    if payment.month == month
                ),
                0,
            )
        else:
            additional_payment = 0

        # Calculate interest payment
        if amortization_type != AmortizationType.AMERICAN:
            interest_payment = remaining_balance * monthly_interest_rate

        # Check the grace period months
        if month <= grace_period_months:
            # Calculate interest portion and principal amortization portion with grace period.
            principal_payment = 0
            payment_installment = 0 + interest_payment + additional_payment
        else:
            # Evaluate value of principal payment.
            if amortization_type == AmortizationType.FRENCH:
                principal_payment = monthly_payment - interest_payment

            # Evaluate value of payment installment
            if amortization_type == AmortizationType.GERMAN:
                payment_installment = (
                    principal_payment + interest_payment + additional_payment
                )
            else:
                payment_installment = monthly_payment + additional_payment

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

        if additional_payments is not None:
            entry["additionalPayment"] = round(additional_payment, 2)
            total_additional_payment += additional_payment

        if insurances is not None:
            entry["insurances"] = {}
            for insurance in insurances:
                name = insurance.name
                amount = insurance.amount

                # Add the current insurance amount to the total for that insurance
                if name in total_insurances:
                    total_insurances[name] += amount
                else:
                    total_insurances[name] = amount

                entry["insurances"][name] = round(amount, 2)

        # Calculate totals with every iteration
        total_monthly_payment += payment_installment
        total_interest_payment += interest_payment

        amortization_table.append(entry)

        # Initialize dictionary result
        result = {}

        if disbursement_fee is not None:
            result["commission"] = round(disbursement_fee.amount, 2)

        # Round the values in total_insurances
        rounded_total_insurances = {
            key: round(value, 2) for key, value in total_insurances.items()
        }

        # Add the calculated totals to the result dictionary
        result["principal"] = round(principal, 2)
        result["interestRate"] = interest_rate
        result["numPayments"] = num_payments
        result["totalMonthlyPayment"] = round(total_monthly_payment, 2)
        result["totalInterestPayment"] = round(total_interest_payment, 2)
        result["totalAdditionalPayment"] = round(total_additional_payment, 2)
        result["totalInsurances"] = rounded_total_insurances
        result["amortizationTable"] = amortization_table

    return result
