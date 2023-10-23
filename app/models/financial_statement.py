from enum import Enum
from pydantic import BaseModel, Field, validator
from datetime import date


# Setup Accounts Models
class AccountGroup(str, Enum):
    ASSETS = 1
    LIABILITIES = 2
    EQUITY = 3
    REVENUE = 4
    EXPENSE = 5


class BalanceType(str, Enum):
    DEBIT = "debit"
    CREDIT = "credit"


class AccountingMethod(str, Enum):
    PERPETUAL = "perpetual"
    ANALYTICAL = "analytical"


class IncomeStatementAccountNames(str, Enum):
    SALES = "sales"
    SALES_RETURNS = "salesReturns"
    SALES_DISCOUNTS = "salesDiscounts"
    SALES_ALLOWANCES = "salesAllowances"
    SALES_COST = "salesCost"
    PURCHASES = "purchases"
    PURCHASING_EXPENSES = "purchasingExpenses"
    PURCHASES_RETURNS = "purchasesReturns"
    PURCHASES_DISCOUNTS = "purchasesDiscounts"
    PURCHASES_ALLOWANCES = "purchasesAllowances"
    BEGINNING_INVENTORY = "beginningInventory"
    ENDING_INVENTORY = "endingInventory"
    DIRECT_MATERIAL = "directMaterial"
    DIRECT_LABOR = "directLabor"
    FACTORY_OVERHEAD = "factoryOverhead"
    SALES_EXPENSES = "salesExpenses"
    ADMINISTRATIVE_EXPENSES = "administrativeExpenses"
    FINANCIAL_EXPENSES = "financialExpenses"
    OTHER_EXPENSES = "otherExpenses"
    OTHER_PRODUCTS = "otherProducts"

    @classmethod
    def get_values(cls):
        return [item.value for item in cls]


# Entry Models
class EntryBase(BaseModel):
    entry_number: int = Field(title="Entry Number", alias="entryNumber")
    date: date
    debit: float
    credit: float


# Account Models
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

    def get_subgroup(self):
        codes = self.account_code.split(".")
        if len(codes) >= 2:
            return ".".join([codes[0], codes[1]])


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


# Account Catalog Models
class AccountCatalog(BaseModel):
    accounts: list[Account] = []


# Journal Book Models
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


# Ledger Book Models
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


# Trial Balance Models
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


# Income Statement Models
class NetSales(BaseModel):
    sales: float
    sales_returns: float = Field(alias="salesReturns")
    sales_discounts: float = Field(alias="salesDiscounts")
    sales_allowances: float = Field(alias="salesAllowances")
    net_sales: float = Field(alias="netSales", default=0)

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
    purchasing_expenses: float = Field(alias="purchasingExpenses")
    total_purchases: float = Field(alias="totalPurchases", default=0)
    purchases_returns: float = Field(alias="purchasesReturns")
    purchases_discounts: float = Field(alias="purchasesDiscounts")
    purchases_allowances: float = Field(alias="purchasesAllowances")
    net_purchases: float = Field(alias="netPurchases", default=0)

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


class SalesCostPerpetual(BaseModel):
    sales_cost: float = Field(alias="salesCost")


class SalesCostAnalytical(BaseModel):
    beginning_inventory: float = Field(alias="beginningInventory")
    purchases: float
    ending_inventory: float = Field(alias="endingInventory")
    sales_cost: float = Field(alias="salesCost", default=0)

    def __init__(self, **data):
        super().__init__(**data)
        sales_cost = self.beginning_inventory + self.purchases - self.ending_inventory

        self.sales_cost = sales_cost


class GrossMargin(BaseModel):
    sales_revenue: float = Field(alias="salesRevenue")
    sales_cost: float = Field(alias="salesCost")
    gross_profit: float = Field(alias="grossProfit", default=0)

    def __init__(self, **data):
        super().__init__(**data)
        self.gross_profit = self.sales_revenue - self.sales_cost


class OperatingExpenses(BaseModel):
    sales_expenses: float = Field(alias="salesExpenses")
    administrative_expenses: float = Field(alias="administrativeExpenses")
    financial_expenses: float = Field(alias="financialExpenses")
    operating_expenses: float = Field(alias="operatingExpenses", default=0)

    def __init__(self, **data):
        super().__init__(**data)
        self.operating_expenses = (
            self.sales_expenses + self.administrative_expenses + self.financial_expenses
        )


class OperatingIncome(BaseModel):
    gross_margin: float = Field(alias="grossMargin")
    operating_expenses: float = Field(alias="operatingExpenses")
    operating_income: float = Field(alias="operatingIncome", default=0)

    def __init__(self, **data):
        super().__init__(**data)
        self.operating_income = self.gross_margin - self.operating_expenses


