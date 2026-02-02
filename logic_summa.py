# logic_summa.py
import re
from datetime import datetime
from collections import Counter

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

from collections import Counter

def analyze_digits(number: str) -> tuple[str, str]:
    """
    Возвращает две строки:
    - Цифры, которые есть: в формате '1 (2), 3 (1), ...'
    - Цифры, которых нет: в формате '2, 5, 9'
    0 не учитывается вообще.
    """
    counts = Counter(number)

    present = []
    absent = []

    for digit in map(str, range(1, 10)):  # исключаем 0
        if digit in counts:
            present.append(f"{digit} ({counts[digit]})")
        else:
            absent.append(digit)

    present_str = ", ".join(present)
    absent_str = ", ".join(absent)

    return present_str, absent_str



def calculate_personal_year(day: int, month: int, year: int) -> int:
    """
    Личный год:
    (текущий год → сумма цифр → однозначное)
    + день + месяц рождения
    → однозначное
    """
    current_year = datetime.now().year
    year_sum = reduce_to_single_digit(sum(int(d) for d in str(current_year)))

    total = year_sum + day + month
    return reduce_to_single_digit(total)


def calculate_personal_months(personal_year: int) -> str:
    """
    Расписывает месяцы с января по декабрь:
    личный год + номер месяца → однозначное
    Возвращает строку в столбик
    """
    months = [
        "Январь", "Февраль", "Март", "Апрель",
        "Май", "Июнь", "Июль", "Август",
        "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
    ]

    lines = []
    for i, month_name in enumerate(months, start=1):
        value = reduce_to_single_digit(personal_year + i)
        lines.append(f"{month_name}: {value}")

    return "\n".join(lines)




def build_psychomatrix(day: int, month: int, year: int) -> list[list[str]]:
    """
    Строит психоматрицу (квадрат Пифагора) по дате рождения
    Возвращает матрицу 3×3 из строк
    """
    digits = f"{day}{month}{year}"
    digits = [d for d in digits if d != "0"]
    counts = Counter(digits)

    layout = [
        ["3", "6", "9"],
        ["2", "5", "8"],
        ["1", "4", "7"],
    ]

    matrix = []
    for row in layout:
        matrix.append([
            digit * counts.get(digit, 0) for digit in row
        ])

    return matrix


def psychomatrix_to_ascii(
    matrix: list[list[str]],
    cell_width: int = 11,
    empty_content: str = "---"  # три тире для пустых
) -> str:
    h_line = "+" + "+".join(["-" * cell_width] * 3) + "+"

    lines = [h_line]
    for row in matrix:
        formatted_cells = []
        for cell in row:
            # Ограничиваем длину строки до cell_width
            content = str(cell)[:cell_width] if cell else empty_content
            formatted_cells.append(f"{content:^{cell_width}}")  # центрируем
        lines.append("|" + "|".join(formatted_cells) + "|")
        lines.append(h_line)

    return "\n".join(lines)


from PIL import Image, ImageDraw, ImageFont

def draw_psychomatrix_image(matrix, cell_size=80, empty_content="---"):
    """
    Рисует психоматрицу как картинку.
    
    matrix: 3x3 список строк (например, build_psychomatrix)
    cell_size: размер одной ячейки
    empty_content: что показывать в пустой ячейке
    """
    rows = len(matrix)
    cols = len(matrix[0])

    width = cols * cell_size + 1
    height = rows * cell_size + 1

    img = Image.new("RGB", (width, height), color="white")
    draw = ImageDraw.Draw(img)

    # Шрифт
    try:
        font = ImageFont.truetype("arial.ttf", int(cell_size * 0.4))
    except:
        font = ImageFont.load_default()

    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            x0 = j * cell_size
            y0 = i * cell_size
            x1 = x0 + cell_size
            y1 = y0 + cell_size

            fill_color = "white" if cell else "#DDDDDD"

            # Рисуем ячейку
            draw.rectangle([x0, y0, x1, y1], fill=fill_color, outline="black", width=2)

            # Текст
            content = cell if cell else empty_content
            w, h = draw.textsize(content, font=font)
            draw.text(
                (x0 + (cell_size - w) / 2, y0 + (cell_size - h) / 2),
                content,
                fill="black",
                font=font
            )

    return img




