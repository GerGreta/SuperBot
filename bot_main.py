import threading
from ping_server import run_ping_server

# Запускаем ping-сервер в отдельном потоке
threading.Thread(target=run_ping_server, daemon=True).start()


import asyncio
from handlers import dp, bot  # остаётся как есть

async def main():
    print("🤖 Бот запускается через polling...")
    try:
        await dp.start_polling(bot)
    except Exception as e:
        print(f"❌ Ошибка запуска бота: {e}")

if __name__ == "__main__":
    asyncio.run(main())
