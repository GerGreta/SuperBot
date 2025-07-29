import asyncio
import os
from aiohttp import web
from handlers import dp, bot

async def handle(request):
    return web.Response(text="OK")

async def start_polling():
    print("Запускаю polling...")
    await dp.start_polling(bot)

async def main():
    app = web.Application()
    app.add_routes([web.get('/', handle)])

    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8000))
    site = web.TCPSite(runner, '0.0.0.0', port)
    await site.start()

    print(f"HTTP сервер запущен на порту {port}")

    await start_polling()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен")
