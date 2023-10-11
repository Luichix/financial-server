from enum import Enum
from pydantic import BaseModel, Field
from datetime import date


class AccountGroup(str, Enum):
    ASSETS = 1
    LIABILITIES = 2
    EQUITY = 3
    REVENUE = 4
    EXPENSE = 5


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
    in_income_statement: bool = Field(
        title="Belongs to Income Statement", alias="inIncomeStatement", default=False
    )
    in_balance_sheet: bool = Field(
        title="Belongs to Balance Sheet", alias="inBalanceSheet", default=True
    )
    order_in_income_statement: int = Field(
        title="Order in Income Statement",
        description="Column position u order into the Income Statement",
        alias="orderInIncomeStatement",
        default=0,
    )
    related_income_statement_account: str | None = Field(
        title="Related Income Statement Account",
        alias="relatedIncomeStatementAccount",
        default=None,
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


class IncomeStatement(BaseModel):
    entries: list[list]
    before_tax: float = Field(title="Before Tax", alias="beforeTax")
    tax: float
    profit_or_loss: float = Field(title="Profit or Loss", alias="profitOrLoss")


class BalanceSheetAccount(AccountBase):
    balance: float


class BalanceSheet(BaseModel):
    assets: dict[str, BalanceSheetAccount] = {}
    liability: dict[str, BalanceSheetAccount] = {}
    equity: dict[str, BalanceSheetAccount] = {}
