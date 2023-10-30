import xlsxwriter

from app.models.financial_statement import (
    BalanceType,
    JournalBook,
    AccountCatalog,
    LedgerBook,
)


def generate_account_catalog_xlsx(
    account_catalog: AccountCatalog,
    output_path,
):
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(output_path)
    worksheet = workbook.add_worksheet()

    # Define headers
    headers = ["Codigo", "Cuenta", "Descripción"]

    # Write headers in the first row
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Write the data of accounts in successive files
    for row, account in enumerate(account_catalog.accounts, start=1):
        worksheet.write(row, 0, account.accountCode)
        worksheet.write(row, 1, account.accountName)
        worksheet.write(row, 2, account.description)

    # Close file
    workbook.close()


def generate_journal_book_xlsx(journal_book: JournalBook, output_path):
    # Crea un archivo XLSX en la ubicación de salida
    workbook = xlsxwriter.Workbook(output_path)
    worksheet = workbook.add_worksheet()

    # Define encabezados
    headers = ["Asiento", "Fecha", "Codigo", "Cuenta", "Concepto", "Debe", "Haber"]

    # Escribir los encabezados en la primera fila
    for col, header in enumerate(headers):
        worksheet.write(0, col, header)

    # Escribir los datos de las entradas del libro de diario en filas sucesivas
    for row, entry in enumerate(journal_book.journal_book_entries, start=1):
        worksheet.write(row, 0, entry.entry_number)
        worksheet.write(row, 1, entry.date.isoformat())
        worksheet.write(row, 2, entry.account.account_code)
        worksheet.write(row, 3, entry.account.account_name)
        worksheet.write(row, 4, entry.concept)
        worksheet.write(row, 5, entry.debit)
        worksheet.write(row, 6, entry.credit)

    # Cerrar el archivo
    workbook.close()


def generate_ledger_book_xlsx(ledger_book: LedgerBook, output_path):
    # Crea un archivo XLSX en la ubicación de salida
    workbook = xlsxwriter.Workbook(output_path)
    worksheet = workbook.add_worksheet()

    # Define encabezados
    headers = ["Fecha", "Asiento", "Debe", "Haber", "Asiento", "Fecha"]

    row = 0
    # Recorrer cada cuenta del libro mayor
    for account in ledger_book.ledger_book_entries:
        # Escribir el encabezado del codigo de cuenta
        worksheet.write(row, 0, account.account_code)
        row += 1
        # Escribir el encabezado del nombre de la cuenta
        worksheet.write(row, 0, account.account_name)
        row += 1

        # Escribir los encabezados de los registros
        for col, header in enumerate(headers):
            worksheet.write(row, col, header)
        row += 1

        # Escribir los datos de los registros del libro mayor en filas sucesivas
        debit_row = row
        credit_row = row
        for entry in account.entries:
            if entry.debit != 0:
                worksheet.write(debit_row, 0, entry.date.isoformat())
                worksheet.write(debit_row, 1, entry.entry_number)
                worksheet.write(debit_row, 2, entry.debit)
                debit_row += 1

            if entry.credit != 0:
                worksheet.write(credit_row, 4, entry.entry_number)
                worksheet.write(credit_row, 5, entry.date.isoformat())
                worksheet.write(credit_row, 3, entry.credit)
                credit_row += 1

            row = max(debit_row, credit_row)

        if len(account.entries) > 1:
            worksheet.write(row, 2, account.debit)
            worksheet.write(row, 3, account.credit)
            row += 1

        if account.balance_type == BalanceType.DEBIT:
            worksheet.write(row, 2, account.balance)
        if account.balance_type == BalanceType.CREDIT:
            worksheet.write(row, 3, account.balance)
        row += 2

    # Cerrar el archivo
    workbook.close()
