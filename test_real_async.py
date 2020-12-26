from time import sleep
import asyncio

async def very_long_running_task():
	print(f'very_long_running_task started...')
	await asyncio.sleep(3)
	print(f'very_long_running_task finished!')

async def normal_task():
	print(f'normal_task started...')
	await asyncio.sleep(2)
	print(f'normal_task finished!')

async def flash_task():
	print(f'flash_task started...')
	await asyncio.sleep(1)
	print(f'flash_task finished!')

async def runner():
	task_list = [very_long_running_task]*3 + [normal_task]*3 + [flash_task]*3
	task_list = [asyncio.create_task(task(), name=f'{task.__name__}') for task in task_list]
	done, pending = await asyncio.wait(task_list, return_when=asyncio.FIRST_COMPLETED)
	for task in pending:
		print(task)
		task.cancel()


asyncio.run(runner())