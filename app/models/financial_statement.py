from pydantic import BaseModel
from datetime import date


class Account(BaseModel):
    account_code: str
    account_name: str
    description: str


class BookEntry(Account):
    entry_number: int
    date: date
    debit: float
    credit: float


class JournalBook(BookEntry):
    entries: list[BookEntry]


class LedgerBook(Account):
    pass
