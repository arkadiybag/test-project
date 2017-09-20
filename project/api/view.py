import asyncio
import random
import string
import logging

import aiohttp
from aiohttp import web
from aiohttp.web_response import json_response

logger = logging.getLogger()

# https://docs.google.com/document/d/19h_HhZ_iBhIMxTM8AnzPA61J407WRl1-ncuEMlF6quw/


class WsView(web.View):
    async def get(self):
        await self.websocket_handler(self.request)

        return json_response({'success': True})

    async def websocket_handler(self, request):
        ws = web.WebSocketResponse()
        await ws.prepare(request)
        request.app['websockets'].append(ws)

        asyncio.ensure_future(self.timer(ws))

        async for msg in ws:
            if msg.type == aiohttp.WSMsgType.TEXT:
                if msg.data == 'close':
                    await ws.close()

            if msg.type == aiohttp.WSMsgType.ERROR:
                print('ws connection closed with exception %s' %
                      ws.exception())

        print('websocket connection closed')

        return ws

    async def timer(self, ws):
        items = list(string.ascii_lowercase)  # + list(map(str, range(0, 9)))
        while True:
            if ws.closed:
                break

            msg = ''.join([random.choice(items) for i in range(random.randint(5, 15))])

            ws.send_str(msg)
            await asyncio.sleep(1)
