# handlers.py
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart
from logic_summa import word_to_sum, reduce_to_single_digit
from logic_number import parse_date, calculate_consciousness, calculate_action

TOKEN_SUMMA = os.getenv("BOT_TOKEN_SUMMA")
TOKEN_NUMBER = os.getenv("BOT_TOKEN_NUMBER")

# Для простоты будем использовать один Dispatcher и бота — токен можно менять при запуске.
# Но если хочешь запускать 2 бота одновременно — лучше разделять их на разные процессы.

# Для демонстрации — создадим два бота (при запуске берём один токен)
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    await message.answer(
        "Привет! Напиши слово (русское или английское) для подсчёта суммы букв, "
        "или дату рождения (формат: 24041991) для расчёта чисел Сознания и Действия."
    )

@dp.message()
async def message_handler(message: types.Message):
    text = message.text.strip()

    # Попробуем распознать дату
    date = parse_date(text)
    if date:
        day, month, year = date
        consciousness = calculate_consciousness(day)
        action = calculate_action(day, month, year)
        await message.answer(
            f"Дата рождения: {day:02}.{month:02}.{year}\n"
            f"Число Сознания: {consciousness}\n"
            f"Число Действия: {action}"
        )
        return

    # Иначе — считаем слово
    result = word_to_sum(text)
    if result is not None:
        reduced = reduce_to_single_digit(result)
        await message.answer(
            f"Слово: {text}\n"
            f"Сумма по буквам: {result}\n"
            f"Однозначная сумма: {reduced}"
        )
        return

    await message.answer("Не могу распознать дату или слово. Попробуй ещё раз.")
