from enum import Enum
from pydantic import BaseModel, Field
from datetime import date


class AccountGroup(str, Enum):
    ASSETS = 1
    LIABILITIES = 2
    EQUITY = 3
    REVENUE = 4
    EXPENSE = 5


class IncomeStatementAccountNames(str, Enum):
    SALES = "sales"
    SALES_RETURNS = "sales_returns"
    SALES_DISCOUNTS = "sales_discounts"
    SALES_ALLOWANCES = "sales_allowances"
    PURCHASES = "purchases"
    PURCHASING_EXPENSES = "purchasing_expenses"
    PURCHASES_RETURNS = "purchases_returns"
    PURCHASES_DISCOUNTS = "purchases_discounts"
    PURCHASES_ALLOWANCES = "purchases_allowances"
    BEGINNING_INVENTORY = "beginning_inventory"
    ENDING_INVENTORY = "ending_inventory"
    DIRECT_MATERIAL = "direct_material"
    DIRECT_LABOR = "direct_labor"
    FACTORY_OVERHEAD = "factory_overhead"
    SALES_EXPENSES = "sales_expenses"
    ADMINISTRATIVE_EXPENSES = "administrative_expenses"
    FINANCIAL_EXPENSES = "financial_expenses"
    OTHER_EXPENSES = "other_expenses"
    OTHER_PRODUCTS = "other_products"


class AccountBase(BaseModel):
    account_code: str = Field(title="Account Code", alias="accountCode")
    account_name: str = Field(title="Account Name", alias="accountName")
    is_group: bool | None = Field(title="Group", alias="isGroup", default=None)
    is_subgroup: bool | None = Field(title="Subgroup", alias="isSubgroup", default=None)
    is_entity: bool | None = Field(title="Entity", alias="isEntity", default=None)

    def __init__(self, **data):
        super().__init__(**data)
        codes = len(self.account_code.split("."))
        self.is_entity = codes >= 3
        self.is_subgroup = codes == 2
        self.is_group = codes == 1

    def get_group(self):
        codes = self.account_code.split(".")
        return codes[0]


class BalanceType(str, Enum):
    DEBIT = "Debit"
    CREDIT = "Credit"


class EntryBase(BaseModel):
    entry_number: int = Field(title="Entry Number", alias="entryNumber")
    date: date
    debit: float
    credit: float


class Account(AccountBase):
    description: str = ""
    related_accounts: list[str] = Field(
        title="Accounts related", alias="relatedAccounts", default=[]
    )
    income_statement_account_name: str = Field(
        title="Income Statement Account Name",
        alias="incomeStatementAccountName",
        default="",
    )
    in_balance_sheet: bool = Field(
        title="Belongs to Balance Sheet", alias="inBalanceSheet", default=True
    )


class AccountCatalog(BaseModel):
    accounts: list[Account] = []


class JournalBookEntry(EntryBase):
    concept: str
    account: AccountBase
    unbalanced: bool | None = None


class JournalBook(BaseModel):
    journal_book_entries: list[JournalBookEntry] = Field(
        title="Journal Book Entries", alias="journalBookEntries"
    )
    unbalanced: bool | None = None
    unbalanced_entries: list[JournalBookEntry] = Field(
        title="Unbalanced Entries", alias="unbalancedEntries", default=[]
    )


class LedgerBookAccount(AccountBase):
    entries: list[EntryBase]
    debit: float
    credit: float
    balance: float
    balance_type: BalanceType = Field(title="Balance Type", alias="balanceType")


class LedgerBook(BaseModel):
    ledger_book_entries: list[LedgerBookAccount] = Field(
        title="Ledger Book Entries", alias="ledgerBookEntries"
    )


class TrialBalanceAccount(AccountBase):
    debit: float
    credit: float
    debit_balance: float = Field(title="Debit Balance", alias="debitBalance")
    credit_balance: float = Field(title="Credit Balance", alias="creditBalance")
    balance: float


class TrialBalance(BaseModel):
    accounts_summary: list[TrialBalanceAccount] = Field(
        title="Accounts Summary", alias="accountsSummary"
    )
    total_debit: float = Field(title="Total Debit", alias="totalDebit")
    total_credit: float = Field(title="Total Credit", alias="totalCredit")
    total_debit_balance: float = Field(
        title="Total Debit Balance", alias="totalDebitBalance"
    )
    total_credit_balance: float = Field(
        title="Total Credit Balance", alias="totalCreditBalance"
    )
    is_balanced: bool = Field(title="Is Balanced", alias="isBalanced")

    def get_balance(self, account_code: str) -> float:
        """
        Get account balance of Trial Balance.
        :param account_code: Account code like query.
        :return: Account balance.
        """
        for account in self.accounts_summary:
            if account.account_code == account_code:
                return account.balance
        return 0.0


