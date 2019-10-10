from aiohttp import web
import aiohttp_jinja2
import jinja2

@aiohttp_jinja2.template('index.html')
async def handle(request):
    header=['X','Y','Z']
    data=[[3,4,5],[4,7,9]]
    return {'header':header,'data':data}

app = web.Application()
aiohttp_jinja2.setup(app,
    loader=jinja2.FileSystemLoader('./templates'))
app.add_routes([web.get('/', handle),
                web.get('/{name}', handle)])

if __name__ == '__main__':
    web.run_app(app,port=8081)

    