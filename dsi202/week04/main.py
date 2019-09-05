from aiohttp import web
import sqlite3
from datetime import datetime

html="""
<!DOCTYPE html>
<html>
<body>
<h1>My First Heading</h1>
<p>Hello %s</p>
%s
</body>
</html>
"""

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
    table = """
    <table>
        <tr>
            <th>Datetime</th>
            <th>Name</th>
        </tr>
        <tr>
            <td>2019-9-5</td>
            <td>Maria Anders</td>
        </tr>
    </table>    
    """
    usercounter(name)
    return web.Response(text=html%(name,table),content_type='text/html')

app = web.Application()
app.router.add_get('/counter/{name}', handle)

web.run_app(app,port=8082)

#go to http://localhost:8082/counter/einstien