from app.models.financial_statement import (
    AccountCatalog,
    BalanceSheet,
    BalanceSheetAccount,
    GrossMargin,
    IncomeBeforeTaxes,
    IncomeStatement,
    JournalBook,
    LedgerBook,
    NetIncome,
    NetPurchases,
    NetSales,
    OperatingExpenses,
    OperatingIncome,
    ProductionCost,
    SalesCost,
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
    income_statement_data,
    balance_sheet_data,
)


class TestFinancialStatement:
    tax_rate = 0.3

    account_catalog_instance = AccountCatalog(**account_catalog_data)

    journal_book_instance = JournalBook(**journal_book_data)

    evaluated_journal_book_instance = JournalBook(**evaluated_journal_book_data)

    ledger_book_instance = LedgerBook(**ledger_book_data)

    trial_balance_instance = TrialBalance(**trial_balance_data)

    # income_statement_instance = IncomeStatement(**income_statement_data)

    income_statement_instance = IncomeStatement(
        net_sales=NetSales(
            sales=0.0,
            sales_returns=0.0,
            sales_discounts=0.0,
            sales_allowances=0.0,
            net_sales=0.0,
        ),
        net_purchases=NetPurchases(
            purchases=0.0,
            purchasing_expenses=0.0,
            total_purchases=0.0,
            purchases_returns=0.0,
            purchases_discounts=0.0,
            purchases_allowances=0.0,
            net_purchases=0.0,
        ),
        sales_cost=SalesCost(
            beginning_inventory=0.0,
            purchases=0.0,
            ending_inventory=0.0,
            sales_cost=-0.0,
        ),
        production_cost=ProductionCost(
            direct_material=0.0,
            direct_labor=0.0,
            factory_overhead=0.0,
            production_costs=0.0,
        ),
        gross_margin=GrossMargin(sales_revenue=0.0, sales_cost=0.0, gross_profit=0.0),
        operating_expenses=OperatingExpenses(
            sales_expenses=0.0,
            administrative_expenses=0.0,
            financial_expenses=0.0,
            operating_expenses=0.0,
        ),
        operating_income=OperatingIncome(
            gross_margin=0.0, operating_expenses=0.0, operating_income=0.0
        ),
        income_before_taxes=IncomeBeforeTaxes(
            operating_income=0.0,
            other_expenses=0.0,
            other_products=0.0,
            income_before_taxes=0.0,
        ),
        net_income=NetIncome(
            income_before_taxes=0.0,
            tax_rate=0.3,
            income_tax_expense=0.0,
            net_income=0.0,
        ),
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
            )
            == self.income_statement_instance
        )

    def test_create_balance_sheet(self):
        assert (
            create_balance_sheet(
                self.trial_balance_instance, self.account_catalog_instance
            )
            == self.balance_sheet_instance
        )
