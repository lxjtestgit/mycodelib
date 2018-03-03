"【fork和exec组合使用】：直到你输入q之前，程序会一直分支出新的进程，但子进程不再在同一个文件中调用函数，而是运行一个全新的程序。"

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
