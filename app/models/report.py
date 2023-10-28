from pydantic import BaseModel


class AccountFile(BaseModel):
    accountCode: str
    accountName: str


class AccountExtendFile(AccountFile):
    description: str


# Account Catalog Models
class AccountCatalogFile(BaseModel):
    accounts: list[AccountExtendFile] = []
