import uuid
from fastapi import APIRouter
from fastapi.responses import FileResponse
from app.models.amortization import OutLoanAmortization
from app.models.financial_statement import (
    BalanceSheet,
    IncomeStatement,
    JournalBook,
    AccountCatalog,
    LedgerBook,
    TrialBalance,
)
from app.services.report_service import (
    generate_amortization_table_xlsx,
    generate_account_catalog_xlsx,
    generate_balance_sheet_xlsx,
    generate_income_statement_xlsx,
    generate_journal_book_xlsx,
    generate_ledger_book_xlsx,
    generate_trial_balance_xlsx,
)
from app.data.account_catalog_data import account_catalog_data_with_description

router = APIRouter()


@router.post("/generate_amortization_table_xlsx")
async def generate_amortization_table_xlsx_router(
    amortization_table: OutLoanAmortization,
):
    # Generate an unique filename path
    unique_filename_path = f"app/temp/amortization_table_{uuid.uuid4()}.xlsx"

    # Genete the file XLSX in Server
    generate_amortization_table_xlsx(
        amortization_table=amortization_table,
        output_path=unique_filename_path,
    )

    # Devuelve el archivo XLSX como respuesta
    return FileResponse(
        unique_filename_path,
        headers={"Content-Disposition": f"attachment; filename={unique_filename_path}"},
    )


@router.post("/generate_account_catalog_xlsx")
async def generate_account_catalog_xlsx_router():
    # Generate a unique file name with an UUID
    unique_filename_path = f"app/temp/account_catalog_{uuid.uuid4()}.xlsx"

    # Genete the file XLSX in Server
    generate_account_catalog_xlsx(
        account_catalog=AccountCatalog(**account_catalog_data_with_description),
        output_path=unique_filename_path,
    )

    # Devuelve el archivo XLSX como respuesta
    return FileResponse(
        unique_filename_path,
        headers={"Content-Disposition": f"attachment; filename={unique_filename_path}"},
    )


@router.post("/generate_journal_book_xlsx")
async def generate_journal_book_xlsx_router(journal_book: JournalBook):
    # Generate a unique file name with UUID
    unique_filename_path = f"app/temp/journal_book_{uuid.uuid4()}.xlsx"

    # Genete the file XLSX in Server
    generate_journal_book_xlsx(
        journal_book=journal_book,
        output_path=unique_filename_path,
    )

    # Return the XLSX file as response
    return FileResponse(
        unique_filename_path,
        headers={"Content-Disposition": f"attachment; filename={unique_filename_path}"},
    )


@router.post("/generate_ledger_book_xlsx")
async def generate_ledger_book_xlsx_router(ledger_book: LedgerBook):
    # Generate a unique file name with UUID
    unique_filename_path = f"app/temp/ledger_book{uuid.uuid4()}.xlsx"

    # Generate the file XLSX in Server
    generate_ledger_book_xlsx(ledger_book=ledger_book, output_path=unique_filename_path)

    # Return the XLSX file as response
    return FileResponse(
        unique_filename_path,
        headers={"Content-Disposition": f"attachment; filename={unique_filename_path}"},
    )


@router.post("/generate_trial_balance_xlsx")
async def generate_trial_balance_xlsx_router(trial_balance: TrialBalance):
    # Generate a unique file name with UUID
    unique_filename_path = f"app/temp/trial_balance_{uuid.uuid4()}.xlsx"

    # Generate the file XLSX in server
    generate_trial_balance_xlsx(trial_balance, output_path=unique_filename_path)

    # Return the XLSX file as response
    return FileResponse(
        unique_filename_path,
        headers={"Content-Disposition": f"attachment; filename={unique_filename_path}"},
    )


@router.post("/generate_income_statement_xlsx")
async def generate_income_statement_xlsx_router(income_statement: IncomeStatement):
    # Generate a unique file name with uuid
    unique_filename_path = f"app/temp/income_statement_{uuid.uuid4()}.xlsx"

    # Generate the XLSX file in server
    generate_income_statement_xlsx(income_statement, output_path=unique_filename_path)

    # Return the XLSX file as response
    return FileResponse(
        unique_filename_path,
        headers={"Content-Disposition": f"attachment; filename={unique_filename_path}"},
    )


@router.post("/generate_balance_sheet_xlsx")
async def generate_balance_sheet_xlsx_router(balance_sheet: BalanceSheet):
    # Generate a unique filename path
    unique_filename_path = f"app/temp/balance_sheet_{uuid.uuid4()}.xlsx"

    # Generate the XLSX file in server
    generate_balance_sheet_xlsx(balance_sheet, output_path=unique_filename_path)

    # Return the XLSX file as response
    return FileResponse(
        unique_filename_path,
        headers={"Content-Disposition": f"attachment; filename={unique_filename_path}"},
    )
