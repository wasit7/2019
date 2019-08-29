from aiohttp import web

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    return web.Response(text=text)

async def counter(request):
    return web.Response(text="count"+"5")

app = web.Application()
app.add_routes([web.get('/', handle),
                web.get('/counter/', counter)])

web.run_app(app,port=8081)