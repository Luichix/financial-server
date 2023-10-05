from app.services.amortization_service import (
    adjust_frecuency_value,
)
from app.models.amortization import FrecuencyType, PaymentFrecuency


# The frecuency required is same at the frecuency value
def test_same_frecuency_period():
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.ANNUAL,
            value=10,
            value_frecuency=PaymentFrecuency.ANNUAL,
            frecuency_type=FrecuencyType.PERIOD,
        )
        == 10
    )
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.SEMIANNUAL,
            value=10,
            value_frecuency=PaymentFrecuency.SEMIANNUAL,
            frecuency_type=FrecuencyType.PERIOD,
        )
        == 10
    )
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.QUARTERLY,
            value=10,
            value_frecuency=PaymentFrecuency.QUARTERLY,
            frecuency_type=FrecuencyType.PERIOD,
        )
        == 10
    )
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.BIMONTHLY,
            value=10,
            value_frecuency=PaymentFrecuency.BIMONTHLY,
            frecuency_type=FrecuencyType.PERIOD,
        )
        == 10
    )
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.MONTHLY,
            value=10,
            value_frecuency=PaymentFrecuency.MONTHLY,
            frecuency_type=FrecuencyType.PERIOD,
        )
        == 10
    )
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.BIWEEKLY,
            value=10,
            value_frecuency=PaymentFrecuency.BIWEEKLY,
            frecuency_type=FrecuencyType.PERIOD,
        )
        == 10
    )

    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.WEEKLY,
            value=10,
            value_frecuency=PaymentFrecuency.WEEKLY,
            frecuency_type=FrecuencyType.PERIOD,
        )
        == 10
    )

    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.DAILY,
            value=10,
            value_frecuency=PaymentFrecuency.DAILY,
            frecuency_type=FrecuencyType.PERIOD,
        )
        == 10
    )


# The frecuency required is greather than the frecuency value
def test_upper_frecuency_period():
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.ANNUAL,
            value=12,
            value_frecuency=PaymentFrecuency.SEMIANNUAL,
            frecuency_type=FrecuencyType.PERIOD,
        )
    ) == 6
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.ANNUAL,
            value=48,
            value_frecuency=PaymentFrecuency.MONTHLY,
            frecuency_type=FrecuencyType.PERIOD,
        )
    ) == 4
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.ANNUAL,
            value=720,
            value_frecuency=PaymentFrecuency.DAILY,
            frecuency_type=FrecuencyType.PERIOD,
        )
    ) == 2


# The frecuency required is greather than the frecuency value
def test_lower_frecuency_period():
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.SEMIANNUAL,
            value=1,
            value_frecuency=PaymentFrecuency.ANNUAL,
            frecuency_type=FrecuencyType.PERIOD,
        )
    ) == 2
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.MONTHLY,
            value=2,
            value_frecuency=PaymentFrecuency.ANNUAL,
            frecuency_type=FrecuencyType.PERIOD,
        )
    ) == 24
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.DAILY,
            value=1,
            value_frecuency=PaymentFrecuency.ANNUAL,
            frecuency_type=FrecuencyType.PERIOD,
        )
    ) == 360

    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.DAILY,
            value=1,
            value_frecuency=PaymentFrecuency.MONTHLY,
            frecuency_type=FrecuencyType.PERIOD,
        )
    ) == 30


def test_same_frecuency_rate():
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.ANNUAL,
            value=10,
            value_frecuency=PaymentFrecuency.ANNUAL,
            frecuency_type=FrecuencyType.RATE,
        )
        == 10
    )
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.MONTHLY,
            value=1.25,
            value_frecuency=PaymentFrecuency.MONTHLY,
            frecuency_type=FrecuencyType.RATE,
        )
        == 1.25
    )


def test_upper_frecuency_rate():
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.ANNUAL,
            value=1.25,
            value_frecuency=PaymentFrecuency.MONTHLY,
            frecuency_type=FrecuencyType.RATE,
        )
        == 15
    )
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.SEMIANNUAL,
            value=1.25,
            value_frecuency=PaymentFrecuency.MONTHLY,
            frecuency_type=FrecuencyType.RATE,
        )
        == 7.5
    )
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.SEMIANNUAL,
            value=6,
            value_frecuency=PaymentFrecuency.QUARTERLY,
            frecuency_type=FrecuencyType.RATE,
        )
        == 12
    )


def test_lower_frecuency_rate():
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.MONTHLY,
            value=12,
            value_frecuency=PaymentFrecuency.ANNUAL,
            frecuency_type=FrecuencyType.RATE,
        )
        == 1
    )
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.MONTHLY,
            value=6,
            value_frecuency=PaymentFrecuency.SEMIANNUAL,
            frecuency_type=FrecuencyType.RATE,
        )
        == 1
    )
    assert (
        adjust_frecuency_value(
            frecuency=PaymentFrecuency.QUARTERLY,
            value=12,
            value_frecuency=PaymentFrecuency.ANNUAL,
            frecuency_type=FrecuencyType.RATE,
        )
        == 3
    )
