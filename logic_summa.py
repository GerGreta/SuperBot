# logic_summa.py
import re

def reduce_to_single_digit(n: int) -> int:
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

def parse_date(text: str):
    # Ищем дату с разделителями: дд.мм.гггг, дд/мм/гггг или дд-мм-гггг
    match = re.search(r'(\d{1,2})[./-](\d{1,2})[./-](\d{2,4})', text)
    if match:
        day, month, year = match.groups()
        day = int(day)
        month = int(month)
        year = int(year)
        if 1 <= day <= 31 and 1 <= month <= 12:
            return day, month, year

    # Проверяем 8 цифр без разделителей
    if re.fullmatch(r'\d{8}', text):
        day = int(text[0:2])
        month = int(text[2:4])
        year = int(text[4:8])
        if 1 <= day <= 31 and 1 <= month <= 12:
            return day, month, year

    # Проверяем 7 цифр без разделителей — день из 1 цифры
    if re.fullmatch(r'\d{7}', text):
        day = int(text[0:1])
        month = int(text[1:3])
        year = int(text[3:7])
        if 1 <= day <= 9 and 1 <= month <= 12:
            return day, month, year

    return None

def calculate_consciousness(day: int) -> int:
    return reduce_to_single_digit(day)

def calculate_action(day: int, month: int, year: int) -> int:
    all_digits = f"{day}{month}{year}"
    total = sum(int(d) for d in all_digits)
    return reduce_to_single_digit(total)