class NetSales(BaseModel):
    sales: float
    sales_returns: float
    sales_discounts: float
    sales_allowances: float
    net_sales: float = 0

    def __init__(self, **data):
        super().__init__(**data)
        net_sales = (
            self.sales
            - self.sales_returns
            - self.sales_discounts
            - self.sales_allowances
        )
        self.net_sales = net_sales


class NetPurchases(BaseModel):
    purchases: float
    purchasing_expenses: float
    total_purchases: float = 0
    purchases_returns: float
    purchases_discounts: float
    purchases_allowances: float
    net_purchases: float = 0

    def __init__(self, **data):
        super().__init__(**data)
        total_purchases = self.purchases + self.purchasing_expenses
        net_purchases = (
            total_purchases
            - self.purchases_returns
            - self.purchases_discounts
            - self.purchases_allowances
        )

        self.total_purchases = total_purchases
        self.net_purchases = net_purchases


class SalesCost(BaseModel):
    beginning_inventory: float
    purchases: float
    ending_inventory: float
    sales_cost: float = 0

    def __init__(self, **data):
        super().__init__(**data)
        sales_cost = self.beginning_inventory + self.purchases - self.ending_inventory

        self.sales_cost = sales_cost


class ProductionCost(BaseModel):
    direct_material: float
    direct_labor: float
    factory_overhead: float
    production_costs: float = 0

    def __init__(self, **data):
        super().__init__(**data)
        production_costs = (
            self.direct_material + self.direct_labor + self.factory_overhead
        )

        self.production_costs = production_costs


class GrossMargin(BaseModel):
    sales_revenue: float
    sales_cost: float
    gross_profit: float = 0

    def __init__(self, **data):
        super().__init__(**data)
        self.gross_profit = self.sales_revenue - self.sales_cost


class OperatingExpenses(BaseModel):
    sales_expenses: float
    administrative_expenses: float
    financial_expenses: float
    operating_expenses: float = 0

    def __init__(self, **data):
        super().__init__(**data)
        self.operating_expenses = (
            self.sales_expenses + self.administrative_expenses + self.financial_expenses
        )


class OperatingIncome(BaseModel):
    gross_margin: float
    operating_expenses: float
    operating_income: float = 0

    def __init__(self, **data):
        super().__init__(**data)
        self.operating_income = self.gross_margin - self.operating_expenses


class IncomeBeforeTaxes(BaseModel):
    operating_income: float
    other_expenses: float
    other_products: float
    income_before_taxes: float = 0

    def __init__(self, **data):
        super().__init__(**data)
        income_before_taxes = (
            self.operating_income - self.other_expenses + self.other_products
        )
        self.income_before_taxes = income_before_taxes


class NetIncome(BaseModel):
    income_before_taxes: float
    tax_rate: float
    income_tax_expense: float = 0
    net_income: float = 0

    def __init__(self, **data):
        super().__init__(**data)
        if self.income_before_taxes > 0:
            income_tax_expense = self.income_before_taxes * self.tax_rate
            self.income_tax_expense = income_tax_expense
        self.net_income = self.income_before_taxes - self.income_tax_expense


class IncomeStatementAccounts(BaseModel):
    sales: float = 0
    sales_returns: float = 0
    sales_discounts: float = 0
    sales_allowances: float = 0
    purchases: float = 0
    purchasing_expenses: float = 0
    purchases_returns: float = 0
    purchases_discounts: float = 0
    purchases_allowances: float = 0
    beginning_inventory: float = 0
    ending_inventory: float = 0
    direct_material: float = 0
    direct_labor: float = 0
    factory_overhead: float = 0
    sales_expenses: float = 0
    administrative_expenses: float = 0
    financial_expenses: float = 0
    other_expenses: float = 0
    other_products: float = 0


class IncomeStatement(BaseModel):
    net_sales: NetSales
    net_purchases: NetPurchases
    sales_cost: SalesCost
    production_cost: ProductionCost
    gross_margin: GrossMargin
    operating_expenses: OperatingExpenses
    operating_income: OperatingIncome
    income_before_taxes: IncomeBeforeTaxes
    net_income: NetIncome


class BalanceSheetAccount(AccountBase):
    balance: float


class BalanceSheet(BaseModel):
    assets: dict[str, BalanceSheetAccount] = {}
    liability: dict[str, BalanceSheetAccount] = {}
    equity: dict[str, BalanceSheetAccount] = {}
