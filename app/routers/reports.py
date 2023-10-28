import uuid
from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.models.financial_statement import JournalBook, AccountCatalog, LedgerBook
from app.services.report_service import (
    generate_account_catalog_xlsx,
    generate_journal_book_xlsx,
    generate_ledger_book_xlsx,
)
from app.data.financial_statement_data import account_catalog_data

router = APIRouter()


@router.post("/generate_account_catalog_xlsx/")
async def generate_account_catalog_xlsx_router():
    # Generate a unique file name with an UUID
    unique_filename_path = f"app/temp/account_catalog_{uuid.uuid4()}.xlsx"

    # Genete the file XLSX in Server
    generate_account_catalog_xlsx(
        account_catalog=AccountCatalog(**account_catalog_data),
        output_path=unique_filename_path,
    )

    # Devuelve el archivo XLSX como respuesta
    return FileResponse(
        unique_filename_path,
        headers={"Content-Disposition": f"attachment; filename={unique_filename_path}"},
    )


@router.post("/generate_journal_book_xlsx/")
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


@router.post("/generate_ledger_book_xlsx/")
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
