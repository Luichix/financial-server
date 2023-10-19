from collections import defaultdict

from app.models.financial_statement import (
    Account,
    AccountCatalog,
    AccountGroup,
    BalanceSheet,
    BalanceSheetAccount,
    BalanceType,
    EntryBase,
    IncomeStatement,
    JournalBook,
    JournalBookEntry,
    LedgerBook,
    LedgerBookAccount,
    TrialBalance,
    TrialBalanceAccount,
)


# Evaluate Data Dairy Book
from typing import List, Dict


def group_entries_by_entry_number(
    entries: List[JournalBookEntry],
) -> Dict[int, List[JournalBookEntry]]:
    # Creamos un diccionario para agrupar las entradas por entryNumber
    grouped_entries: Dict[int, List[JournalBookEntry]] = {}

    for entry in entries:
        entry_number = entry.entry_number
        if entry_number not in grouped_entries:
            grouped_entries[entry_number] = []
        grouped_entries[entry_number].append(entry)

    return grouped_entries


def evaluate_journal_book(journal_book: JournalBook) -> JournalBook:
    journal_book_entries = journal_book.journal_book_entries
    grouped_entries = group_entries_by_entry_number(journal_book_entries)

    evaluated_journal_book_entries = []
    unbalanced_entries = []
    unbalanced = False

    for entryNumber, entries in grouped_entries.items():
        debit_total = sum(entry.debit for entry in entries)
        credit_total = sum(entry.credit for entry in entries)

        is_unbalanced = debit_total != credit_total

        for entry in entries:
            entry.unbalanced = is_unbalanced

        if is_unbalanced:
            unbalanced = True
            unbalanced_entries.extend(entries)

        evaluated_journal_book_entries.extend(entries)

    return JournalBook(
        journalBookEntries=evaluated_journal_book_entries,
        unbalanced=unbalanced,
        unbalancedEntries=unbalanced_entries,
    )


def create_ledger_book(journal_book: JournalBook) -> LedgerBook:
    # Crear un diccionario para mantener los saldos de las cuentas en el libro mayor
    ledger_balances: dict[str, float] = defaultdict(float)
    ledger_debits: dict[str, float] = defaultdict(float)
    ledger_credits: dict[str, float] = defaultdict(float)

    # Crear un diccionario para mantener las entradas en el libro mayor
    ledger_entries: dict[str, LedgerBookAccount] = {}

    # Iterar a través de las entradas del libro diario
    for journal_entry in journal_book.journal_book_entries:
        # Obtener la cuenta de la entrada del libro diario
        account = journal_entry.account

        # Obtener el saldo actual de la cuenta en el libro mayor
        current_balance = ledger_balances.get(account.account_code, 0.0)
        current_debit = ledger_debits.get(account.account_code, 0.0)
        current_credit = ledger_credits.get(account.account_code, 0.0)

        # Actualizar el saldo con los débitos y créditos de la entrada
        current_balance += journal_entry.debit - journal_entry.credit
        current_debit += journal_entry.debit
        current_credit += journal_entry.credit

        # Determinar el tipo de saldo (Debit o Credit) según el saldo actual
        balance_type = BalanceType.DEBIT if current_balance > 0 else BalanceType.CREDIT

        # Actualizar el saldo en el diccionario de saldos del libro mayor
        ledger_balances[account.account_code] = current_balance
        ledger_debits[account.account_code] = current_debit
        ledger_credits[account.account_code] = current_credit

        # Crear una entrada en el libro mayor si aún no existe
        if account.account_code not in ledger_entries:
            ledger_entries[account.account_code] = LedgerBookAccount(
                accountCode=account.account_code,
                accountName=account.account_name,
                entries=[],
                debit=0.0,
                credit=0.0,
                balance=0.0,  # Inicializar el saldo a 0
                balanceType=balance_type,  # Establecer el tipo de saldo
            )

        # Agregar la entrada del libro diario al libro mayor
        ledger_entries[account.account_code].entries.append(
            EntryBase(
                entryNumber=journal_entry.entry_number,
                date=journal_entry.date,
                debit=journal_entry.debit,
                credit=journal_entry.credit,
            )
        )

    # Crear una lista de las cuentas en el libro mayor a partir del diccionario de entradas
    ledger_accounts = list(ledger_entries.values())

    # Calcular y asignar los saldos finales en las cuentas del libro mayor
    for ledger_account in ledger_accounts:
        ledger_account.balance = abs(ledger_balances[ledger_account.account_code])
        ledger_account.debit = ledger_debits[ledger_account.account_code]
        ledger_account.credit = ledger_credits[ledger_account.account_code]

    # Crear el libro mayor final
    ledger_book = LedgerBook(ledgerBookEntries=ledger_accounts)

    return ledger_book


