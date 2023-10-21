from app.models.financial_statement import (
    AccountCatalog,
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

from app.data.financial_statement_data import (
    account_catalog_data,
    journal_book_data,
    evaluated_journal_book_data,
    ledger_book_data,
    trial_balance_data,
    income_statement_perpetual_data,
    income_statement_analytical_data,
    balance_sheet_data,
)


class TestFinancialStatement:
    tax_rate = 0.3

    account_catalog_instance = AccountCatalog(**account_catalog_data)

    journal_book_instance = JournalBook(**journal_book_data)

    evaluated_journal_book_instance = JournalBook(**evaluated_journal_book_data)

    ledger_book_instance = LedgerBook(**ledger_book_data)

    trial_balance_instance = TrialBalance(**trial_balance_data)

    income_statement_perpetual_instance = IncomeStatement(
        **income_statement_perpetual_data
    )

    income_statement_analytical_instance = IncomeStatement(
        **income_statement_analytical_data
    )

    balance_sheet_instance = BalanceSheet(**balance_sheet_data)

    def test_evaluated_journal_book(self):
        assert (
            evaluate_journal_book(self.journal_book_instance)
            == self.evaluated_journal_book_instance
        )

    def test_create_ledger_book(self):
        assert (
            create_ledger_book(self.evaluated_journal_book_instance)
            == self.ledger_book_instance
        )

    def test_create_trial_balance(self):
        assert (
            create_trial_balance(self.ledger_book_instance)
            == self.trial_balance_instance
        )

    def test_create_income_statement(self):
        assert (
            create_income_statement(
                self.trial_balance_instance,
                self.account_catalog_instance,
                self.tax_rate,
                "perpetual",
            )
            == self.income_statement_perpetual_instance
        )
        assert (
            create_income_statement(
                self.trial_balance_instance,
                self.account_catalog_instance,
                self.tax_rate,
                "analytical",
            )
            == self.income_statement_analytical_instance
        )

    def test_create_balance_sheet(self):
        assert (
            create_balance_sheet(
                self.trial_balance_instance, self.account_catalog_instance
            )
            == self.balance_sheet_instance
        )
