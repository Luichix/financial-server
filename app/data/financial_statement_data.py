from app.models.financial_statement import BalanceType, IncomeStatementAccountNames


account_catalog_data = {
    "accounts": [
        {
            "accountCode": "1",
            "accountName": "ACTIVO",
            "description": "",
        },
        {
            "accountCode": "1.01",
            "accountName": "ACTIVO CIRCULANTE",
            "description": "",
        },
        {
            "accountCode": "1.01.01",
            "accountName": "CAJA GENERAL",
            "description": "",
        },
        {
            "accountCode": "1.01.02",
            "accountName": "CAJA CHICA",
            "description": "",
        },
        {
            "accountCode": "1.01.03",
            "accountName": "BANCOS",
            "description": "",
        },
        {
            "accountCode": "1.01.04",
            "accountName": "INVENTARIOS",
            "description": "Inventario de Mercancias",
            "incomeStatementAccountName": IncomeStatementAccountNames.ENDING_INVENTORY,
        },
        {
            "accountCode": "1.01.05",
            "accountName": "CLIENTES",
            "description": "",
        },
        {
            "accountCode": "1.01.06",
            "accountName": "DOCUMENTOS POR COBRAR",
            "description": "",
        },
        {
            "accountCode": "1.01.07",
            "accountName": "DEUDORES DIVERSOS",
            "description": "",
        },
        {
            "accountCode": "1.01.08",
            "accountName": "FUNCIONARIOS Y EMPLEADOS",
            "description": "",
        },
        {
            "accountCode": "1.01.09",
            "accountName": "PAPELERIA Y UTILES",
            "description": "",
        },
        {
            "accountCode": "1.02",
            "accountName": "ACTIVO FIJO",
            "description": "",
        },
        {
            "accountCode": "1.02.01",
            "accountName": "TERRENO",
            "description": "",
        },
        {
            "accountCode": "1.02.02",
            "accountName": "EDIFICIO",
            "description": "",
        },
        {
            "accountCode": "1.02.03",
            "accountName": "MAQUINARIA Y EQUIPO",
            "description": "",
        },
        {
            "accountCode": "1.02.04",
            "accountName": "MOBILIARIO Y EQUIPO DE OFICINA",
            "description": "",
        },
        {
            "accountCode": "1.02.05",
            "accountName": "EQUIPO DE TRANSPORTE",
            "description": "",
        },
        {
            "accountCode": "1.02.06",
            "accountName": "EQUIPO DE ENTREGA Y REPARTO",
            "description": "",
        },
        {
            "accountCode": "2",
            "accountName": "PASIVO",
            "description": "",
        },
        {
            "accountCode": "2.01",
            "accountName": "PASIVO CIRCULANTE",
            "description": "",
        },
        {
            "accountCode": "2.01.01",
            "accountName": "PROVEEDORES",
            "description": "",
        },
        {
            "accountCode": "2.01.02",
            "accountName": "ACREEDORES DIVERSOS",
            "description": "",
        },
        {
            "accountCode": "2.01.03",
            "accountName": "DOCUMENTOS POR PAGAR",
            "description": "",
        },
        {
            "accountCode": "2.01.04",
            "accountName": "IMPUESTOS POR PAGAR",
            "description": "",
        },
        {
            "accountCode": "2.01.05",
            "accountName": "INTERESES POR PAGAR",
            "description": "",
        },
        {
            "accountCode": "2.01.06",
            "accountName": "SUELDOS ACUMULADOS POR PAGAR",
            "description": "",
        },
        {
            "accountCode": "2.02",
            "accountName": "PASIVO FIJO",
            "description": "",
        },
        {
            "accountCode": "2.02.01",
            "accountName": "DOCUMENTOS POR PAGAR A LARGO PLAZO",
            "description": "",
        },
        {
            "accountCode": "3",
            "accountName": "PATRIMONIO",
            "description": "",
        },
        {
            "accountCode": "3.01",
            "accountName": "CAPITAL SOCIAL",
            "description": "",
        },
        {
            "accountCode": "3.01.01",
            "accountName": "CAPITAL CONTABLE",
            "description": "",
        },
        {
            "accountCode": "3.01.02",
            "accountName": "UTILIDAD DEL EJERCICIO",
            "description": "",
        },
        {
            "accountCode": "3.01.03",
            "accountName": "PERDIDA DEL EJERCICIO",
            "description": "",
        },
        {
            "accountCode": "4",
            "accountName": "INGRESOS",
            "description": "",
        },
        {
            "accountCode": "4.01",
            "accountName": "INGRESOS POR VENTAS",
            "description": "",
        },
        {
            "accountCode": "4.01.01",
            "accountName": "VENTAS POR ACTIVIDAD",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.SALES,
        },
        {
            "accountCode": "4.01.02",
            "accountName": "DEVOLUCIONES SOBRE VENTAS",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.SALES_RETURNS,
        },
        {
            "accountCode": "4.01.03",
            "accountName": "DESCUENTOS SOBRE VENTAS",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.SALES_DISCOUNTS,
        },
        {
            "accountCode": "4.01.04",
            "accountName": "REBAJAS SOBRE VENTAS",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.SALES_ALLOWANCES,
        },
        {
            "accountCode": "4.02",
            "accountName": "OTROS INGRESOS",
            "description": "",
        },
        {
            "accountCode": "4.02.01",
            "accountName": "OTROS PRODUCTOS",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.OTHER_PRODUCTS,
        },
        {
            "accountCode": "5",
            "accountName": "EGRESOS",
            "description": "",
        },
        {
            "accountCode": "5.01",
            "accountName": "COMPRAS",
            "description": "",
        },
        {
            "accountCode": "5.01.01",
            "accountName": "COMPRAS DE MERCANCIAS",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.PURCHASES,
        },
        {
            "accountCode": "5.01.02",
            "accountName": "GASTOS DE COMPRAS",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.PURCHASING_EXPENSES,
        },
        {
            "accountCode": "5.01.03",
            "accountName": "DEVOLUCIONES SOBRE COMPRAS",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.PURCHASES_RETURNS,
        },
        {
            "accountCode": "5.01.04",
            "accountName": "DESCUENTOS SOBRE COMPRAS",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.PURCHASES_DISCOUNTS,
        },
        {
            "accountCode": "5.01.05",
            "accountName": "REBAJAS SOBRE COMPRAS",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.PURCHASES_ALLOWANCES,
        },
        {
            "accountCode": "5.02",
            "accountName": "COSTOS DE PRODUCCIÓN",
            "description": "",
        },
        {
            "accountCode": "5.02.01",
            "accountName": "COSTOS DE MATERIALES",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.DIRECT_MATERIAL,
        },
        {
            "accountCode": "5.02.02",
            "accountName": "COSTOS DE MANO DE OBRA",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.DIRECT_LABOR,
        },
        {
            "accountCode": "5.02.03",
            "accountName": "COSTOS INDIRECTOS DE FABRICACIÓN",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.FACTORY_OVERHEAD,
        },
        {
            "accountCode": "5.03",
            "accountName": "GASTOS OPERATIVOS",
            "description": "",
        },
        {
            "accountCode": "5.03.01",
            "accountName": "GASTOS DE ADMINISTRACIÓN",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.ADMINISTRATIVE_EXPENSES,
        },
        {
            "accountCode": "5.03.02",
            "accountName": "GASTOS DE VENTA",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.SALES_EXPENSES,
        },
        {
            "accountCode": "5.03.03",
            "accountName": "GASTOS FINANCIEROS",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.FINANCIAL_EXPENSES,
        },
        {
            "accountCode": "5.04",
            "accountName": "OTROS EGRESOS",
            "description": "",
        },
        {
            "accountCode": "5.04.01",
            "accountName": "OTROS GASTOS",
            "description": "",
            "incomeStatementAccountName": IncomeStatementAccountNames.OTHER_EXPENSES,
        },
    ]
}

