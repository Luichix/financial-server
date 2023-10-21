from app.models.financial_statement import (
    AccountCatalog,
    AnalyticalMethod,
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
    PerpetualMethod,
    ProductionCost,
    SalesCostPerpetual,
    SalesCostAnalytical,
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

    income_statement_instance_perpetual = IncomeStatement(
        accountingMethod="perpetual",
        earningsIncome=PerpetualMethod(
            netSales=NetSales(
                sales=0.0,
                salesReturns=0.0,
                salesDiscounts=0.0,
                salesAllowances=0.0,
                netSales=0.0,
            ),
            salesCost=SalesCostPerpetual(
                salesCost=-0.0,
            ),
            grossMargin=GrossMargin(salesRevenue=0.0, salesCost=0.0, grossProfit=0.0),
            operatingExpenses=OperatingExpenses(
                salesExpenses=0.0,
                administrativeExpenses=0.0,
                financialExpenses=0.0,
                operatingExpenses=0.0,
            ),
            operatingIncome=OperatingIncome(
                grossMargin=0.0, operatingExpenses=0.0, operatingIncome=0.0
            ),
            incomeBeforeTaxes=IncomeBeforeTaxes(
                operatingIncome=0.0,
                otherExpenses=0.0,
                otherProducts=0.0,
                incomeBeforeTaxes=0.0,
            ),
            netIncome=NetIncome(
                incomeBeforeTaxes=0.0,
                taxRate=0.3,
                incomeTaxExpense=0.0,
                netIncome=0.0,
            ),
        ),
    )

    income_statement_instance_analytical = IncomeStatement(
        accountingMethod="analytical",
        earningsIncome=AnalyticalMethod(
            netSales=NetSales(
                sales=0.0,
                salesReturns=0.0,
                salesDiscounts=0.0,
                salesAllowances=0.0,
                netSales=0.0,
            ),
            netPurchases=NetPurchases(
                purchases=0.0,
                purchasingExpenses=0.0,
                totalPurchases=0.0,
                purchasesReturns=0.0,
                purchasesDiscounts=0.0,
                purchasesAllowances=0.0,
                netPurchases=0.0,
            ),
            salesCost=SalesCostAnalytical(
                beginningInventory=0.0,
                purchases=0.0,
                endingInventory=100.0,
                salesCost=-100.0,
            ),
            grossMargin=GrossMargin(
                salesRevenue=0.0, salesCost=-100.0, grossProfit=-100.0
            ),
            operatingExpenses=OperatingExpenses(
                salesExpenses=0.0,
                administrativeExpenses=0.0,
                financialExpenses=0.0,
                operatingExpenses=0.0,
            ),
            operatingIncome=OperatingIncome(
                grossMargin=100.0, operatingExpenses=0.0, operatingIncome=0.0
            ),
            incomeBeforeTaxes=IncomeBeforeTaxes(
                operatingIncome=100.0,
                otherExpenses=0.0,
                otherProducts=0.0,
                incomeBeforeTaxes=100.0,
            ),
            netIncome=NetIncome(
                incomeBeforeTaxes=100.0,
                taxRate=0.3,
                incomeTaxExpense=30.0,
                netIncome=70.0,
            ),
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
                "perpetual",
            )
            == self.income_statement_instance_perpetual
        )
        assert (
            create_income_statement(
                self.trial_balance_instance,
                self.account_catalog_instance,
                self.tax_rate,
                "analytical",
            )
            == self.income_statement_instance_analytical
        )

    def test_create_balance_sheet(self):
        assert (
            create_balance_sheet(
                self.trial_balance_instance, self.account_catalog_instance
            )
            == self.balance_sheet_instance
        )
