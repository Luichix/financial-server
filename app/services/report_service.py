import xlsxwriter

from app.models.amortization import OutLoanAmortization

from app.models.financial_statement import (
    AccountingMethod,
    BalanceSheet,
    BalanceType,
    IncomeStatement,
    JournalBook,
    AccountCatalog,
    LedgerBook,
    TrialBalance,
)
from app.models.report import TypeFrecuencyName, TypePeriodName


def generate_amortization_table_xlsx(
    amortization_table: OutLoanAmortization, output_path
):
    # Crear un nuevo archivo de Excel
    workbook = xlsxwriter.Workbook(output_path)
    worksheet = workbook.add_worksheet()

    # Definir formatos para celdas
    bold_format = workbook.add_format({"bold": True})
    money_format = workbook.add_format({"num_format": "#,##0.00"})
    number_format = workbook.add_format({"num_format": "#,##0"})
    rate_format = workbook.add_format({"num_format": "0.00%"})
    right_format = workbook.add_format({"align": "right"})

    row = 0

    worksheet.write_string(row, 0, "Resultados", bold_format)
    row += 2

    # Resumen de datos de pagos
    worksheet.write_string(row, 0, "Principal:", bold_format)
    worksheet.write_number(row, 1, amortization_table.principal, money_format)
    row += 1
    worksheet.write_string(row, 0, "Intereses:", bold_format)
    worksheet.write_number(row, 1, amortization_table.interest_payment, money_format)
    row += 1
    worksheet.write_string(row, 0, "Comisiones:", bold_format)
    worksheet.write_number(row, 1, amortization_table.disbursement_fee, money_format)
    row += 1

    for label, amount in amortization_table.recurring_payments.items():
        worksheet.write_string(row, 0, label, bold_format)
        worksheet.write_number(row, 1, amount, money_format)
        row += 1

    worksheet.write_string(row, 0, "Pagos Adicionales:", bold_format)
    worksheet.write_number(row, 1, amortization_table.additional_payment, money_format)
    row += 1

    worksheet.write_string(row, 0, "Total de Pagos", bold_format)
    worksheet.write_number(row, 1, amortization_table.total_amount_pay, money_format)
    row += 1

    # Resumen de datos de amortizacion
    row_data = 2
    worksheet.write_string(row_data, 3, "Principal e Intereses:", bold_format)
    worksheet.write_number(row_data, 4, amortization_table.fee_payment, money_format)
    row_data += 1

    worksheet.write_string(row_data, 3, "Tasa de Interes:", bold_format)
    worksheet.write_number(
        row_data, 4, amortization_table.interest_rate / 100, rate_format
    )
    worksheet.write_string(
        row_data,
        5,
        TypeFrecuencyName[amortization_table.interest_rate_type],
        money_format,
    )
    row_data += 1
    worksheet.write_string(row_data, 3, "Numero de Periodos:", bold_format)
    worksheet.write_number(
        row_data, 4, amortization_table.periods_number, number_format
    )
    worksheet.write_string(row_data, 5, TypePeriodName[amortization_table.periods_type])
    row_data += 1
    worksheet.write_string(row_data, 3, "Frecuencia de Pago:", bold_format)
    worksheet.write_string(
        row_data,
        4,
        TypeFrecuencyName[amortization_table.payment_frecuency],
        right_format,
    )
    row_data += 1
    worksheet.write_string(row_data, 3, "Numero de Cuotas:", bold_format)
    worksheet.write_number(
        row_data, 4, amortization_table.number_installments, number_format
    )
    worksheet.write_string(row_data, 5, "Cuotas")
    row_data += 1
    worksheet.write_string(row_data, 3, "Periodo de Gracia:", bold_format)
    worksheet.write_number(row_data, 4, amortization_table.grace_period, number_format)
    worksheet.write_string(row_data, 5, "Cuotas")

    row += 2

    # Escribir los encabezados
    headers = ["Periodo", "Principal", "Cuota de Pago", "Intereses", "Amortización"]
    worksheet.write_row(row, 0, headers, bold_format)

    col = 5

    worksheet.write_string(row, col, "Pagos Adicionales", bold_format)
    col += 1

    for label, amount in amortization_table.recurring_payments.items():
        worksheet.write_string(row, col, label, bold_format)
        col += 1
    row += 1

    # Escribir los datos de la tabla de amortización
    for i, data in enumerate(amortization_table.amortization_table):
        row_number = i + row  # Empezar desde la segunda fila
        worksheet.write_number(row_number, 0, data.period)
        worksheet.write_number(row_number, 1, data.principal_payment, money_format)
        worksheet.write_number(row_number, 2, data.fee_payment, money_format)
        worksheet.write_number(row_number, 3, data.interest_payment, money_format)
        worksheet.write_number(row_number, 4, data.remaining_balance, money_format)

        col = 5

        worksheet.write_number(row_number, col, data.additional_payment, money_format)
        col += 1

        for label, amount in data.recurring_payments.items():
            worksheet.write_number(row_number, col, amount, money_format)
            col += 1

    # Escribir los totales
    last_row = len(amortization_table.amortization_table) + row
    worksheet.write(last_row, 0, "Total:", bold_format)
    worksheet.write(last_row, 1, amortization_table.principal, money_format)
    worksheet.write(last_row, 2, amortization_table.fee_payment, money_format)
    worksheet.write(last_row, 3, amortization_table.interest_payment, money_format)

    col = 5
    worksheet.write_number(
        last_row, col, amortization_table.additional_payment, money_format
    )
    col += 1
    for label, amount in amortization_table.recurring_payments.items():
        worksheet.write_number(last_row, col, amount, money_format)
        col += 1

    # Ajustar automáticamente el ancho de las columnas
    worksheet.set_column(0, col, 20)

    for row in range(0, last_row + 1):
        worksheet.set_row(row, 20)  # Establecer el alto para cada fila en el rango

    # Cerrar el archivo de Excel
    workbook.close()


