from collections import defaultdict

from app.models.financial_statement import (
    Account,
    BalanceType,
    EntryBase,
    JournalBook,
    LedgerBook,
    LedgerBookAccount,
    TrialBalance,
    TrialBalanceAccount,
)


def accounts_catalog():
    catalog: list[Account] = [
        {
            "account_code": 1,
            "account_name": "ACTIVO",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 101,
            "account_name": "ACTIVO CIRCULANTE",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10101,
            "account_name": "CAJA GENERAL",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10102,
            "account_name": "CAJA CHICA",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10103,
            "account_name": "BANCOS",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10104,
            "account_name": "INVENTARIOS",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10105,
            "account_name": "CLIENTES",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10106,
            "account_name": "DOCUMENTOS POR COBRAR",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10107,
            "account_name": "DEUDORES DIVERSOS",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10108,
            "account_name": "FUNCIONARIOS Y EMPLEADOS",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10109,
            "account_name": "PAPELERIA Y UTILES",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 102,
            "account_name": "ACTIVO FIJO",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10201,
            "account_name": "TERRENO",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10202,
            "account_name": "EDIFICIO",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10203,
            "account_name": "MAQUINARIA Y EQUIPO",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10204,
            "account_name": "MOBILIARIO Y EQUIPO DE OFICINA",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10205,
            "account_name": "EQUIPO DE TRANSPORTE",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 10206,
            "account_name": "EQUIPO DE ENTREGA Y REPARTO",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 2,
            "account_name": "PASIVO",
            "account_group": 1,
            "description": "",
        },
        {
            "account_code": 201,
            "account_name": "PASIVO CIRCULANTE",
            "account_group": 2,
            "description": "",
        },
        {
            "account_code": 20101,
            "account_name": "PROVEEDORES",
            "account_group": 2,
            "description": "",
        },
        {
            "account_code": 20102,
            "account_name": "ACREEDORES DIVERSOS",
            "account_group": 2,
            "description": "",
        },
        {
            "account_code": 20103,
            "account_name": "DOCUMENTOS POR PAGAR",
            "account_group": 2,
            "description": "",
        },
        {
            "account_code": 20104,
            "account_name": "IMPUESTOS POR PAGAR",
            "account_group": 2,
            "description": "",
        },
        {
            "account_code": 20105,
            "account_name": "INTERESES POR PAGAR",
            "account_group": 2,
            "description": "",
        },
        {
            "account_code": 20106,
            "account_name": "SUELDOS ACUMULADOS POR PAGAR",
            "account_group": 2,
            "description": "",
        },
        {
            "account_code": 202,
            "account_name": "PASIVO FIJO",
            "account_group": 2,
            "description": "",
        },
        {
            "account_code": 20201,
            "account_name": "DOCUMENTOS POR PAGAR A LARGO PLAZO",
            "account_group": 2,
            "description": "",
        },
        {
            "account_code": 3,
            "account_name": "PATRIMONIO",
            "account_group": 3,
            "description": "",
        },
        {
            "account_code": 301,
            "account_name": "CAPITAL SOCIAL",
            "account_group": 3,
            "description": "",
        },
        {
            "account_code": 30101,
            "account_name": "CAPITAL CONTABLE",
            "account_group": 3,
            "description": "",
        },
        {
            "account_code": 302,
            "account_name": "UTILIDAD O PERDIDA DEL EJERCICIO",
            "account_group": 3,
            "description": "",
        },
        {
            "account_code": 30201,
            "account_name": "UTILIDAD O PERDIDA DEL EJERCICIO",
            "account_group": 3,
            "description": "",
        },
        {
            "account_code": 4,
            "account_name": "INGRESOS",
            "account_group": 4,
            "description": "",
        },
        {
            "account_code": 401,
            "account_name": "INGRESOS POR VENTAS",
            "account_group": 4,
            "description": "",
        },
        {
            "account_code": 40101,
            "account_name": "VENTAS POR ACTIVIDAD",
            "account_group": 4,
            "description": "",
        },
        {
            "account_code": 5,
            "account_name": "EGRESOS",
            "account_group": 5,
            "description": "",
        },
        {
            "account_code": 501,
            "account_name": "GASTOS OPERATIVOS",
            "account_group": 5,
            "description": "",
        },
        {
            "account_code": 50101,
            "account_name": "GASTOS DE ADMINISTRACIÓN",
            "account_group": 5,
            "description": "",
        },
        {
            "account_code": 50102,
            "account_name": "GASTOS DE VENTA",
            "account_group": 5,
            "description": "",
        },
        {
            "account_code": 50103,
            "account_name": "GASTOS FINANCIEROS",
            "account_group": 5,
            "description": "",
        },
        {
            "account_code": 6,
            "account_name": "COSTOS",
            "account_group": 6,
            "description": "",
        },
        {
            "account_code": 601,
            "account_name": "COSTOS DE PRODUCCIÓN",
            "account_group": 6,
            "description": "",
        },
        {
            "account_code": 60101,
            "account_name": "COSTOS DE MATERIALES",
            "account_group": 6,
            "description": "",
        },
        {
            "account_code": 60102,
            "account_name": "COSTOS DE MANO DE OBRA",
            "account_group": 6,
            "description": "",
        },
        {
            "account_code": 60103,
            "account_name": "COSTOS INDIRECTOS DE FABRICACIÓN",
            "account_group": 6,
            "description": "",
        },
        {
            "account_code": 7,
            "account_name": "CUENTA DE CIERRE",
            "account_group": 7,
            "description": "",
        },
        {
            "account_code": 701,
            "account_name": "RESUMEN DE INGRESOS Y GASTOS",
            "account_group": 7,
            "description": "",
        },
        {
            "account_code": 70101,
            "account_name": "PERDIDAS Y GANANCIAS",
            "account_group": 7,
            "description": "",
        },
    ]


