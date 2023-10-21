from fastapi.testclient import TestClient
from app.main import app
from app.models.amortization import LoanExtraParams


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200


class TestAmortizationTable:
    body: LoanExtraParams = {
        "principal": 10000,
        "interestRate": 10,
        "periodsNumber": 12,
        "paymentFrecuency": "monthly",
        "interestRateType": "annual",
        "periodsType": "monthly",
        "gracePeriod": 0,
        "additionalPayments": [{"period": 0, "paymentAmount": 0}],
        "recurringPayments": [{"name": "string", "amount": 1, "isRate": False}],
        "disbursementFee": {"amount": 1, "isRate": False},
    }

    def test_read_amortization_table_french(self):
        response = client.post(
            "/amortization_table?amortizationType=French",
            json=self.body,
        )
        assert response.status_code == 200
        assert response.json()["principal"] == 10000
        assert response.json()["interestPayment"] == 549.91

    def test_read_amortization_table_German(self):
        response = client.post(
            "/amortization_table?amortizationType=German",
            json=self.body,
        )

        assert response.status_code == 200
        assert response.json()["principal"] == 10000
        assert response.json()["interestPayment"] == 541.67

    def test_read_amortization_table_American(self):
        response = client.post(
            "/amortization_table?amortizationType=American",
            json=self.body,
        )
        assert response.status_code == 200
        assert response.json()["principal"] == 10000
        assert response.json()["interestPayment"] == 1000
