import re
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from strands import Agent, tool


@tool
def calculate_date(base_date: str, operation: str) -> str:
    """Calcula fechas agregando o restando períodos de tiempo.

    Esta herramienta permite realizar cálculos de fechas de manera precisa,
    manejando diferentes formatos de entrada y operaciones temporales.

    Args:
        base_date: Fecha base en formato DD-MM-YYYY, DD/MM/YYYY, YYYY-MM-DD
                  o DD-mes-YYYY. Ejemplos: "30-04-2025", "30/04/2025"
        operation: Operación temporal con formato "[+/-]número unidad".
                  Unidades soportadas:
                  - Días: día, días, day, days
                  - Semanas: semana, semanas, week, weeks
                  - Meses: mes, meses, month, months
                  - Años: año, años, year, years
                  Ejemplos: "+30 días", "-2 semanas", "1 mes", "-6 months"
                  Nota: Si no se especifica signo, se asume positivo (+)

    Returns:
        str: Fecha resultante en formato DD-MM-YYYY con nombre del día y fecha
             completa en español. En caso de error, retorna mensaje descriptivo.

    Raises:
        ValueError: Cuando el formato de fecha o operación no es válido.

    Examples:
        >>> calculate_date("30-04-2025", "+30 días")
        "Resultado: 30-05-2025 (Viernes, 30 de Mayo de 2025)"

        >>> calculate_date("15/12/2024", "-2 semanas")
        "Resultado: 01-12-2024 (Domingo, 01 de Diciembre de 2024)"
    """
    try:
        # Parsear fecha base
        parsed_date = _parse_date(base_date)

        # Parsear operación
        sign, amount, unit = _parse_operation(operation)

        # Realizar cálculo
        if unit in ["día", "días", "day", "days"]:
            result = parsed_date + timedelta(days=sign * amount)
        elif unit in ["semana", "semanas", "week", "weeks"]:
            result = parsed_date + timedelta(weeks=sign * amount)
        elif unit in ["mes", "meses", "month", "months"]:
            result = parsed_date + relativedelta(months=sign * amount)
        elif unit in ["año", "años", "year", "years"]:
            result = parsed_date + relativedelta(years=sign * amount)
        else:
            return (
                f"Error: Unidad '{unit}' no reconocida. Use: días, semanas, meses, años"
            )

        return (
            f"Resultado: {result.strftime('%d-%m-%Y')} "
            f"({result.strftime('%A, %d de %B de %Y')})"
        )

    except Exception as e:
        return f"Error: {str(e)}"


def _parse_date(date_str: str) -> datetime:
    """Parsea diferentes formatos de fecha."""
    date_str = date_str.strip()

    # Mapeo de meses en español
    months_es = {
        "enero": 1,
        "febrero": 2,
        "marzo": 3,
        "abril": 4,
        "mayo": 5,
        "junio": 6,
        "julio": 7,
        "agosto": 8,
        "septiembre": 9,
        "octubre": 10,
        "noviembre": 11,
        "diciembre": 12,
    }

    # Intentar formato con nombre de mes en español (30-abril-2025)
    pattern_es = r"(\d{1,2})-([a-záéíóú]+)-(\d{4})"
    match = re.match(pattern_es, date_str.lower())
    if match:
        day, month_name, year = match.groups()
        if month_name in months_es:
            return datetime(int(year), months_es[month_name], int(day))

    # Formatos numéricos estándar
    formats = [
        "%d-%m-%Y",  # 30-04-2025
        "%d/%m/%Y",  # 30/04/2025
        "%Y-%m-%d",  # 2025-04-30
    ]

    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    raise ValueError(f"Formato de fecha no reconocido: {date_str}")


def _parse_operation(operation: str) -> tuple:
    """Parsea la operación (+/-30 días)."""
    operation = operation.strip().lower()

    # Patrón para capturar signo, número y unidad
    pattern = (
        r"([+-]?)\s*(\d+)\s*"
        r"(día|días|semana|semanas|mes|meses|año|años|"
        r"day|days|week|weeks|month|months|year|years)"
    )

    match = re.match(pattern, operation)
    if not match:
        raise ValueError(f"Formato de operación no válido: {operation}")

    sign_str, amount_str, unit = match.groups()

    sign = -1 if sign_str == "-" else 1
    amount = int(amount_str)

    return sign, amount, unit


def main():
    # Crea un agente con la configuración estándar
    agent = Agent(tools=[calculate_date])
    # Solicita al agente el cálculo de algunas fechas
    agent("""
        1) ¿Qué día será el 20-abril-2025 +45 días?
        2) ¿Qué día será el 17-julio-2025 +20 semanas?
    """)


if __name__ == "__main__":
    main()
