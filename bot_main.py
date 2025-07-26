import asyncio
import os
from handlers import dp, bot
from ping_server import app

async def start_bot():
    print("Бот запускается...")
    await dp.start_polling(bot)

async def main():
    port = int(os.getenv("PORT", 8000))
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"HTTP сервер запущен на порту {port}")

    await start_bot()

if __name__ == "__main__":
    from aiohttp import web
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
