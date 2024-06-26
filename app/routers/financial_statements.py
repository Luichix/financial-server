from typing import Annotated
from fastapi import APIRouter, Query

from app.models.financial_statement import (
    AccountCatalog,
    AccountingMethod,
    BalanceSheet,
    IncomeStatement,
    JournalBook,
    LedgerBook,
    TrialBalance,
)
from app.services.financial_statement_service import (
    create_balance_sheet,
    create_income_statement,
    create_ledger_book,
    create_trial_balance,
    evaluate_journal_book,
)

from app.data.financial_statement_data import account_catalog_data
from app.data.account_catalog_data import account_catalog_data_with_description

router = APIRouter()


@router.get("/account_catalog", response_model=AccountCatalog)
async def get_account_catalog():
    return AccountCatalog(**account_catalog_data_with_description)


@router.post(
    "/evaluate_journal_book",
    response_model=JournalBook,
)
async def validate_journal_book(
    journal_book: JournalBook,
):
    return evaluate_journal_book(journal_book)


@router.post("/generate_ledger_book", response_model=LedgerBook)
async def generate_ledger_book(journal_book: JournalBook):
    return create_ledger_book(journal_book)


@router.post("/generate_trial_balance", response_model=TrialBalance)
async def generate_trial_balance(ledger_book: LedgerBook):
    return create_trial_balance(ledger_book)


@router.post("/generate_income_statement", response_model=IncomeStatement)
async def generate_income_statement(
    trial_balance: TrialBalance,
    tax_rate: Annotated[float, Query(alias="taxRate")] = 0,
    accounting_method: Annotated[
        AccountingMethod, Query(alias="accountingMethod")
    ] = AccountingMethod.ANALYTICAL,
    initial_inventory: Annotated[float, Query(alias="initialInventory")] = 0,
):
    return create_income_statement(
        trial_balance=trial_balance,
        tax_rate=tax_rate,
        account_catalog=AccountCatalog(**account_catalog_data),
        accounting_method=accounting_method,
        initial_inventory=initial_inventory,
    )


@router.post("/generate_balance_sheet", response_model=BalanceSheet)
async def generate_balance_sheet(trial_balance: TrialBalance):
    return create_balance_sheet(
        trial_balance=trial_balance,
        account_catalog=AccountCatalog(**account_catalog_data),
    )
