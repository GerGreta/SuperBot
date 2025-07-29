# ping_server.py

from aiohttp import web

async def handle(request):
    return web.Response(text="OK")

def run_ping_server():
    app = web.Application()
    app.add_routes([web.get("/", handle)])
    web.run_app(app, port=8000)