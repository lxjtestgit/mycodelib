"运行程序，直到你输入q"

import os

parm = 0
while True:
    parm += 1
    pid = os.fork()
    if pid ==0:         #复制进程
        os.execlp('python','python','child.py',str(parm))       #覆盖原来的程序
        assert False,'error starting program'       #不应该返回
    else:
        print('child is',pid)
        if input() == 'q': break