def generate_account_catalog_xlsx(
    account_catalog: AccountCatalog,
    output_path,
):
    # Create an new Excel file and add a worksheet.
    workbook = xlsxwriter.Workbook(output_path)
    worksheet = workbook.add_worksheet()

    bold_format = workbook.add_format({"bold": True})

    # Define headers
    headers = ["Codigo", "Cuenta", "Descripción"]

    # Write headers in the first row
    for col, header in enumerate(headers):
        worksheet.write_string(0, col, header, bold_format)

    # Write the data of accounts in successive files
    for row, account in enumerate(account_catalog.accounts, start=1):
        worksheet.write(row, 0, account.account_code)
        worksheet.write_string(row, 1, account.account_name)
        worksheet.write_string(row, 2, account.description)

    # Ajustar automáticamente el ancho de las columnas
    worksheet.set_column(0, 0, None)
    worksheet.set_column(1, 1, 40)
    worksheet.set_column(2, 2, 40)

    last_row = len(account_catalog.accounts)
    for row in range(0, last_row + 1):
        worksheet.set_row(row, 18)  # Establecer el alto para cada fila en el rango

    # Close file
    workbook.close()


def generate_journal_book_xlsx(journal_book: JournalBook, output_path):
    # Crea un archivo XLSX en la ubicación de salida
    workbook = xlsxwriter.Workbook(output_path)
    worksheet = workbook.add_worksheet()

    bold_format = workbook.add_format({"bold": True})
    money_format = workbook.add_format({"num_format": "#,##0.00"})

    # Define encabezados
    headers = ["Asiento", "Fecha", "Codigo", "Cuenta", "Concepto", "Debe", "Haber"]

    # Escribir los encabezados en la primera row
    for col, header in enumerate(headers):
        worksheet.write(0, col, header, bold_format)

    # Escribir los datos de las entradas del libro de diario en filas sucesivas
    for row, entry in enumerate(journal_book.journal_book_entries, start=1):
        worksheet.write(row, 0, entry.entry_number)
        worksheet.write(row, 1, entry.date.isoformat())
        worksheet.write(row, 2, entry.account.account_code)
        worksheet.write(row, 3, entry.account.account_name)
        worksheet.write(row, 4, entry.concept)
        worksheet.write(row, 5, entry.debit, money_format)
        worksheet.write(row, 6, entry.credit, money_format)

    # Ajustar automáticamente el ancho de las columnas
    worksheet.set_column(3, 3, 30)
    worksheet.set_column(4, 4, 40)

    # Cerrar el archivo
    workbook.close()


