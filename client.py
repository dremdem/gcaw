
# WS client example

import asyncio
import websockets

from aioconsole import ainput

async def producer(ws):
	message = await ainput("> ")
	await ws.send(message)

async def consumer(ws):
	try:
		message = await ws.recv()
		print(f"< {message}")
	except websockets.exceptions.ConnectionClosedError:
		print('Connection lost.')
		return 0

async def close(ws):
	await ws.wait_closed()


async def hello():
	uri = "ws://localhost:8765"
	name = input("What's your name? ")
	async with websockets.connect(uri) as websocket:
		await websocket.send(name)
		while True:
			con_task = asyncio.create_task(consumer(websocket))
			prod_task = asyncio.create_task(producer(websocket))
			done, pending = \
				await asyncio.wait([con_task, prod_task],
				return_when=asyncio.FIRST_COMPLETED)

			for task in pending:
				task.cancel()

			if 0 in map(lambda x: x.result(), list(done)):
				break




asyncio.get_event_loop().run_until_complete(hello())
