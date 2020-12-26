#!/usr/bin/env python

# WS server example

import asyncio
import websockets

users = {}


async def register(user_name, ws):
    users.update({user_name: {'ws': ws}})
    await broadcast(f'connected!', user_name)


async def unregister(user_name):
    if user_name in users:
        users.pop(user_name)
        await broadcast(f'Disconnected!', user_name)


async def broadcast(message, user_name):
    for u in [u for u in users if u != user_name]:
        await users[u]['ws'].send(f'[{user_name}]: {message}')


async def hello(ws, path):
    name = ''
    try:
        name = await ws.recv()
        await register(name, ws)

        async for message in ws:
            await broadcast(message, name)
    finally:
        await unregister(name)


start_server = websockets.serve(hello, "localhost", 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