def generate_ledger_book_xlsx(ledger_book: LedgerBook, output_path):
    # Crea un archivo XLSX en la ubicación de salida
    workbook = xlsxwriter.Workbook(output_path)
    worksheet = workbook.add_worksheet()

    # Define encabezados
    headers = ["", "#", "Debe", "Haber", "#", ""]

    # Add a bold format to use to highlight cells.
    header_format = workbook.add_format({"bold": True, "align": "center"})

    # Add a header with bottom border
    header_border = workbook.add_format({"bold": True, "align": "center", "bottom": 2})

    # Add a bottom border
    debit_format = workbook.add_format({"num_format": "#,##0.00", "right": 2})

    # Add a bottom border
    credit_format = workbook.add_format({"num_format": "#,##0.00", "left": 2})

    # Add a balance debit border format
    sub_balance_debit_format = workbook.add_format(
        {"num_format": "#,##0.00", "top": 1, "bottom": 1, "right": 2}
    )
    # Add a balance credit border format
    sub_balance_credit_format = workbook.add_format(
        {"num_format": "#,##0.00", "top": 1, "bottom": 1, "left": 2}
    )

    # Add a balance debit border format
    balance_debit_format = workbook.add_format(
        {"num_format": "#,##0.00", "top": 1, "right": 2}
    )
    # Add a balance credit border format
    balance_credit_format = workbook.add_format(
        {"num_format": "#,##0.00", "top": 1, "left": 2}
    )

    # Add an Excel date format.
    date_format = workbook.add_format({"num_format": "dd/mm/yyyy", "align": "center"})

    # Add an Excel entry number format.
    number_format = workbook.add_format({"align": "center"})

    row = 0
    # Recorrer cada account del libro mayor
    for account in ledger_book.ledger_book_entries:
        # Escribir el encabezado del codigo de account
        worksheet.merge_range(row, 2, row, 3, account.account_code, header_format)
        row += 1
        # Escribir el encabezado del nombre de la account
        worksheet.merge_range(row, 2, row, 3, account.account_name, header_format)

        row += 1

        # Escribir los encabezados de los registros
        for col, header in enumerate(headers):
            if col == 2 or col == 3:
                worksheet.write_string(row, col, header, header_border)
            else:
                worksheet.write_string(row, col, header, header_format)
        row += 1

        # Escribir los datos de los registros del libro mayor en filas sucesivas
        debit_row = row
        credit_row = row
        for entry in account.entries:
            if entry.debit != 0:
                worksheet.write_datetime(debit_row, 0, entry.date, date_format)
                worksheet.write(debit_row, 1, entry.entry_number, number_format)
                worksheet.write_number(debit_row, 2, entry.debit, debit_format)
                debit_row += 1

            if entry.credit != 0:
                worksheet.write_datetime(credit_row, 5, entry.date, date_format)
                worksheet.write(credit_row, 4, entry.entry_number, number_format)
                worksheet.write_number(credit_row, 3, entry.credit, credit_format)
                credit_row += 1

            row = max(debit_row, credit_row)

        if len(account.entries) > 1:
            worksheet.write_number(row, 2, account.debit, sub_balance_debit_format)
            worksheet.write_number(row, 3, account.credit, sub_balance_credit_format)
            row += 1

        if account.balance_type == BalanceType.DEBIT:
            worksheet.write_number(row, 2, account.balance, balance_debit_format)
            worksheet.write_number(row, 3, 0, balance_credit_format)
        if account.balance_type == BalanceType.CREDIT:
            worksheet.write_number(row, 2, 0, balance_debit_format)
            worksheet.write_number(row, 3, account.balance, balance_credit_format)
        row += 3

    worksheet.set_column(0, 0, 12, None)
    worksheet.set_column(5, 5, 12, None)

    # Cerrar el archivo
    workbook.close()


