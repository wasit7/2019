from aiohttp import web
import sqlite3
from datetime import datetime

def usercounter(name):
    conn = sqlite3.connect('usercounter.db')
    c = conn.cursor()

    username=name
    now=datetime.now()
    time=now.isoformat()

    c.execute("INSERT INTO usercounter VALUES ('%s','%s')"%(time,username))
    conn.commit()
    conn.close()

async def handle(request):
    name = request.match_info.get('name', "Anonymous")
    text = "Hello, " + name
    usercounter(name)
    return web.Response(text=text)

app = web.Application()
app.router.add_get('/counter/{name}', handle)

web.run_app(app,port=8082)

#go to http://localhost:8082/counter/einstien