journal_book_data = {
    "journalBookEntries": [
        {
            "entryNumber": 1,
            "date": "2023-10-10",
            "debit": 100,
            "credit": 0,
            "concept": "Ingreso de productos en inventario",
            "account": {
                "accountCode": "1.01.04",
                "accountName": "INVENTARIOS",
            },
        },
        {
            "entryNumber": 1,
            "date": "2023-10-10",
            "debit": 0,
            "credit": 100,
            "concept": "Pago de la compra de mercancia al contado",
            "account": {
                "accountCode": "1.01.01",
                "accountName": "CAJA GENERAL",
            },
        },
    ]
}

evaluated_journal_book_data = {
    "journalBookEntries": [
        {
            "entryNumber": 1,
            "date": "2023-10-10",
            "debit": 100,
            "credit": 0,
            "concept": "Ingreso de productos en inventario",
            "account": {
                "accountCode": "1.01.04",
                "accountName": "INVENTARIOS",
            },
            "unbalanced": False,
        },
        {
            "entryNumber": 1,
            "date": "2023-10-10",
            "debit": 0,
            "credit": 100,
            "concept": "Pago de la compra de mercancia al contado",
            "account": {
                "accountCode": "1.01.01",
                "accountName": "CAJA GENERAL",
            },
            "unbalanced": False,
        },
    ],
    "unbalanced": False,
    "unbalancedEntries": [],
}

