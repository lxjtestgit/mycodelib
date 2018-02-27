"分支出子进程，直到你输入'q'"

import os 

def child():
	print('Hello from child',os.getpid())
	os._exit(0)		#否则将回到父循环中

def parent():
	while True:
		newpid = os.fork()
		if newpid == 0:
			child()
		else:
			print('Hello from parent',os.getpid(),newpid)
		if input() == 'q': break

parent()
