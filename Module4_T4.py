from datetime import datetime, date, timedelta
from typing import List, Dict


def get_birthday_for_year(birthday: date, year: int) -> date:
    try:
        return birthday.replace(year=year)
    except ValueError:
        # Якщо дата 29.02, а рік не високосний,
        # вважаємо день народження 28.02
        return date(year, 2, 28)


def get_upcoming_birthdays(users: List[Dict[str, str]]) -> List[Dict[str, str]]:
    today: date = date.today()
    upcoming_birthdays: List[Dict[str, str]] = []

    for user in users:
        birthday: date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year: date = get_birthday_for_year(birthday, today.year)

        if birthday_this_year < today:
            birthday_this_year = get_birthday_for_year(birthday, today.year + 1)

        delta_days: int = (birthday_this_year - today).days

        if 0 <= delta_days <= 7:
            congratulation_date: date = birthday_this_year

            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append(
                {
                    "name": user["name"],
                    "congratulation_date": congratulation_date.strftime("%Y.%m.%d"),
                }
            )

    return upcoming_birthdays


if __name__ == "__main__":
    users = [
        {"name": "John Doe", "birthday": "1985.01.23"},
        {"name": "Jane Smith", "birthday": "1990.01.27"},
        {"name": "Leap User", "birthday": "1992.02.29"},
    ]

    upcoming_birthdays = get_upcoming_birthdays(users)
    print("Список привітань на цьому тижні:", upcoming_birthdays)
