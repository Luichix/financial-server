from fastapi.testclient import TestClient
from app.main import app
from app.data.financial_statement_data import (
    evaluated_journal_book_data,
    ledger_book_data,
    trial_balance_data,
    income_statement_analytical_data,
    income_statement_perpetual_data,
    balance_sheet_data,
)

client = TestClient(app)


def test_generate_account_catalog_xlsx():
    response = client.post("/generate_account_catalog_xlsx/")
    assert response.status_code == 200
    assert (
        response.headers["content-type"]
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


def test_generate_journal_book_xlsx():
    response = client.post(
        "/generate_journal_book_xlsx/",
        json=evaluated_journal_book_data,
    )
    assert response.status_code == 200
    assert (
        response.headers["content-type"]
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


def test_generate_ledger_book_xlsx():
    response = client.post("/generate_ledger_book_xlsx/", json=ledger_book_data)
    assert response.status_code == 200
    assert (
        response.headers["content-type"]
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


def test_generate_trial_balance_xlsx():
    response = client.post("/generate_trial_balance_xlsx/", json=trial_balance_data)
    assert response.status_code == 200
    assert (
        response.headers["content-type"]
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


def test_generate_income_statement_xlsx():
    response_analytical = client.post(
        "/generate_income_statement_xlsx/", json=income_statement_analytical_data
    )
    assert response_analytical.status_code == 200
    assert (
        response_analytical.headers["content-type"]
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
    response_perpetual = client.post(
        "/generate_income_statement_xlsx/", json=income_statement_perpetual_data
    )
    assert response_perpetual.status_code == 200
    assert (
        response_perpetual.headers["content-type"]
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


def test_generate_balance_sheet_xlsx():
    response = client.post("/generate_balance_sheet_xlsx/", json=balance_sheet_data)
    assert response.status_code == 200
    assert (
        response.headers["content-type"]
        == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
