from app.services.amortization_service import (
    adjust_frecuency_value,
)
from app.models.amortization import PaymentFrecuency


payment_frecuency = PaymentFrecuency.ANNUAL
value = 360
value_type = PaymentFrecuency.DAILY


def test_adjust_frecuency_value():
    adjusted_value = adjust_frecuency_value(payment_frecuency, value, value_type)

    print(adjusted_value)
    assert adjusted_value == 1


def test_adjust_frecuency_value():
    adjusted_value = adjust_frecuency_value(frecuency="daily", value=5, type="annual")

    print(adjusted_value)
    assert adjusted_value == 1800