def generate_trial_balance_xlsx(trial_balance: TrialBalance, output_path):
    # Crear un nuevo archivo de Excel y una hoja de trabajo
    workbook = xlsxwriter.Workbook(output_path)
    worksheet = workbook.add_worksheet()

    # Establecer el formato para las celdas
    header_format = workbook.add_format({"bold": True, "align": "center"})
    cell_format = workbook.add_format({"align": "center"})
    money_format = workbook.add_format({"num_format": "#,##0.00"})

    # Encabezados de tabla
    headers = [
        "Código",
        "Cuenta",
        "Débito",
        "Crédito",
        "Saldo Deudor",
        "Saldo Acreedor",
    ]

    # Escribir encabezados
    for col, header in enumerate(headers):
        worksheet.write(0, col, header, header_format)

    # Datos de resumen de cuentas
    row = 1
    for account in trial_balance.accounts_summary:
        worksheet.write(row, 0, account.account_code, cell_format)
        worksheet.write(row, 1, account.account_name, cell_format)
        worksheet.write(row, 2, account.debit, money_format)
        worksheet.write(row, 3, account.credit, money_format)
        worksheet.write(row, 5, account.debit_balance, money_format)
        worksheet.write(row, 4, account.credit_balance, money_format)
        row += 1

    # Datos de resumen total
    if trial_balance.accounts_summary:
        worksheet.write(row, 2, trial_balance.total_debit, money_format)
        worksheet.write(row, 3, trial_balance.total_credit, money_format)
        worksheet.write(row, 4, trial_balance.total_debit_balance, money_format)
        worksheet.write(row, 5, trial_balance.total_credit_balance, money_format)

    # Ajustar automáticamente el ancho de las columnas al contenido
    for col, header in enumerate(headers):
        worksheet.set_column(col, col, len(header) + 2)

    worksheet.set_column(1, 1, 30)

    # Guardar el archivo de Excel
    workbook.close()