class IncomeBeforeTaxes(BaseModel):
    operating_income: float = Field(alias="operatingIncome")
    other_expenses: float = Field(alias="otherExpenses")
    other_products: float = Field(alias="otherProducts")
    income_before_taxes: float = Field(alias="incomeBeforeTaxes", default=0)

    def __init__(self, **data):
        super().__init__(**data)
        income_before_taxes = (
            self.operating_income - self.other_expenses + self.other_products
        )
        self.income_before_taxes = income_before_taxes


class NetIncome(BaseModel):
    income_before_taxes: float = Field(alias="incomeBeforeTaxes")
    tax_rate: float = Field(alias="taxRate")
    income_tax_expense: float = Field(alias="incomeTaxExpense", default=0)
    net_income: float = Field(alias="netIncome", default=0)

    def __init__(self, **data):
        super().__init__(**data)
        if self.income_before_taxes > 0:
            income_tax_expense = self.income_before_taxes * self.tax_rate
            self.income_tax_expense = income_tax_expense
        self.net_income = self.income_before_taxes - self.income_tax_expense


class IncomeStatementAccounts(BaseModel):
    sales: float = 0
    sales_returns: float = Field(alias="salesReturns", default=0)
    sales_discounts: float = Field(alias="salesDiscounts", default=0)
    sales_allowances: float = Field(alias="salesAllowances", default=0)
    sales_cost: float = Field(alias="salesCost", default=0)
    purchases: float = 0
    purchasing_expenses: float = Field(alias="purchasingExpenses", default=0)
    purchases_returns: float = Field(alias="purchasesReturns", default=0)
    purchases_discounts: float = Field(alias="purchasesDiscounts", default=0)
    purchases_allowances: float = Field(alias="purchasesAllowances", default=0)
    beginning_inventory: float = Field(alias="beginningInventory", default=0)
    ending_inventory: float = Field(alias="endingInventory", default=0)
    direct_material: float = Field(alias="directMaterial", default=0)
    direct_labor: float = Field(alias="directLabor", default=0)
    factory_overhead: float = Field(alias="factoryOverhead", default=0)
    sales_expenses: float = Field(alias="salesExpenses", default=0)
    administrative_expenses: float = Field(alias="administrativeExpenses", default=0)
    financial_expenses: float = Field(alias="financialExpenses", default=0)
    other_expenses: float = Field(alias="otherExpenses", default=0)
    other_products: float = Field(alias="otherProducts", default=0)


class IncomeStatementBase(BaseModel):
    net_sales: NetSales = Field(alias="netSales")
    gross_margin: GrossMargin = Field(alias="grossMargin")
    operating_expenses: OperatingExpenses = Field(alias="operatingExpenses")
    operating_income: OperatingIncome = Field(alias="operatingIncome")
    income_before_taxes: IncomeBeforeTaxes = Field(alias="incomeBeforeTaxes")
    net_income: NetIncome = Field(alias="netIncome")


class PerpetualMethod(IncomeStatementBase):
    sales_cost: SalesCostPerpetual = Field(alias="salesCost")


class AnalyticalMethod(IncomeStatementBase):
    net_purchases: NetPurchases = Field(alias="netPurchases")
    sales_cost: SalesCostAnalytical = Field(alias="salesCost")


class IncomeStatement(BaseModel):
    accounting_method: AccountingMethod = Field(alias="accountingMethod")
    earnings_income: AnalyticalMethod | PerpetualMethod = Field(alias="earningsIncome")


# Balance Sheet Models
class BalanceSheetAccount(AccountBase):
    balance: float


class BalanceSheetSubgroup(BaseModel):
    subgroup: BalanceSheetAccount = {}
    entities: dict[str, BalanceSheetAccount] = {}


class BalanceSheetGroup(BaseModel):
    group: BalanceSheetAccount = {}
    subgroups: dict[str, BalanceSheetSubgroup] = {}


class BalanceSheet(BaseModel):
    assets: BalanceSheetGroup = BalanceSheetGroup()
    liability: BalanceSheetGroup = BalanceSheetGroup()
    equity: BalanceSheetGroup = BalanceSheetGroup()


# Production and Sales Cost Statement Models
class ProductionCost(BaseModel):
    direct_material: float = Field(alias="directMaterial")
    direct_labor: float = Field(alias="directLabor")
    factory_overhead: float = Field(alias="factoryOverhead")
    production_costs: float = Field(alias="productionCosts", default=0)

    def __init__(self, **data):
        super().__init__(**data)
        production_costs = (
            self.direct_material + self.direct_labor + self.factory_overhead
        )

        self.production_costs = production_costs
