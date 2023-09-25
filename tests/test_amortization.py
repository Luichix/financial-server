from app.services.amortization_service import create_amortization_entry


def test_create_amortization_entry():
    assert create_amortization_entry(1, 1000, 900, 100, 9000) == {
        "month": 1,
        "monthly_payment": 1000,
        "principal_payment": 900,
        "interest_payment": 100,
        "remaining_balance": 9000,
    }