def generate_income_statement_xlsx(income_statement: IncomeStatement, output_path):
    # Generate workbook with output path
    workbook = xlsxwriter.Workbook(output_path)

    worksheet = workbook.add_worksheet()

    header_format = workbook.add_format({"bold": True})
    money_format = workbook.add_format({"num_format": "#,##0.00"})

    headers = ["Descripción", 1, 2, 3, 4]

    for col, header in enumerate(headers):
        worksheet.write(0, col, header, header_format)

    row = 1

    def add_row(row, label, col1=None, col2=None, col3=None, col4=None):
        worksheet.write_string(row, 0, label)
        if isinstance(col1, (int, float)):
            worksheet.write_number(row, 1, col1, money_format)
        if isinstance(col2, (int, float)):
            worksheet.write_number(row, 2, col2, money_format)
        if isinstance(col3, (int, float)):
            worksheet.write_number(row, 3, col3, money_format)
        if isinstance(col4, (int, float)):
            worksheet.write_number(row, 4, col4, money_format)
        return row + 1

    net_sales = income_statement.earnings_income.net_sales
    sales_cost = income_statement.earnings_income.sales_cost

    gross_margin = income_statement.earnings_income.gross_margin
    operating_expenses = income_statement.earnings_income.operating_expenses
    operating_income = income_statement.earnings_income.operating_income
    income_before_taxes = income_statement.earnings_income.income_before_taxes
    net_income = income_statement.earnings_income.net_income

    # Sales income section
    row = add_row(row, "Ingresos por Actividad")
    row = add_row(row, "Ingresos por Ventas:", col3=net_sales.sales)
    row = add_row(row, "Devoluciones de Ventas:", col2=net_sales.sales_returns)
    row = add_row(row, "Descuentos sobre Ventas:", col2=net_sales.sales_discounts)
    row = add_row(
        row,
        "Rebajas sobre Ventas:",
        col2=net_sales.sales_allowances,
        col3=sum(
            [
                net_sales.sales_returns,
                net_sales.sales_discounts,
                net_sales.sales_allowances,
            ],
            0,
        ),
    )
    row = add_row(row, "Ventas Netas:", col4=net_sales.net_sales)

    # Sales cost section
    row = add_row(row, "Costo de los Bienes Vendidos")
    if income_statement.accounting_method == AccountingMethod.ANALYTICAL:
        net_purchases = income_statement.earnings_income.net_purchases

        row = add_row(row, "Inventario Inicial:", col3=sales_cost.beginning_inventory)
        row = add_row(row, "Compras:", col1=net_purchases.purchases)
        row = add_row(row, "Gastos de Compras:", col1=net_purchases.purchasing_expenses)
        row = add_row(row, "Compras Totales:", col2=net_purchases.total_purchases)
        row = add_row(
            row, "Devoluciones de Compras:", col1=net_purchases.purchases_returns
        )
        row = add_row(
            row, "Descuentos sobre Compras:", col1=net_purchases.purchases_discounts
        )
        row = add_row(
            row,
            "Rebajas sobre Compras:",
            col1=net_purchases.purchases_allowances,
            col2=sum(
                [
                    net_purchases.purchases_returns,
                    net_purchases.purchases_discounts,
                    net_purchases.purchases_allowances,
                ],
                0,
            ),
        )
        row = add_row(row, "Compras Netas:", col3=net_purchases)
        row = add_row(
            row,
            "Total de Mercancias:",
            col3=sales_cost.purchases + net_purchases.net_purchases,
        )
        row = add_row(row, "Inventario Final:", col3=sales_cost.ending_inventory)
    row = add_row(row, "Costos de Ventas:", col4=sales_cost.sales_cost)
    row = add_row(row, "Utilidad Bruta:", col4=gross_margin.gross_profit)

    # Operation expenses Section
    row = add_row(row, "Gastos de Operación")
    row = add_row(row, "Gastos de Ventas:", col3=operating_expenses.sales_expenses)
    row = add_row(
        row, "Gastos Administrativos:", col3=operating_expenses.administrative_expenses
    )
    row = add_row(
        row, "Gastos Financieros:", col3=operating_expenses.financial_expenses
    )
    row = add_row(
        row, "Total de Gastos Operativos:", col4=operating_expenses.operating_expenses
    )
    row = add_row(row, "Utilidad de Operación:", col4=operating_income.operating_income)

    # Other expenses and incomes section
    row = add_row(row, "Otros Gastos e Ingresos")
    row = add_row(row, "Otros Gastos:", col3=income_before_taxes.other_expenses)
    row = add_row(row, "Otros Ingresos:", col3=income_before_taxes.other_products)
    row = add_row(
        row,
        "Perdida entre otros gastos e ingresos",
        col4=income_before_taxes.other_expenses - income_before_taxes.other_products,
    )
    row = add_row(row, "Resultado del Ejercicio")
    row = add_row(
        row, "Utilidad antes de Impuestos:", col4=net_income.income_before_taxes
    )
    row = add_row(
        row,
        f"Impuestos sobre la renta ({net_income.tax_rate * 100}%):",
        col4=net_income.income_tax_expense,
    )
    row = add_row(
        row, "Utilidad Neta después de Impuestos:", col4=net_income.net_income
    )

    worksheet.set_column(0, 0, 30)

    workbook.close()


def generate_balance_sheet_xlsx(balance_sheet: BalanceSheet, output_path):
    workbook = xlsxwriter.Workbook(output_path)
    worksheet = workbook.add_worksheet()

    header_format = workbook.add_format({"bold": True})
    footer_format = workbook.add_format({"bold": True, "align": "right"})
    money_format = workbook.add_format({"num_format": "#,##0.00"})

    row = 1
    for group_code, group in balance_sheet:
        worksheet.write(row, 0, group.group.account_name, header_format)
        row += 1
        for subgroup_code, subgroup in group.subgroups.items():
            row += 1
            worksheet.write_string(
                row, 0, subgroup.subgroup.account_name, header_format
            )
            row += 1

            for entity_code, entity in subgroup.entities.items():
                worksheet.write_string(row, 0, entity.account_name)
                worksheet.write_number(row, 1, entity.balance, money_format)
                row += 1

            worksheet.write_string(row, 0, "SUBTOTAL", footer_format)
            worksheet.write_number(row, 1, subgroup.subgroup.balance, money_format)
            row += 1
        row += 1
        worksheet.write_string(
            row, 0, f"TOTAL {group.group.account_name}", header_format
        )
        worksheet.write_number(row, 1, group.group.balance, money_format)

        row += 2

    worksheet.set_column(0, 0, 40)

    # Cerrar el archivo de Excel
    workbook.close()
