from app.models.financial_statement import IncomeStatementAccountNames

account_catalog_data_with_description = {
    "accounts": [
        {
            "accountCode": "1",
            "accountName": "ACTIVO",
            "description": "Representa todos los bienes y derechos de la empresa, incluyendo tanto los activos circulantes como no circulantes.",
        },
        {
            "accountCode": "1.01",
            "accountName": "ACTIVO CIRCULANTE",
            "description": "Incluye los activos líquidos o convertibles en efectivo dentro de un año, como efectivo, cuentas por cobrar e inventarios.",
        },
        {
            "accountCode": "1.01.01",
            "accountName": "CAJA GENERAL",
            "description": "Refleja los fondos disponibles en efectivo en la empresa, utilizados para transacciones y pagos diarios.",
        },
        {
            "accountCode": "1.01.02",
            "accountName": "CAJA CHICA",
            "description": "Representa un fondo menor de efectivo destinado a gastos menores y pagos inmediatos en la empresa.",
        },
        {
            "accountCode": "1.01.03",
            "accountName": "BANCOS",
            "description": "Cuenta que registra los saldos en cuentas bancarias propiedad de la empresa, incluyendo cuentas corrientes y de ahorros.",
        },
        {
            "accountCode": "1.01.04",
            "accountName": "INVENTARIOS",
            "description": "Registra el valor de las mercancías y materiales disponibles para la venta o producción en la empresa.",
            "incomeStatementAccountName": IncomeStatementAccountNames.ENDING_INVENTORY,
        },
        {
            "accountCode": "1.01.05",
            "accountName": "CLIENTES",
            "description": "Representa el monto total adeudado por los clientes a la empresa, usualmente por ventas de bienes o servicios a crédito.",
        },
        {
            "accountCode": "1.01.06",
            "accountName": "DOCUMENTOS POR COBRAR",
            "description": "Incluye deudas formalizadas mediante documentos, como letras de cambio o pagarés, que la empresa tiene derecho a cobrar.",
        },
        {
            "accountCode": "1.01.07",
            "accountName": "DEUDORES DIVERSOS",
            "description": "Cuenta para registrar otros montos adeudados a la empresa, no clasificados en otras categorías de cuentas por cobrar.",
        },
        {
            "accountCode": "1.01.08",
            "accountName": "FUNCIONARIOS Y EMPLEADOS",
            "description": "Registra los anticipos y préstamos otorgados por la empresa a sus funcionarios y empleados.",
        },
        {
            "accountCode": "1.01.09",
            "accountName": "PAPELERIA Y UTILES",
            "description": "Representa el costo de materiales de oficina y útiles consumidos o disponibles para uso en las operaciones de la empresa.",
        },
        {
            "accountCode": "1.02",
            "accountName": "ACTIVO FIJO",
            "description": "Incluye bienes de larga duración que la empresa utiliza para su operación y no están destinados a la venta, como terrenos, edificios y maquinaria.",
        },
        {
            "accountCode": "1.02.01",
            "accountName": "TERRENO",
            "description": "Registra el valor de los terrenos propiedad de la empresa. No está sujeto a depreciación.",
        },
        {
            "accountCode": "1.02.02",
            "accountName": "EDIFICIO",
            "description": "Representa el valor de los edificios propiedad de la empresa, incluyendo oficinas y plantas industriales. Sujeto a depreciación.",
        },
        {
            "accountCode": "1.02.03",
            "accountName": "MAQUINARIA Y EQUIPO",
            "description": "Incluye el valor de la maquinaria y equipo especializado utilizado en la producción o prestación de servicios de la empresa.",
        },
        {
            "accountCode": "1.02.04",
            "accountName": "MOBILIARIO Y EQUIPO DE OFICINA",
            "description": "Registra el valor de mobiliario y equipos utilizados en la oficina, como escritorios, sillas y computadoras.",
        },
        {
            "accountCode": "1.02.05",
            "accountName": "EQUIPO DE TRANSPORTE",
            "description": "Cuenta para el valor de los vehículos de transporte de la empresa, como camiones y autos para actividades comerciales.",
        },
        {
            "accountCode": "1.02.06",
            "accountName": "EQUIPO DE ENTREGA Y REPARTO",
            "description": "Representa el valor de equipos y vehículos específicamente utilizados para la entrega y reparto de productos de la empresa.",
        },
        {
            "accountCode": "2",
            "accountName": "PASIVO",
            "description": "Agrupa las obligaciones financieras y deudas de la empresa frente a terceros, incluyendo tanto pasivos circulantes como no circulantes.",
        },
        {
            "accountCode": "2.01",
            "accountName": "PASIVO CIRCULANTE",
            "description": "Representa las deudas y obligaciones a corto plazo que deben ser pagadas dentro del año fiscal, como cuentas por pagar y préstamos a corto plazo.",
        },
        {
            "accountCode": "2.01.01",
            "accountName": "PROVEEDORES",
            "description": "Refleja el monto adeudado a proveedores por bienes o servicios adquiridos en crédito y aún no pagados.",
        },
        {
            "accountCode": "2.01.02",
            "accountName": "ACREEDORES DIVERSOS",
            "description": "Cuenta para registrar deudas diversas no clasificadas en otras cuentas, como obligaciones con terceros distintos a proveedores.",
        },
        {
            "accountCode": "2.01.03",
            "accountName": "DOCUMENTOS POR PAGAR",
            "description": "Incluye obligaciones formalizadas mediante documentos, como letras de cambio o pagarés, que la empresa debe pagar.",
        },
        {
            "accountCode": "2.01.04",
            "accountName": "IMPUESTOS POR PAGAR",
            "description": "Registra los impuestos acumulados y pendientes de pago a las autoridades fiscales.",
        },
        {
            "accountCode": "2.01.05",
            "accountName": "INTERESES POR PAGAR",
            "description": "Representa los intereses acumulados y aún no pagados sobre préstamos y otras formas de deuda.",
        },
        {
            "accountCode": "2.01.06",
            "accountName": "SUELDOS ACUMULADOS POR PAGAR",
            "description": "Cuenta para los salarios y sueldos ganados por los empleados pero aún no pagados por la empresa.",
        },
        {
            "accountCode": "2.02",
            "accountName": "PASIVO FIJO",
            "description": "Incluye deudas y obligaciones de la empresa a largo plazo, es decir, aquellas cuyo vencimiento supera el año fiscal actual.",
        },
        {
            "accountCode": "2.02.01",
            "accountName": "DOCUMENTOS POR PAGAR A LARGO PLAZO",
            "description": "Registra deudas formalizadas a través de documentos que la empresa debe pagar en un plazo mayor a un año.",
        },
        {
            "accountCode": "3",
            "accountName": "PATRIMONIO",
            "description": "Representa los derechos de los propietarios sobre los activos netos de la empresa, después de deducir todos sus pasivos.",
        },
        {
            "accountCode": "3.01",
            "accountName": "CAPITAL SOCIAL",
            "description": "Refleja el valor nominal de las acciones emitidas por la empresa, representando la inversión inicial de los accionistas.",
        },
        {
            "accountCode": "3.01.01",
            "accountName": "CAPITAL CONTABLE",
            "description": "Representa el valor total del capital aportado por los accionistas, más las utilidades retenidas y menos las pérdidas acumuladas.",
        },
        {
            "accountCode": "3.01.02",
            "accountName": "UTILIDAD DEL EJERCICIO",
            "description": "Registra el beneficio neto obtenido por la empresa durante el ejercicio fiscal actual, después de deducir todos los gastos.",
        },
        {
            "accountCode": "3.01.03",
            "accountName": "PERDIDA DEL EJERCICIO",
            "description": "Refleja las pérdidas netas sufridas por la empresa durante el ejercicio fiscal actual, después de considerar todos los ingresos y gastos.",
        },
        {
            "accountCode": "4",
            "accountName": "INGRESOS",
            "description": "Agrupa todos los ingresos generados por la empresa, tanto por sus operaciones principales como por actividades secundarias.",
        },
        {
            "accountCode": "4.01",
            "accountName": "INGRESOS POR VENTAS",
            "description": "Registra los ingresos obtenidos de las ventas principales de bienes o servicios de la empresa.",
        },
        {
            "accountCode": "4.01.01",
            "accountName": "VENTAS POR ACTIVIDAD",
            "description": "Representa los ingresos específicos generados por las distintas actividades comerciales o servicios ofrecidos por la empresa.",
            "incomeStatementAccountName": IncomeStatementAccountNames.SALES,
        },
        {
            "accountCode": "4.01.02",
            "accountName": "DEVOLUCIONES SOBRE VENTAS",
            "description": "Cuenta para registrar el valor de las ventas que fueron devueltas por los clientes.",
            "incomeStatementAccountName": IncomeStatementAccountNames.SALES_RETURNS,
        },
        {
            "accountCode": "4.01.03",
            "accountName": "DESCUENTOS SOBRE VENTAS",
            "description": "Refleja los descuentos concedidos a clientes sobre las ventas originales, reduciendo así los ingresos brutos.",
            "incomeStatementAccountName": IncomeStatementAccountNames.SALES_DISCOUNTS,
        },
        {
            "accountCode": "4.01.04",
            "accountName": "REBAJAS SOBRE VENTAS",
            "description": "Registra las rebajas concedidas en el precio de venta de bienes o servicios, distintas de los descuentos habituales.",
            "incomeStatementAccountName": IncomeStatementAccountNames.SALES_ALLOWANCES,
        },
        {
            "accountCode": "4.02",
            "accountName": "OTROS INGRESOS",
            "description": "Incluye ingresos que no provienen de las ventas principales de la empresa, como intereses, dividendos o ingresos por alquileres.",
        },
        {
            "accountCode": "4.02.01",
            "accountName": "OTROS PRODUCTOS",
            "description": "Registra ingresos provenientes de fuentes distintas a las ventas, como ganancias por inversiones o actividades secundarias.",
            "incomeStatementAccountName": IncomeStatementAccountNames.OTHER_PRODUCTS,
        },
        {
            "accountCode": "5",
            "accountName": "EGRESOS",
            "description": "Incluye todos los gastos y desembolsos realizados por la empresa, tanto en sus operaciones regulares como en actividades secundarias.",
        },
        {
            "accountCode": "5.01",
            "accountName": "COMPRAS",
            "description": "Registra el total de adquisiciones de mercancías o materias primas realizadas por la empresa para su venta o producción.",
        },
        {
            "accountCode": "5.01.01",
            "accountName": "COMPRAS DE MERCANCIAS",
            "description": "Representa el gasto en la adquisición de bienes destinados a la venta, sin incluir los costos adicionales como transporte o almacenamiento.",
            "incomeStatementAccountName": IncomeStatementAccountNames.PURCHASES,
        },
        {
            "accountCode": "5.01.02",
            "accountName": "GASTOS DE COMPRAS",
            "description": "Incluye todos los costos asociados a la adquisición de bienes, como transporte, almacenaje y manejo de inventario.",
            "incomeStatementAccountName": IncomeStatementAccountNames.PURCHASING_EXPENSES,
        },
        {
            "accountCode": "5.01.03",
            "accountName": "DEVOLUCIONES SOBRE COMPRAS",
            "description": "Cuenta para registrar el valor de las compras que fueron devueltas a los proveedores.",
            "incomeStatementAccountName": IncomeStatementAccountNames.PURCHASES_RETURNS,
        },
        {
            "accountCode": "5.01.04",
            "accountName": "DESCUENTOS SOBRE COMPRAS",
            "description": "Refleja los descuentos obtenidos en las compras, lo cual reduce el costo de adquisición de los bienes.",
            "incomeStatementAccountName": IncomeStatementAccountNames.PURCHASES_DISCOUNTS,
        },
        {
            "accountCode": "5.01.05",
            "accountName": "REBAJAS SOBRE COMPRAS",
            "description": "Registra las rebajas en el precio de compra de bienes o servicios, distintas de los descuentos habituales.",
            "incomeStatementAccountName": IncomeStatementAccountNames.PURCHASES_ALLOWANCES,
        },
        {
            "accountCode": "5.02",
            "accountName": "COSTOS DE PRODUCCIÓN",
            "description": "Incluye todos los costos directamente relacionados con la fabricación de productos, como materiales, mano de obra y costos indirectos.",
        },
        {
            "accountCode": "5.02.01",
            "accountName": "COSTOS DE MATERIALES",
            "description": "Registra el costo de los materiales directos utilizados en la fabricación de los productos.",
            "incomeStatementAccountName": IncomeStatementAccountNames.DIRECT_MATERIAL,
        },
        {
            "accountCode": "5.02.02",
            "accountName": "COSTOS DE MANO DE OBRA",
            "description": "Representa los costos asociados a la mano de obra directa empleada en la producción de bienes.",
            "incomeStatementAccountName": IncomeStatementAccountNames.DIRECT_LABOR,
        },
        {
            "accountCode": "5.02.03",
            "accountName": "COSTOS INDIRECTOS DE FABRICACIÓN",
            "description": "Incluye los costos no directamente asignables a un producto específico, como mantenimiento de fábrica y supervisión.",
            "incomeStatementAccountName": IncomeStatementAccountNames.FACTORY_OVERHEAD,
        },
        {
            "accountCode": "5.03",
            "accountName": "GASTOS OPERATIVOS",
            "description": "Agrupa los gastos necesarios para la administración y venta de los productos o servicios, así como otros costos de operación.",
        },
        {
            "accountCode": "5.03.01",
            "accountName": "GASTOS DE ADMINISTRACIÓN",
            "description": "Cuenta para los gastos relacionados con la gestión y administración general de la empresa.",
            "incomeStatementAccountName": IncomeStatementAccountNames.ADMINISTRATIVE_EXPENSES,
        },
        {
            "accountCode": "5.03.02",
            "accountName": "GASTOS DE VENTA",
            "description": "Registra los gastos relacionados con la comercialización y venta de los productos o servicios.",
            "incomeStatementAccountName": IncomeStatementAccountNames.SALES_EXPENSES,
        },
        {
            "accountCode": "5.03.03",
            "accountName": "GASTOS FINANCIEROS",
            "description": "Incluye costos asociados a financiamientos, como intereses de préstamos y otras cargas financieras.",
            "incomeStatementAccountName": IncomeStatementAccountNames.FINANCIAL_EXPENSES,
        },
        {
            "accountCode": "5.04",
            "accountName": "OTROS EGRESOS",
            "description": "Agrupa gastos no clasificados en las categorías anteriores, como pérdidas por cambios de moneda o gastos extraordinarios.",
        },
        {
            "accountCode": "5.04.01",
            "accountName": "OTROS GASTOS",
            "description": "Representa gastos diversos que no están directamente relacionados con la producción o venta de bienes y servicios.",
            "incomeStatementAccountName": IncomeStatementAccountNames.OTHER_EXPENSES,
        },
    ]
}