ledger_book_data = {
    "ledgerBookEntries": [
        {
            "accountCode": "1.01.04",
            "accountName": "INVENTARIOS",
            "entries": [
                {
                    "entryNumber": 1,
                    "date": "2023-10-10",
                    "debit": 100,
                    "credit": 0,
                }
            ],
            "debit": 100,
            "credit": 0,
            "balance": 100.0,
            "balanceType": BalanceType.DEBIT,
        },
        {
            "accountCode": "1.01.01",
            "accountName": "CAJA GENERAL",
            "entries": [
                {
                    "entryNumber": 1,
                    "date": "2023-10-10",
                    "debit": 0,
                    "credit": 100,
                }
            ],
            "credit": 100,
            "debit": 0,
            "balance": 100.0,
            "balanceType": BalanceType.CREDIT,
        },
    ]
}

trial_balance_data = {
    "accountsSummary": [
        {
            "accountCode": "1.01.04",
            "accountName": "INVENTARIOS",
            "debit": 100,
            "credit": 0,
            "debitBalance": 100,
            "creditBalance": 0,
            "balance": 100,
        },
        {
            "accountCode": "1.01.01",
            "accountName": "CAJA GENERAL",
            "debit": 0,
            "credit": 100,
            "debitBalance": 0,
            "creditBalance": 100,
            "balance": 100,
        },
    ],
    "totalDebit": 100,
    "totalCredit": 100,
    "totalDebitBalance": 100,
    "totalCreditBalance": 100,
    "isBalanced": True,
}


income_statement_perpetual_data = {
    "accountingMethod": "perpetual",
    "earningsIncome": {
        "netSales": {
            "sales": 0.0,
            "salesReturns": 0.0,
            "salesDiscounts": 0.0,
            "salesAllowances": 0.0,
            "netSales": 0.0,
        },
        "salesCost": {
            "salesCost": -0.0,
        },
        "grossMargin": {"salesRevenue": 0.0, "salesCost": 0.0, "grossProfit": 0.0},
        "operatingExpenses": {
            "salesExpenses": 0.0,
            "administrativeExpenses": 0.0,
            "financialExpenses": 0.0,
            "operatingExpenses": 0.0,
        },
        "operatingIncome": {
            "grossMargin": 0.0,
            "operatingExpenses": 0.0,
            "operatingIncome": 0.0,
        },
        "incomeBeforeTaxes": {
            "operatingIncome": 0.0,
            "otherExpenses": 0.0,
            "otherProducts": 0.0,
            "incomeBeforeTaxes": 0.0,
        },
        "netIncome": {
            "incomeBeforeTaxes": 0.0,
            "taxRate": 0.3,
            "incomeTaxExpense": 0.0,
            "netIncome": 0.0,
        },
    },
}

income_statement_analytical_data = {
    "accountingMethod": "analytical",
    "earningsIncome": {
        "netSales": {
            "sales": 0.0,
            "salesReturns": 0.0,
            "salesDiscounts": 0.0,
            "salesAllowances": 0.0,
            "netSales": 0.0,
        },
        "netPurchases": {
            "purchases": 0.0,
            "purchasingExpenses": 0.0,
            "totalPurchases": 0.0,
            "purchasesReturns": 0.0,
            "purchasesDiscounts": 0.0,
            "purchasesAllowances": 0.0,
            "netPurchases": 0.0,
        },
        "salesCost": {
            "beginningInventory": 0.0,
            "purchases": 0.0,
            "endingInventory": 100.0,
            "salesCost": -100.0,
        },
        "grossMargin": {
            "salesRevenue": 0.0,
            "salesCost": -100.0,
            "grossProfit": -100.0,
        },
        "operatingExpenses": {
            "salesExpenses": 0.0,
            "administrativeExpenses": 0.0,
            "financialExpenses": 0.0,
            "operatingExpenses": 0.0,
        },
        "operatingIncome": {
            "grossMargin": 100.0,
            "operatingExpenses": 0.0,
            "operatingIncome": 0.0,
        },
        "incomeBeforeTaxes": {
            "operatingIncome": 100.0,
            "otherExpenses": 0.0,
            "otherProducts": 0.0,
            "incomeBeforeTaxes": 100.0,
        },
        "netIncome": {
            "incomeBeforeTaxes": 100.0,
            "taxRate": 0.3,
            "incomeTaxExpense": 30.0,
            "netIncome": 70.0,
        },
    },
}


