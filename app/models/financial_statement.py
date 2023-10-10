from enum import Enum
from pydantic import BaseModel
from datetime import date


class BalanceType(str, Enum):
    DEBIT = "Debit"
    CREDIT = "Credit"


class AccountBase(BaseModel):
    account_code: str
    account_name: str
    account_group: str


class EntryBase(BaseModel):
    entry_number: int
    date: date
    debit: float
    credit: float


class Account(AccountBase):
    description: str


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


class TrialBalanceSummary(BaseModel):
    total_debit: float
    total_credit: float
    debit_balance: float
    credit_balance: float


class TrialBalanceAccount(AccountBase, TrialBalanceSummary):
    pass


class TrialBalance(TrialBalanceSummary):
    accounts_summary: list[TrialBalanceAccount]
    is_balanced: bool