def create_trial_balance(ledger_book: LedgerBook) -> TrialBalance:
    # Crear diccionarios para almacenar los totales de débito y crédito por tipo de saldo
    total_debit = 0
    total_credit = 0
    accounts_summary = []
    accounts_entries: dict[str, TrialBalanceAccount] = {}

    # Iterar a través de las cuentas en el libro mayor
    for account in ledger_book.ledger_book_entries:
        total_debit += account.debit
        total_credit += account.credit

        # Obtener el tipo de saldo de la cuenta
        balance_type = account.balance_type

        # Crear una entrada en el libro mayor si aún no existe
        if account.account_code not in accounts_entries:
            accounts_entries[account.account_code] = TrialBalanceAccount(
                accountCode=account.account_code,
                accountName=account.account_name,
                debit=account.debit,
                credit=account.credit,
                debitBalance=0.0,
                creditBalance=0.0,
                balance=0.0,
            )

        # Actualizar los totales de débito y crédito según el tipo de saldo
        if balance_type == BalanceType.DEBIT:
            accounts_entries[account.account_code].debit_balance = account.balance
        elif balance_type == BalanceType.CREDIT:
            accounts_entries[account.account_code].credit_balance = account.balance

        accounts_entries[account.account_code].balance = account.balance

    accounts_summary = list(accounts_entries.values())

    # Verificar si el libro mayor está equilibrado
    debit_balance = sum(account.debit_balance for account in accounts_summary)
    credit_balance = sum(account.credit_balance for account in accounts_summary)
    is_balanced = total_debit == total_credit and debit_balance == credit_balance

    # Crear el balance de comprobación como un diccionario
    trial_balance = TrialBalance(
        accountsSummary=accounts_summary,
        totalDebit=total_debit,
        totalCredit=total_credit,
        totalDebitBalance=debit_balance,
        totalCreditBalance=credit_balance,
        isBalanced=is_balanced,
    )

    return trial_balance


def create_income_statement(
    trial_balance: TrialBalance, account_catalog: AccountCatalog, tax_rate: float
) -> IncomeStatement:
    revenue_accounts: dict[str, TrialBalanceAccount] = {}
    expense_accounts: dict[str, TrialBalanceAccount] = {}
    last_column = 0

    # evaluate income group account
    for account in trial_balance.accounts_summary:
        account_group = account.get_group()
        if account_group == AccountGroup.REVENUE:
            revenue_accounts[account.account_code] = account
        elif account_group == AccountGroup.EXPENSE:
            expense_accounts[account.account_code] = account

    income_statement = []

    for account in account_catalog.accounts:
        # Determinar si hay que añadirlo al estado de resultados
        if (
            account.get_group() in [AccountGroup.REVENUE, AccountGroup.EXPENSE]
            and account.in_income_statement
        ):
            # Comprobar si la cuenta existe en el Balance de Comprobación
            if account.account_code in revenue_accounts:
                balance = revenue_accounts[account.account_code].balance
            elif account.account_code in expense_accounts:
                balance = expense_accounts[account.account_code].balance
            else:
                balance = 0.0  # Valor predeterminado si la cuenta no existe en el Balance de Comprobación

            # Determinar la posicion en la que hay que añadirlo
            column = account.order_in_income_statement
            column_values = [None, None, None, None]
            column_values[column] = balance

            if column > last_column:
                last_column = column

            row = [account.account_name] + column_values
            income_statement.append(row)

    last_column += 1

    column_values = [None, None, None, None]
    before_tax = ["UTILIDAD ANTES DE IMPUESTOS"] + column_values
    total_revenue = sum(
        account.balance
        for account in revenue_accounts.values()
        if account.order_in_income_statement == last_column
    )
    total_expense = sum(
        account.balance
        for account in expense_accounts.values()
        if account.order_in_income_statement == last_column
    )
    before_tax_value = total_revenue - total_expense
    before_tax[last_column] = round(before_tax_value, 2)

    tax = ["IMPUESTOS"] + column_values
    tax_value = before_tax_value * tax_rate
    tax[last_column] = round(tax_value, 2)

    profit_or_loss = ["UTILIDAD O PERDIDA DEL EJERCICIO"] + column_values
    profit_or_loss_value = before_tax_value - tax_value
    profit_or_loss[last_column] = round(profit_or_loss_value, 2)

    income_statement.append(before_tax)
    income_statement.append(tax)
    income_statement.append(profit_or_loss)

    return IncomeStatement(
        entries=income_statement,
        beforeTax=before_tax_value,
        tax=tax_value,
        profitOrLoss=profit_or_loss_value,
    )


def create_balance_sheet(
    trial_balance: TrialBalance, account_catalog: AccountCatalog
) -> BalanceSheet:
    balance_sheet = BalanceSheet()

    for account in account_catalog.accounts:
        if account.in_balance_sheet:
            if account.get_group() == AccountGroup.ASSETS:
                balance_sheet.assets[account.account_code] = BalanceSheetAccount(
                    accountCode=account.account_code,
                    accountName=account.account_name,
                    balance=get_account_balance(account, trial_balance),
                )
            elif account.get_group() == AccountGroup.LIABILITIES:
                balance_sheet.liability[account.account_code] = BalanceSheetAccount(
                    accountCode=account.account_code,
                    accountName=account.account_name,
                    balance=get_account_balance(account, trial_balance),
                )
            elif account.get_group() == AccountGroup.EQUITY:
                balance_sheet.equity[account.account_code] = BalanceSheetAccount(
                    accountCode=account.account_code,
                    accountName=account.account_name,
                    balance=get_account_balance(account, trial_balance),
                )

    return balance_sheet


def get_account_balance(account: Account, trial_balance: TrialBalance):
    return trial_balance.get_balance(account.account_code)
