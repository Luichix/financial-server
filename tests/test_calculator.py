from app.services.calculator_service import (
    calculate_simple_future,
    calculate_simple_interest,
    calculate_simple_interest_rate,
    calculate_simple_interest_rate_based_future,
    calculate_simple_period,
    calculate_simple_period_based_future,
    calculate_simple_principal,
    calculate_simple_principal_based_future,
)


class TestCalculatorSimple:
    principal = 1000
    interest_rate = 0.1
    period = 2
    interest = 200
    future = 1200

    def test_calculator_principal(self):
        assert (
            calculate_simple_principal(
                interest_rate=self.interest_rate,
                period=self.period,
                interest=self.interest,
            )
            == self.principal
        )

    def test_calculator_interest_rate(self):
        assert (
            calculate_simple_interest_rate(
                interest=self.interest,
                principal=self.principal,
                period=self.period,
            )
            == self.interest_rate
        )

    def test_calculator_period(self):
        assert (
            calculate_simple_period(
                interest_rate=self.interest_rate,
                principal=self.principal,
                interest=self.interest,
            )
            == self.period
        )

    def test_calculator_interest(self):
        assert (
            calculate_simple_interest(
                interest_rate=self.interest_rate,
                principal=self.principal,
                period=self.period,
            )
            == self.interest
        )

    def test_calculator_future(self):
        assert (
            calculate_simple_future(principal=self.principal, interest=self.interest)
            == self.future
        )


class TestCalculatorSimpleFuture:
    principal = 1000
    interest_rate = 0.1
    period = 2
    interest = 200
    future = 1210

    def test_calculator_principal_based_future(self):
        assert (
            calculate_simple_principal_based_future(
                interest_rate=self.interest_rate,
                period=self.period,
                future=self.future,
            )
            == self.principal
        )

    def test_calculator_interest_rate_based_future(self):
        assert (
            calculate_simple_interest_rate_based_future(
                future=self.future,
                principal=self.principal,
                period=self.period,
            )
            == self.interest_rate
        )

    def test_calculator_period_based_future(self):
        assert (
            calculate_simple_period_based_future(
                interest_rate=self.interest_rate,
                principal=self.principal,
                future=self.future,
            )
            == self.period
        )

    # def test_calculator_interest(self):
    #     assert (
    #         calculate_simple_interest(
    #             interest_rate=self.interest_rate,
    #             principal=self.principal,
    #             period=self.period,
    #         )
    #         == self.interest
    #     )

    # def test_calculator_future(self):
    #     assert (
    #         calculate_simple_future(principal=self.principal, interest=self.interest)
    #         == self.future
    #     )
