import math


def calculate_simple_principal(interest: float, interest_rate: float, period: int):
    try:
        principal = interest / (interest_rate * period)
        return principal

    except ZeroDivisionError:
        raise ValueError("interest_rate or period cannot be zero")


def calculate_simple_interest_rate(principal: float, interest: float, period: int):
    try:
        interest_rate = interest / (principal * period)
        return interest_rate

    except ZeroDivisionError:
        raise ValueError("principal or period cannot be zero")


def calculate_simple_period(principal: float, interest: float, interest_rate: float):
    try:
        period = interest / (principal * interest_rate)
        return period

    except ZeroDivisionError:
        raise ValueError("principal or interest_rate cannot be zero")


def calculate_simple_interest(principal: float, interest_rate: float, period: int):
    interest = principal * interest_rate * period
    return interest


def calculate_simple_future(principal: float, interest: float):
    future = principal + interest
    return future


# Based Future
def calculate_simple_principal_based_future(
    future: float, interest_rate: float, period: int
):
    principal = future / (1 + interest_rate) ** period
    return round(principal, 2)


def calculate_simple_interest_rate_based_future(
    future: float, principal: float, period: int
):
    interest_rate = ((future / principal) ** (1 / period)) - 1
    return round(interest_rate, 2)


def calculate_simple_period_based_future(
    future: float, interest_rate: float, principal: float
):
    interest_rate = (math.log(future / principal)) / math.log(1 + interest_rate)
    return round(interest_rate, 2)
