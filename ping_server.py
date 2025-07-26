from aiohttp import web

async def handle(request):
    return web.Response(text="OK")

app = web.Application()
app.add_routes([web.get("/", handle)])

if __name__ == "__main__":
    import os
    port = int(os.getenv("PORT", 8000))
    web.run_app(app, port=port)
