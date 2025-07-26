import asyncio
import os
from aiohttp import web
from handlers import dp, bot
from ping_server import app as ping_app
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application

WEBHOOK_PATH = "/webhook"
WEBHOOK_HOST = os.getenv("RENDER_EXTERNAL_URL", "https://your-bot.onrender.com")
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"


async def on_startup(app):
    await bot.set_webhook(WEBHOOK_URL)
    print(f"✅ Webhook установлен: {WEBHOOK_URL}")


async def on_shutdown(app):
    await bot.delete_webhook()
    print("❌ Webhook удалён")


def create_app():
    app = web.Application()
    app["bot"] = bot

    SimpleRequestHandler(dispatcher=dp, bot=bot).register(app, path=WEBHOOK_PATH)

    # Исправлено: Пинг-сервер на /ping
    app.add_subapp("/ping", ping_app)

    app.on_startup.append(on_startup)
    app.on_shutdown.append(on_shutdown)
    return app



if __name__ == "__main__":
    try:
        web.run_app(create_app(), host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
    except KeyboardInterrupt:
        print("Бот остановлен")