balance_sheet_data = {
    "assets": {
        "group": {
            "accountCode": "1",
            "accountName": "ACTIVO",
            "isGroup": True,
            "isSubgroup": False,
            "isEntity": False,
            "balance": 200,
        },
        "subgroups": {
            "1.01": {
                "subgroup": {
                    "accountCode": "1.01",
                    "accountName": "ACTIVO CIRCULANTE",
                    "isGroup": False,
                    "isSubgroup": True,
                    "isEntity": False,
                    "balance": 200,
                },
                "entities": {
                    "1.01.01": {
                        "accountCode": "1.01.01",
                        "accountName": "CAJA GENERAL",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 100,
                    },
                    "1.01.02": {
                        "accountCode": "1.01.02",
                        "accountName": "CAJA CHICA",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "1.01.03": {
                        "accountCode": "1.01.03",
                        "accountName": "BANCOS",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "1.01.04": {
                        "accountCode": "1.01.04",
                        "accountName": "INVENTARIOS",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 100,
                    },
                    "1.01.05": {
                        "accountCode": "1.01.05",
                        "accountName": "CLIENTES",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "1.01.06": {
                        "accountCode": "1.01.06",
                        "accountName": "DOCUMENTOS POR COBRAR",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "1.01.07": {
                        "accountCode": "1.01.07",
                        "accountName": "DEUDORES DIVERSOS",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "1.01.08": {
                        "accountCode": "1.01.08",
                        "accountName": "FUNCIONARIOS Y EMPLEADOS",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "1.01.09": {
                        "accountCode": "1.01.09",
                        "accountName": "PAPELERIA Y UTILES",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                },
            },
            "1.02": {
                "subgroup": {
                    "accountCode": "1.02",
                    "accountName": "ACTIVO FIJO",
                    "isGroup": False,
                    "isSubgroup": True,
                    "isEntity": False,
                    "balance": 0,
                },
                "entities": {
                    "1.02.01": {
                        "accountCode": "1.02.01",
                        "accountName": "TERRENO",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "1.02.02": {
                        "accountCode": "1.02.02",
                        "accountName": "EDIFICIO",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "1.02.03": {
                        "accountCode": "1.02.03",
                        "accountName": "MAQUINARIA Y EQUIPO",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "1.02.04": {
                        "accountCode": "1.02.04",
                        "accountName": "MOBILIARIO Y EQUIPO DE OFICINA",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "1.02.05": {
                        "accountCode": "1.02.05",
                        "accountName": "EQUIPO DE TRANSPORTE",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "1.02.06": {
                        "accountCode": "1.02.06",
                        "accountName": "EQUIPO DE ENTREGA Y REPARTO",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                },
            },
        },
    },
    "liability": {
        "group": {
            "accountCode": "2",
            "accountName": "PASIVO",
            "isGroup": True,
            "isSubgroup": False,
            "isEntity": False,
            "balance": 0,
        },
        "subgroups": {
            "2.01": {
                "subgroup": {
                    "accountCode": "2.01",
                    "accountName": "PASIVO CIRCULANTE",
                    "isGroup": False,
                    "isSubgroup": True,
                    "isEntity": False,
                    "balance": 0,
                },
                "entities": {
                    "2.01.01": {
                        "accountCode": "2.01.01",
                        "accountName": "PROVEEDORES",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "2.01.02": {
                        "accountCode": "2.01.02",
                        "accountName": "ACREEDORES DIVERSOS",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "2.01.03": {
                        "accountCode": "2.01.03",
                        "accountName": "DOCUMENTOS POR PAGAR",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "2.01.04": {
                        "accountCode": "2.01.04",
                        "accountName": "IMPUESTOS POR PAGAR",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "2.01.05": {
                        "accountCode": "2.01.05",
                        "accountName": "INTERESES POR PAGAR",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "2.01.06": {
                        "accountCode": "2.01.06",
                        "accountName": "SUELDOS ACUMULADOS POR PAGAR",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                },
            },
            "2.02": {
                "subgroup": {
                    "accountCode": "2.02",
                    "accountName": "PASIVO FIJO",
                    "isGroup": False,
                    "isSubgroup": True,
                    "isEntity": False,
                    "balance": 0,
                },
                "entities": {
                    "2.02.01": {
                        "accountCode": "2.02.01",
                        "accountName": "DOCUMENTOS POR PAGAR A LARGO PLAZO",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                },
            },
        },
    },
    "equity": {
        "group": {
            "accountCode": "3",
            "accountName": "PATRIMONIO",
            "isGroup": True,
            "isSubgroup": False,
            "isEntity": False,
            "balance": 0,
        },
        "subgroups": {
            "3.01": {
                "subgroup": {
                    "accountCode": "3.01",
                    "accountName": "CAPITAL SOCIAL",
                    "isGroup": False,
                    "isSubgroup": True,
                    "isEntity": False,
                    "balance": 0,
                },
                "entities": {
                    "3.01.01": {
                        "accountCode": "3.01.01",
                        "accountName": "CAPITAL CONTABLE",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "3.01.02": {
                        "accountCode": "3.01.02",
                        "accountName": "UTILIDAD DEL EJERCICIO",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                    "3.01.03": {
                        "accountCode": "3.01.03",
                        "accountName": "PERDIDA DEL EJERCICIO",
                        "isGroup": False,
                        "isSubgroup": False,
                        "isEntity": True,
                        "balance": 0,
                    },
                },
            }
        },
    },
}
