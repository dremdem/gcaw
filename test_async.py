from time import sleep

def very_long_running_task():
	print(f'very_long_running_task started...')
	sleep(3)
	print(f'very_long_running_task finished!')

def normal_task():
	print(f'normal_task started...')
	sleep(2)
	print(f'normal_task finished!')

def flash_task():
	print(f'flash_task started...')
	sleep(1)
	print(f'flash_task finished!')



task_list = [very_long_running_task]*3 + [normal_task]*3 + [flash_task]*3

for task in task_list:
	task()
