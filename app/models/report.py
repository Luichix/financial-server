from enum import Enum


class TypeFrecuencyName(str, Enum):
    annual = "Anual"
    semiannual = "Semestral"
    quarterly = "Trimestral"
    bimonthly = "Bimensual"
    monthly = "Mensual"
    biweekly = "Quincenal"
    weekly = "Semanal"
    daily = "Diaria"


class TypePeriodName(str, Enum):
    annual = "Año(s)"
    semiannual = "Semestre(s)"
    quarterly = "Trimestre(s)"
    bimonthly = "Bimenstre(s)"
    monthly = "Mes(es)"
    biweekly = "Quincena(s)"
    weekly = "Semana(s)"
    daily = "Dia(s)"
