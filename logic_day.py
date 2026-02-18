import re
from datetime import datetime, timedelta

# Сокращения месяцев и дней недели
MONTH_SHORT = {
    1: "янв.",
    2: "фев.",
    3: "мар.",
    4: "апр.",
    5: "май.",
    6: "июн.",
    7: "июл.",
    8: "авг.",
    9: "сен.",
    10: "окт.",
    11: "ноя.",
    12: "дек.",
}

WEEKDAY_SHORT = {
    0: "пн",
    1: "вт",
    2: "ср",
    3: "чт",
    4: "пт",
    5: "сб",
    6: "вс",
}


def reduce_to_digit(n: int) -> int:
    """Приведение числа к однозначному."""
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


def parse_day_month(text: str):
    """
    Извлекает день и месяц из строки.
    День: 1–2 цифры, месяц: всегда 2 цифры.
    Примеры:
    506 -> 5 июня
    2404 -> 24 апреля
    05.06 -> 5 июня
    """
    digits = re.sub(r"\D", "", text)

    if len(digits) == 3:  # dMM
        day = int(digits[0])
        month = int(digits[1:])
    elif len(digits) == 4:  # ddMM
        day = int(digits[:2])
        month = int(digits[2:])
    else:
        return None, None

    if 1 <= day <= 31 and 1 <= month <= 12:
        return day, month
    return None, None


def calculate_personal_days(birth_day: int, birth_month: int) -> str:
    """Расчёт личного дня на сегодня и следующие 8 дней (формат 18 фев. ср ➤ 4)."""
    today = datetime.now()

    birth_number = reduce_to_digit(sum(int(d) for d in f"{birth_day}{birth_month}"))
    year_number = reduce_to_digit(sum(int(d) for d in str(today.year)))

    results = []

    for i in range(9):
        current_date = today + timedelta(days=i)
        total = birth_number + year_number + current_date.month + current_date.day
        personal_day = reduce_to_digit(total)

        day = current_date.day
        month = MONTH_SHORT[current_date.month]
        weekday = WEEKDAY_SHORT[current_date.weekday()]

        results.append(f"{day} {month} {weekday} ➤ {personal_day}")

    return "\n".join(results)


def logic_day(text: str) -> str:
    """Главная функция для использования в боте."""
    day, month = parse_day_month(text)
    if day and month:
        return calculate_personal_days(day, month)
    return None
