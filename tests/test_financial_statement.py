from app.models.financial_statement import (
    BalanceType,
    JournalBook,
    LedgerBook,
    TrialBalance,
)
from app.services.financial_statement_service import (
    create_ledger_book,
    create_trial_balance,
    evaluate_journal_book,
)


class TestFinancialStatement:
    journal_book = {
        "journal_book_entries": [
            {
                "entry_number": 1,
                "date": "2023-10-10",
                "debit": 100,
                "credit": 0,
                "concept": "Compra de productos en inventario",
                "account": {
                    "account_code": "101010",
                    "account_name": "Inventario de Mercancias",
                    "account_group": "1",
                },
            },
            {
                "entry_number": 1,
                "date": "2023-10-10",
                "debit": 0,
                "credit": 100,
                "concept": "Pago de la compra de mercancia al contado",
                "account": {
                    "account_code": "102010",
                    "account_name": "Caja",
                    "account_group": "1",
                },
            },
        ]
    }

    evaluated_journal_book = {
        "journal_book_entries": [
            {
                "entry_number": 1,
                "date": "2023-10-10",
                "debit": 100,
                "credit": 0,
                "concept": "Compra de productos en inventario",
                "account": {
                    "account_code": "101010",
                    "account_name": "Inventario de Mercancias",
                    "account_group": "1",
                },
                "unbalanced": False,
            },
            {
                "entry_number": 1,
                "date": "2023-10-10",
                "debit": 0,
                "credit": 100,
                "concept": "Pago de la compra de mercancia al contado",
                "account": {
                    "account_code": "102010",
                    "account_name": "Caja",
                    "account_group": "1",
                },
                "unbalanced": False,
            },
        ],
        "unbalanced": False,
        "unbalanced_entries": [],
    }

    ledger_book = {
        "ledger_book_entries": [
            {
                "account_code": "101010",
                "account_name": "Inventario de Mercancias",
                "account_group": "1",
                "entries": [
                    {
                        "entry_number": 1,
                        "date": "2023-10-10",
                        "debit": 100,
                        "credit": 0,
                    }
                ],
                "debit": 100,
                "credit": 0,
                "balance": 100.0,
                "balance_type": BalanceType.DEBIT,
            },
            {
                "account_code": "102010",
                "account_name": "Caja",
                "account_group": "1",
                "entries": [
                    {
                        "entry_number": 1,
                        "date": "2023-10-10",
                        "debit": 0,
                        "credit": 100,
                    }
                ],
                "credit": 100,
                "debit": 0,
                "balance": 100.0,
                "balance_type": BalanceType.CREDIT,
            },
        ]
    }

    trial_balance = {
        "accounts_summary": [
            {
                "account_code": "101010",
                "account_name": "Inventario de Mercancias",
                "account_group": "1",
                "total_debit": 100,
                "total_credit": 0,
                "debit_balance": 100,
                "credit_balance": 0,
            },
            {
                "account_code": "102010",
                "account_name": "Caja",
                "account_group": "1",
                "total_debit": 0,
                "total_credit": 100,
                "debit_balance": 0,
                "credit_balance": 100,
            },
        ],
        "total_debit": 100,
        "total_credit": 100,
        "debit_balance": 100,
        "credit_balance": 100,
        "is_balanced": True,
    }

    journal_book_instance = JournalBook(**journal_book)

    evaluated_journal_book_instance = JournalBook(**evaluated_journal_book)

    ledger_book_instance = LedgerBook(**ledger_book)

    trial_balance_instance = TrialBalance(**trial_balance)

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
