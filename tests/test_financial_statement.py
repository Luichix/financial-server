from app.models.financial_statement import (
    AccountCatalog,
    BalanceType,
    IncomeStatement,
    JournalBook,
    LedgerBook,
    TrialBalance,
)
from app.services.financial_statement_service import (
    create_income_statement,
    create_ledger_book,
    create_trial_balance,
    evaluate_journal_book,
)


class TestFinancialStatement:
    tax_rate = 0.3
    account_catalog_data = [
        {
            "account_code": "1",
            "account_name": "ACTIVO",
            "description": "",
        },
        {
            "account_code": "1.01",
            "account_name": "ACTIVO CIRCULANTE",
            "description": "",
        },
        {
            "account_code": "1.01.01",
            "account_name": "CAJA GENERAL",
            "description": "",
        },
        {
            "account_code": "1.01.02",
            "account_name": "CAJA CHICA",
            "description": "",
        },
        {
            "account_code": "1.01.03",
            "account_name": "BANCOS",
            "description": "",
        },
        {
            "account_code": "1.01.04",
            "account_name": "INVENTARIOS",
            "description": "",
        },
        {
            "account_code": "1.01.05",
            "account_name": "CLIENTES",
            "description": "",
        },
        {
            "account_code": "1.01.06",
            "account_name": "DOCUMENTOS POR COBRAR",
            "description": "",
        },
        {
            "account_code": "1.01.07",
            "account_name": "DEUDORES DIVERSOS",
            "description": "",
        },
        {
            "account_code": "1.01.08",
            "account_name": "FUNCIONARIOS Y EMPLEADOS",
            "description": "",
        },
        {
            "account_code": "1.01.09",
            "account_name": "PAPELERIA Y UTILES",
            "description": "",
        },
        {
            "account_code": "1.02",
            "account_name": "ACTIVO FIJO",
            "description": "",
        },
        {
            "account_code": "1.02.01",
            "account_name": "TERRENO",
            "description": "",
        },
        {
            "account_code": "1.02.02",
            "account_name": "EDIFICIO",
            "description": "",
        },
        {
            "account_code": "1.02.03",
            "account_name": "MAQUINARIA Y EQUIPO",
            "description": "",
        },
        {
            "account_code": "1.02.04",
            "account_name": "MOBILIARIO Y EQUIPO DE OFICINA",
            "description": "",
        },
        {
            "account_code": "1.02.05",
            "account_name": "EQUIPO DE TRANSPORTE",
            "description": "",
        },
        {
            "account_code": "1.02.06",
            "account_name": "EQUIPO DE ENTREGA Y REPARTO",
            "description": "",
        },
        {
            "account_code": "2",
            "account_name": "PASIVO",
            "description": "",
        },
        {
            "account_code": "2.01",
            "account_name": "PASIVO CIRCULANTE",
            "description": "",
        },
        {
            "account_code": "2.01.01",
            "account_name": "PROVEEDORES",
            "description": "",
        },
        {
            "account_code": "2.01.02",
            "account_name": "ACREEDORES DIVERSOS",
            "description": "",
        },
        {
            "account_code": "2.01.03",
            "account_name": "DOCUMENTOS POR PAGAR",
            "description": "",
        },
        {
            "account_code": "2.01.04",
            "account_name": "IMPUESTOS POR PAGAR",
            "description": "",
        },
        {
            "account_code": "2.01.05",
            "account_name": "INTERESES POR PAGAR",
            "description": "",
        },
        {
            "account_code": "2.01.06",
            "account_name": "SUELDOS ACUMULADOS POR PAGAR",
            "description": "",
        },
        {
            "account_code": "2.02",
            "account_name": "PASIVO FIJO",
            "description": "",
        },
        {
            "account_code": "2.02.01",
            "account_name": "DOCUMENTOS POR PAGAR A LARGO PLAZO",
            "description": "",
        },
        {
            "account_code": "3",
            "account_name": "PATRIMONIO",
            "description": "",
        },
        {
            "account_code": "3.01",
            "account_name": "CAPITAL SOCIAL",
            "description": "",
        },
        {
            "account_code": "3.01.01",
            "account_name": "CAPITAL CONTABLE",
            "description": "",
        },
        {
            "account_code": "3.01.02",
            "account_name": "UTILIDAD DEL EJERCICIO",
            "description": "",
        },
        {
            "account_code": "3.01.03",
            "account_name": "PERDIDA DEL EJERCICIO",
            "description": "",
        },
        {
            "account_code": "4",
            "account_name": "INGRESOS",
            "description": "",
        },
        {
            "account_code": "4.01",
            "account_name": "INGRESOS POR VENTAS",
            "description": "",
            "belongs_to_income_statement": True,
            "order_in_income_statement": 1,
        },
        {
            "account_code": "4.01.01",
            "account_name": "VENTAS POR ACTIVIDAD",
            "description": "",
            "belongs_to_income_statement": True,
        },
        {
            "account_code": "5",
            "account_name": "EGRESOS",
            "description": "",
        },
        {
            "account_code": "5.01",
            "account_name": "COSTOS DE PRODUCCIÓN",
            "description": "",
            "belongs_to_income_statement": True,
            "order_in_income_statement": 1,
        },
        {
            "account_code": "5.01.01",
            "account_name": "COSTOS DE MATERIALES",
            "description": "",
            "belongs_to_income_statement": True,
        },
        {
            "account_code": "5.01.02",
            "account_name": "COSTOS DE MANO DE OBRA",
            "description": "",
            "belongs_to_income_statement": True,
        },
        {
            "account_code": "5.01.03",
            "account_name": "COSTOS INDIRECTOS DE FABRICACIÓN",
            "description": "",
            "belongs_to_income_statement": True,
        },
        {
            "account_code": "5.02",
            "account_name": "GASTOS OPERATIVOS",
            "description": "",
            "belongs_to_income_statement": True,
            "order_in_income_statement": 1,
        },
        {
            "account_code": "5.02.01",
            "account_name": "GASTOS DE ADMINISTRACIÓN",
            "description": "",
            "belongs_to_income_statement": True,
        },
        {
            "account_code": "5.02.02",
            "account_name": "GASTOS DE VENTA",
            "description": "",
            "belongs_to_income_statement": True,
        },
        {
            "account_code": "5.02.03",
            "account_name": "GASTOS FINANCIEROS",
            "description": "",
            "belongs_to_income_statement": True,
        },
    ]

    journal_book_data = {
        "journal_book_entries": [
            {
                "entry_number": 1,
                "date": "2023-10-10",
                "debit": 100,
                "credit": 0,
                "concept": "Compra de productos en inventario",
                "account": {
                    "account_code": "1.01.01",
                    "account_name": "Inventario de Mercancias",
                    "account_group": "1",
                },
            },
            {
                "entry_number": 1,
                "date": "2023-10-10",
                "debit": 0,
                "credit": 100,
                "concept": "Pago de la compra de mercancia al contado",
                "account": {
                    "account_code": "1.02.01",
                    "account_name": "Caja",
                    "account_group": "1",
                },
            },
        ]
    }

    evaluated_journal_book_data = {
        "journal_book_entries": [
            {
                "entry_number": 1,
                "date": "2023-10-10",
                "debit": 100,
                "credit": 0,
                "concept": "Compra de productos en inventario",
                "account": {
                    "account_code": "1.01.01",
                    "account_name": "Inventario de Mercancias",
                    "account_group": "1",
                },
                "unbalanced": False,
            },
            {
                "entry_number": 1,
                "date": "2023-10-10",
                "debit": 0,
                "credit": 100,
                "concept": "Pago de la compra de mercancia al contado",
                "account": {
                    "account_code": "1.02.01",
                    "account_name": "Caja",
                    "account_group": "1",
                },
                "unbalanced": False,
            },
        ],
        "unbalanced": False,
        "unbalanced_entries": [],
    }

    ledger_book_data = {
        "ledger_book_entries": [
            {
                "account_code": "1.01.01",
                "account_name": "Inventario de Mercancias",
                "account_group": "1",
                "entries": [
                    {
                        "entry_number": 1,
                        "date": "2023-10-10",
                        "debit": 100,
                        "credit": 0,
                    }
                ],
                "debit": 100,
                "credit": 0,
                "balance": 100.0,
                "balance_type": BalanceType.DEBIT,
            },
            {
                "account_code": "1.02.01",
                "account_name": "Caja",
                "account_group": "1",
                "entries": [
                    {
                        "entry_number": 1,
                        "date": "2023-10-10",
                        "debit": 0,
                        "credit": 100,
                    }
                ],
                "credit": 100,
                "debit": 0,
                "balance": 100.0,
                "balance_type": BalanceType.CREDIT,
            },
        ]
    }

    trial_balance_data = {
        "accounts_summary": [
            {
                "account_code": "1.01.01",
                "account_name": "Inventario de Mercancias",
                "account_group": "1",
                "debit": 100,
                "credit": 0,
                "debit_balance": 100,
                "credit_balance": 0,
                "balance": 100,
            },
            {
                "account_code": "1.02.01",
                "account_name": "Caja",
                "account_group": "1",
                "debit": 0,
                "credit": 100,
                "debit_balance": 0,
                "credit_balance": 100,
                "balance": 100,
            },
        ],
        "total_debit": 100,
        "total_credit": 100,
        "total_debit_balance": 100,
        "total_credit_balance": 100,
        "is_balanced": True,
    }

    income_statement_data = [
        ["INGRESOS POR VENTAS", None, 0.0, None, None],
        ["VENTAS POR ACTIVIDAD", 0.0, None, None, None],
        ["COSTOS DE PRODUCCIÓN", None, 0.0, None, None],
        ["COSTOS DE MATERIALES", 0.0, None, None, None],
        ["COSTOS DE MANO DE OBRA", 0.0, None, None, None],
        ["COSTOS INDIRECTOS DE FABRICACIÓN", 0.0, None, None, None],
        ["GASTOS OPERATIVOS", None, 0.0, None, None],
        ["GASTOS DE ADMINISTRACIÓN", 0.0, None, None, None],
        ["GASTOS DE VENTA", 0.0, None, None, None],
        ["GASTOS FINANCIEROS", 0.0, None, None, None],
        ["UTILIDAD ANTES DE IMPUESTOS", None, 0, None, None],
        ["IMPUESTOS", None, 0.0, None, None],
        ["UTILIDAD O PERDIDA DEL EJERCICIO", None, 0.0, None, None],
    ]

    account_catalog_instance = AccountCatalog(accounts=account_catalog_data)

    journal_book_instance = JournalBook(**journal_book_data)

    evaluated_journal_book_instance = JournalBook(**evaluated_journal_book_data)

    ledger_book_instance = LedgerBook(**ledger_book_data)

    trial_balance_instance = TrialBalance(**trial_balance_data)

    income_statement_instance = IncomeStatement(entries=income_statement_data)

    def test_evaluated_journal_book(self):
        assert (
            evaluate_journal_book(self.journal_book_instance)
            == self.evaluated_journal_book_instance
        )

    def test_create_ledger_book(self):
        assert (
            create_ledger_book(self.evaluated_journal_book_instance)
            == self.ledger_book_instance
        )

    def test_create_trial_balance(self):
        assert (
            create_trial_balance(self.ledger_book_instance)
            == self.trial_balance_instance
        )

    def test_create_income_statement(self):
        assert (
            create_income_statement(
                self.trial_balance_instance,
                self.account_catalog_instance,
                self.tax_rate,
            )
            == self.income_statement_instance
        )
