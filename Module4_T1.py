from datetime import datetime


def get_days_from_today(date: str) -> int:
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - input_date).days
    except ValueError:
        raise ValueError("Неправильний формат дати. Використовуйте РРРР-ММ-ДД")