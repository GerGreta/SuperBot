import re
from datetime import datetime, timedelta


def reduce_to_digit(n: int) -> int:
    """
    Приведение числа к однозначному.
    """
    while n > 9:
        n = sum(int(d) for d in str(n))
    return n


def parse_day_month(text: str):
    """
    Извлекает день и месяц из строки.
    Поддерживает форматы:
    2404, 24.04, 24/04, 24-4, 244 (24.4)
    """
    digits = re.sub(r"\D", "", text)

    if len(digits) == 4:
        day = int(digits[:2])
        month = int(digits[2:])
    elif len(digits) == 3:
        day = int(digits[:2])
        month = int(digits[2])
    else:
        return None, None

    if 1 <= day <= 31 and 1 <= month <= 12:
        return day, month

    return None, None


def get_russian_weekday(date_obj: datetime) -> str:
    """
    Возвращает день недели на русском языке.
    """
    weekdays = {
        0: "Понедельник",
        1: "Вторник",
        2: "Среда",
        3: "Четверг",
        4: "Пятница",
        5: "Суббота",
        6: "Воскресенье",
    }
    return weekdays[date_obj.weekday()]


def calculate_personal_days(birth_day: int, birth_month: int) -> str:
    """
    Расчёт личного дня на сегодня и следующие 8 дней.
    Формат вывода:
    18.02.2026, Среда - 4
    """
    today = datetime.now()

    # Число рождения
    birth_number = reduce_to_digit(
        sum(int(d) for d in f"{birth_day}{birth_month}")
    )

    # Число текущего года
    year_number = reduce_to_digit(
        sum(int(d) for d in str(today.year))
    )

    results = []

    for i in range(9):
        current_date = today + timedelta(days=i)

        total = (
            birth_number
            + year_number
            + current_date.month
            + current_date.day
        )

        personal_day = reduce_to_digit(total)

        formatted_date = current_date.strftime("%d.%m.%Y")
        weekday = get_russian_weekday(current_date)

        results.append(
            f"{formatted_date}, {weekday} - {personal_day}"
        )

    return "\n".join(results)


def logic_day(text: str) -> str:
    """
    Главная функция для использования в боте.
    Принимает текст пользователя и возвращает результат.
    """
    day, month = parse_day_month(text)

    if day and month:
        return calculate_personal_days(day, month)

    return None
