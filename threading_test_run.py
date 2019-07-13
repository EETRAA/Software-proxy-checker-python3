import time, threading
def loop():#run_over
    print('thread %s is running...%s' % (threading.current_thread().name, time.ctime(time.time())))
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s %s' % (threading.current_thread().name, n, time.ctime(time.time())))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)

print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t2 = threading.Thread(target=loop, name='LoopThread')
t.start()
t2.start()
t.join()
t2.join()
print('thread %s ended.' % threading.current_thread().name)