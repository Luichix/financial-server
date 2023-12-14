from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


class TestCalculatorSimple:
    financial_params = {
        "principal": 100,
        "interest": 10,
        "interest_rate": 10,
        "period": 1,
        "type_period": "years",
        "future": 110,
    }

    def test_simple_interest_interest(self):
        response = client.post(
            "/calculate_simple_interest?calculationType=Interest",
            json=self.financial_params,
        )
        assert response.status_code == 200
        assert response.json() == self.financial_params["interest"]

    def test_simple_interest_principal(self):
        response = client.post(
            "/calculate_simple_interest?calculationType=Principal",
            json=self.financial_params,
        )
        assert response.status_code == 200
        assert response.json() == self.financial_params["principal"]

    def test_simple_interest_rate(self):
        response = client.post(
            "/calculate_simple_interest?calculationType=Rate",
            json=self.financial_params,
        )
        assert response.status_code == 200
        assert response.json() == self.financial_params["interest_rate"]

    def test_simple_interest_period(self):
        response = client.post(
            "/calculate_simple_interest?calculationType=Period",
            json=self.financial_params,
        )
        assert response.status_code == 200
        assert response.json() == self.financial_params["period"]

    def test_simple_interest_future(self):
        response = client.post(
            "/calculate_simple_interest?calculationType=Future",
            json=self.financial_params,
        )
        assert response.status_code == 200
        assert response.json() == self.financial_params["future"]
