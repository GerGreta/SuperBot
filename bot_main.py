import asyncio
from handlers import dp, bot

async def main():
    print("Удаляю webhook (если установлен)...")
    await bot.delete_webhook()
    print("Запускаю polling...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
