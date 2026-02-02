import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

from logic_number import word_to_sum, reduce_to_single_digit
from logic_summa import (
    parse_date,
    calculate_consciousness,
    calculate_action,
    analyze_digits,
    calculate_personal_year,
    calculate_personal_months,
    build_psychomatrix,
    psychomatrix_to_ascii,
)

TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Привет!\n\n"
        "🔹 Напиши слово (русское или английское) — я посчитаю сумму букв\n"
        "🔹 Или дату рождения (например: 24.04.1991 или 24041991)\n\n"
        "Я рассчитаю:\n"
        "• Число Сознания\n"
        "• Число Действия\n"
        "• Психоматрицу\n"
        "• Личный год\n"
        "• Личные месяцы (январь–декабрь)"
    )


@dp.message()
async def message_handler(message: types.Message):
    text = message.text.strip()

    # 1️⃣ Пробуем распознать дату
    date = parse_date(text)
    if date:
        day, month, year = date

        consciousness = calculate_consciousness(day)
        action = calculate_action(day, month, year)

        personal_year = calculate_personal_year(day, month, year)
        personal_months = calculate_personal_months(personal_year)

        present_str, absent_str = analyze_digits(text)

        # психоматрица
        matrix = build_psychomatrix(day, month, year)
        matrix_ascii = psychomatrix_to_ascii(matrix, cell_width=9)

        await message.answer(
            f"📅 Дата рождения: {day:02}.{month:02}.{year}\n\n"
            f"🧠 Число Сознания: {consciousness}\n"
            f"🔥 Число Действия: {action}\n\n"
            f"🧩 Личная матрица:\n"
            f"{matrix_ascii}\n\n"
            f"🔢 Цифры, которые есть: {present_str}\n"
            f"⭕ Цифры, которых нет: {absent_str}\n\n"
            f"🌱 Личный год: {personal_year}\n"
            f"📆 Личные месяцы:\n{personal_months}"
        )
        return

    # 2️⃣ Иначе — считаем слово
    result = word_to_sum(text)
    if result is not None:
        reduced = reduce_to_single_digit(result)
        await message.answer(
            f"🔤 Слово: {text}\n"
            f"➕ Сумма по буквам: {result}\n"
            f"🔹 Однозначная сумма: {reduced}"
        )
        return

    # 3️⃣ Если вообще не распознали
    await message.answer(
        "🤔 Не могу распознать сообщение.\n"
        "Попробуй написать слово или дату рождения."
    )
