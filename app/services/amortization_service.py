import math
from app.models.amortization import (
    AdditionalPayment,
    AmortizationType,
    DisbursementFee,
    FactorFrequency,
    FrecuencyType,
    LoanExtraParams,
    OutAmortizationExtra,
    RecurringPayment,
    OutLoanAmortization,
)


# Generate amortization table
def generate_amortization_table(
    loan_params: LoanExtraParams, amortization_type: AmortizationType
) -> OutLoanAmortization:
    """
    Calculate the amortization table with the diferents systems.

    Args:
      principal: Loan capital.
      interes_rate: Interest rate.
      periods_number: Number of periods in the loan payment.
      payment_frecuency: Frecuency of payment installments.
      interest_rate_type: Type frecuency of interes rate.
      periods_type: Type frecuency of periods in the loan payment.
      grace_period: Period of grace agree the payment frecuency.
      disbursement_fee: Amount of disbursement fee.
      additional_payments: Payments additional in specific time in the period.
      recurring_payments: Payments recurring in the loan.

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
    base_interest_rate = loan_params.interest_rate
    periods_number = loan_params.periods_number
    payment_frecuency = loan_params.payment_frecuency
    interest_rate_type = loan_params.interest_rate_type
    periods_type = loan_params.periods_type
    grace_period = loan_params.grace_period
    disbursement_fee = loan_params.disbursement_fee
    additional_payments = loan_params.additional_payments
    recurring_payments = loan_params.recurring_payments

    # Adjust the values frecuencies in interest and periods
    adjusted_interest_rate = adjust_frecuency_value(
        payment_frecuency, base_interest_rate, interest_rate_type, FrecuencyType.RATE
    )
    number_installments = adjust_frecuency_value(
        payment_frecuency, periods_number, periods_type, FrecuencyType.PERIOD
    )

    number_installments = math.ceil(number_installments)
    # Parse the insterest rate

    interest_rate = adjusted_interest_rate / 100

    # Evaluate type amortization process
    if amortization_type == AmortizationType.GERMAN:
        # Calculate for amortization German
        interest_payment = None
        fee_payment = None
        principal_payment = principal / number_installments
    elif amortization_type == AmortizationType.AMERICAN:
        # Calculate for amortization American
        interest_payment = principal * interest_rate
        fee_payment = interest_payment
        principal_payment = 0
    elif amortization_type == AmortizationType.FRENCH:
        # Calculate the installment amortization French
        interest_payment = None
        principal_payment = None
        fee_payment = (principal * interest_rate) / (
            1 - (1 + interest_rate) ** -number_installments
        )

    # Outstanding balance
    remaining_balance = principal

    # Determine disbursement fee value
    if disbursement_fee is not None:
        if disbursement_fee.is_rate:
            disbursement_fee.amount *= principal

    # Order additional payments for periods
    if additional_payments is not None:
        additional_payments = sorted(additional_payments, key=lambda x: x.period)

    # Define values of recurring_payments
    if recurring_payments is not None:
        for recurring in recurring_payments:
            if recurring.is_rate:
                recurring.amount *= principal

    # Generate amortization
    amortization_result = calculate_amortization(
        amortization_type=amortization_type,
        interest_rate=interest_rate,
        number_installments=number_installments,
        principal_payment=principal_payment,
        fee_payment=fee_payment,
        interest_payment=interest_payment,
        remaining_balance=remaining_balance,
        grace_period=grace_period,
        disbursement_fee=disbursement_fee,
        additional_payments=additional_payments,
        recurring_payments=recurring_payments,
    )

    amortization_result["principal"] = principal
    amortization_result["interestRate"] = base_interest_rate
    amortization_result["periodsNumber"] = periods_number
    amortization_result["paymentFrecuency"] = payment_frecuency
    amortization_result["interestRateType"] = interest_rate_type
    amortization_result["periodsType"] = periods_type
    amortization_result["gracePeriod"] = grace_period

    return amortization_result


# Calculate amortization table
def calculate_amortization(
    amortization_type: AmortizationType,
    interest_rate: float,
    number_installments: int,
    principal_payment: float | None,
    fee_payment: float | None,
    interest_payment: float | None,
    remaining_balance,
    grace_period: int,
    disbursement_fee: DisbursementFee | None,
    additional_payments: list[AdditionalPayment] | None,
    recurring_payments: list[RecurringPayment] | None,
) -> OutAmortizationExtra:
    # Initialize variables to keep track of totals
    total_amount_pay = 0
    total_fee_payment = 0
    total_interest_payment = 0
    total_additional_payment = 0
    total_recurring_payments = {}
    amortization_table = []

    period_range = number_installments + 1 + grace_period
    # Iterate over the loan periods.
    for period in range(1, period_range):
        # Verify if exists an additional payment in current period
        if additional_payments is not None:
            additional_payment = next(
                (
                    payment.payment_amount
                    for payment in additional_payments
                    if payment.period == period
                ),
                0,
            )
        else:
            additional_payment = 0

        # Calculate interest payment
        if amortization_type != AmortizationType.AMERICAN:
            interest_payment = remaining_balance * interest_rate

        principal_amortization = 0
        # Check the grace period
        if period <= grace_period:
            # Calculate interest portion and principal amortization portion with grace period.
            principal_amortization = 0
            payment_installment = interest_payment
        else:
            # Evaluate value of principal payment.
            if amortization_type == AmortizationType.FRENCH:
                principal_amortization = fee_payment - interest_payment
                payment_installment = fee_payment
                remaining_balance -= principal_amortization

            if amortization_type == AmortizationType.GERMAN:
                principal_amortization = principal_payment
                payment_installment = principal_payment + interest_payment
                remaining_balance -= principal_payment

            if amortization_type == AmortizationType.AMERICAN:
                payment_installment = fee_payment
                if period == period_range - 1:
                    payment_installment = fee_payment + remaining_balance
                    principal_amortization = remaining_balance
                    remaining_balance = 0

        entry = {
            "period": period,
            "principalPayment": round(principal_amortization, 2),
            "remainingBalance": round(remaining_balance, 2),
            "feePayment": round(payment_installment, 2),
            "interestPayment": round(interest_payment, 2),
        }

        if additional_payments is not None:
            entry["additionalPayment"] = round(additional_payment, 2)
            total_additional_payment += additional_payment

        if recurring_payments is not None:
            entry["recurringPayments"] = {}
            for recurring in recurring_payments:
                name = recurring.name
                amount = recurring.amount

                # Add the current recurring paymenr amount to the total for that payments
                if name in total_recurring_payments:
                    total_recurring_payments[name] += amount
                else:
                    total_recurring_payments[name] = amount

                entry["recurringPayments"][name] = round(amount, 2)
                total_amount_pay += round(amount, 2)

        # Fill Amortization Table
        amortization_table.append(entry)

        # Calculate totals with every iteration
        total_fee_payment += payment_installment
        total_interest_payment += interest_payment

    # Initialize result amortization generator
    result = {}

    # Round the values in total_recurring_payment
    rounded_total_recurring_payments = {
        key: round(value, 2) for key, value in total_recurring_payments.items()
    }

    # Add Disbursement Fee into the result
    if disbursement_fee is not None:
        result["disbursementFee"] = round(disbursement_fee.amount, 2)
        total_amount_pay += round(disbursement_fee.amount, 2)

    total_amount_pay += round(total_additional_payment, 2) + round(total_fee_payment, 2)

    # Add the calculated totals to the result dictionary
    result["feePayment"] = round(total_fee_payment, 2)
    result["interestPayment"] = round(total_interest_payment, 2)
    result["additionalPayment"] = round(total_additional_payment, 2)
    result["recurringPayments"] = rounded_total_recurring_payments
    result["amortizationTable"] = amortization_table
    result["numberInstallments"] = number_installments
    result["totalAmountPay"] = round(total_amount_pay, 2)

    return result


# Calculate the adjusted_interest_rate
def adjust_frecuency_value(
    frecuency, value, value_frecuency, frecuency_type: FrecuencyType
):
    # Normalize value into year

    factor_frecuency = FactorFrequency.__getitem__(frecuency)
    factor_type = FactorFrequency.__getitem__(value_frecuency)

    if frecuency_type == FrecuencyType.PERIOD:
        normalize_value = value / factor_type
        if factor_frecuency != factor_type:
            return normalize_value * factor_frecuency

    elif frecuency_type == FrecuencyType.RATE:
        normalize_value = value * factor_type
        if factor_frecuency != factor_type:
            return normalize_value / factor_frecuency

    return value
