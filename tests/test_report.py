from fastapi.testclient import TestClient
from app.main import app
from app.data.financial_statement_data import (
    evaluated_journal_book_data,
    ledger_book_data,
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
