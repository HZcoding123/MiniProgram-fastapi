"""
中间件
"""

import time
from starlette.datastructures import MutableHeaders
from starlette.types import ASGIApp, Receive, Scope, Send, Message
from fastapi import Request
from core.Helper import random_str


class Middleware:

    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope['type'] != 'http':
            await self.app(scope, receive, send)
            return
        start_time = time.time()
        req = Request(scope, receive, send)
        if not req.session.get('session'):
            req.session.setdefault('session', random_str())

        async def send_wrapper(message):
            process_time = time.time() - start_time
            if message['type'] == 'http.response.start':
                headers = MutableHeaders(scope=message)
                headers.append('X-Process-Time', str(process_time))
            await send(message)
        await self.app(scope, receive, send_wrapper)



