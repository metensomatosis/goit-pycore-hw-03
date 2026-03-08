from datetime import datetime, date, timedelta


def get_upcoming_birthdays(users):
    today = date.today()
    upcoming_birthdays = []

    for user in users:
        birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        # День народження в поточному році
        birthday_this_year = birthday.replace(year=today.year)

        # Якщо вже минув — беремо наступний рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Різниця в днях між сьогодні і найближчим днем народження
        delta_days = (birthday_this_year - today).days

        # Якщо день народження в межах 7 днів включно
        if 0 <= delta_days <= 7:
            congratulation_date = birthday_this_year

            # Якщо субота — переносимо на понеділок
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            # Якщо неділя — переносимо на понеділок
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays


# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)