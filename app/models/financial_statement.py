from enum import Enum
from pydantic import BaseModel
from datetime import date


class AccountGroup(str, Enum):
    ASSETS = 1
    LIABILITIES = 2
    EQUITY = 3
    REVENUE = 4
    EXPENSE = 5


class AccountBase(BaseModel):
    account_code: str
    account_name: str
    is_group: bool | None = None
    is_subgroup: bool | None = None
    is_entity: bool | None = None

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
    entry_number: int
    date: date
    debit: float
    credit: float


class Account(AccountBase):
    description: str
    related_accounts: list[str] = []  # Lista de cuentas relacionadas
    belongs_to_income_statement: bool = False
    order_in_income_statement: int = 0
    related_income_statement_account: str | None = None
    is_creditor: bool = False

    def is_debtor(self):
        return not self.is_creditor


class AccountCatalog(BaseModel):
    accounts: list[Account] = []


class JournalBookEntry(EntryBase):
    concept: str
    account: AccountBase
    unbalanced: bool | None = None


class JournalBook(BaseModel):
    journal_book_entries: list[JournalBookEntry]
    unbalanced: bool | None = None
    unbalanced_entries: list[JournalBookEntry] = []


class LedgerBookAccount(AccountBase):
    entries: list[EntryBase]
    debit: float
    credit: float
    balance: float
    balance_type: BalanceType


class LedgerBook(BaseModel):
    ledger_book_entries: list[LedgerBookAccount]


class TrialBalanceAccount(AccountBase):
    debit: float
    credit: float
    debit_balance: float
    credit_balance: float
    balance: float


class TrialBalance(BaseModel):
    accounts_summary: list[TrialBalanceAccount]
    total_debit: float
    total_credit: float
    total_debit_balance: float
    total_credit_balance: float
    is_balanced: bool


class IncomeStatement(BaseModel):
    entries: list[list]
