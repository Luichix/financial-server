from app.models.calculator import FinancialParams, CalculationType, PeriodType


def calculate_interest_simple(
    financial_params: FinancialParams, calculation_type: CalculationType
):
    interest = financial_params.interest
    principal = financial_params.principal
    future = financial_params.future
    interest_rate = financial_params.interest_rate
    period = financial_params.period
    type_period = financial_params.type_period
    period_in_years = None

    # Convert period to years based on type_period
    if type_period == PeriodType.YEARS:
        period_in_years = period
    elif type_period == PeriodType.MONTHS:
        period_in_years = period / 12
    elif type_period == PeriodType.DAYS:
        period_in_years = period / 365

    try:
        if calculation_type == CalculationType.INTEREST:
            # I = P * r * t
            interest = principal * (interest_rate / 100) * period_in_years
            return interest
        elif calculation_type == CalculationType.RATE:
            # r = I / (P * t)
            interest_rate = (interest / (principal * period_in_years)) * 100
            return interest_rate
        elif calculation_type == CalculationType.PRINCIPAL:
            # P = I / (r * t)
            principal = interest / ((interest_rate / 100) * period_in_years)
            return principal
        elif calculation_type == CalculationType.FUTURE:
            # F = P + I
            future = principal + interest
            return future
        elif calculation_type == CalculationType.PERIOD:
            # t = I / (P * r)
            period = interest / (principal * (interest_rate / 100))
            return period
        else:
            raise ValueError("Invalid calculation type")

    except ZeroDivisionError:
        raise ValueError("interest_rate or period cannot be zero")