# Evaluate Data Dairy Book
def evaluate_journal_book(journal_book: JournalBook) -> JournalBook:
    journal_book_entries = journal_book.journal_book_entries
    unbalanced_entries = []
    unbalanced = None
    for entry in journal_book_entries:
        debit_total = sum(
            entry.debit
            for entry in journal_book_entries
            if entry.entry_number == entry.entry_number
        )
        credit_total = sum(
            entry.credit
            for entry in journal_book_entries
            if entry.entry_number == entry.entry_number
        )

        if debit_total != credit_total:
            entry.unbalanced = True
            unbalanced_entries.append(entry)
        else:
            entry.unbalanced = False

    if not unbalanced_entries:
        unbalanced = False
    else:
        unbalanced = True

    return JournalBook(
        journal_book_entries=journal_book_entries,
        unbalanced=unbalanced,
        unbalanced_entries=unbalanced_entries,
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
                account_code=account.account_code,
                account_name=account.account_name,
                account_group=account.account_group,
                entries=[],
                debit=0.0,
                credit=0.0,
                balance=0.0,  # Inicializar el saldo a 0
                balance_type=balance_type,  # Establecer el tipo de saldo
            )

        # Agregar la entrada del libro diario al libro mayor
        ledger_entries[account.account_code].entries.append(
            EntryBase(
                entry_number=journal_entry.entry_number,
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
    ledger_book = LedgerBook(ledger_book_entries=ledger_accounts)

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
                account_code=account.account_code,
                account_name=account.account_name,
                account_group=account.account_group,
                total_debit=account.debit,
                total_credit=account.credit,
                debit_balance=0.0,
                credit_balance=0.0,
            )

        # Actualizar los totales de débito y crédito según el tipo de saldo
        if balance_type == BalanceType.DEBIT:
            accounts_entries[account.account_code].debit_balance = account.balance
        elif balance_type == BalanceType.CREDIT:
            accounts_entries[account.account_code].credit_balance = account.balance

    accounts_summary = list(accounts_entries.values())

    # Verificar si el libro mayor está equilibrado
    debit_balance = sum(account.debit_balance for account in accounts_summary)
    credit_balance = sum(account.credit_balance for account in accounts_summary)
    is_balanced = total_debit == total_credit and debit_balance == credit_balance

    # Crear el balance de comprobación como un diccionario
    trial_balance = TrialBalance(
        accounts_summary=accounts_summary,
        total_debit=total_debit,
        total_credit=total_credit,
        debit_balance=debit_balance,
        credit_balance=credit_balance,
        is_balanced=is_balanced,
    )

    return trial_balance
