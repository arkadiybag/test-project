from aiohttp import web, WSCloseCode

from view import WsView


async def on_shutdown(app):
    for ws in app['websockets']:
        await ws.close(code=WSCloseCode.GOING_AWAY,
                       message='Server shutdown')

if __name__ == '__main__':
    app = web.Application(client_max_size=0)
    app['websockets'] = []

    app.router.add_route('GET', '/ws/', WsView)

    app.on_shutdown.append(on_shutdown)

    web.run_app(app, path='main.sock')
    # web.run_app(app, host='127.0.0.1', port=8000)
