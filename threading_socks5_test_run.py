import requests
# import socks
# import socket
import time, threading

def loop1():#voerride_run
    # socks.set_default_proxy(proxy_type=socks.SOCKS5,addr="166.62.83.128",port=12534,rdns=True,username='',password='')
    # socket.socket = socks.socksocket
    # r=requests.get('http://spys.one',timeout=5)
    # print(r.status_code)
    proxies1 = {'http': "socks5://192.169.190.207:10976"}
    r=requests.get('http://www.baidu.com', proxies=proxies1, timeout=10)
    print(r.status_code)
def loop2():#voerride_run
    # socks.set_default_proxy(proxy_type=socks.SOCKS5,addr="166.62.83.45",port=12534,rdns=True,username='',password='')
    # socket.socket = socks.socksocket
    # r=requests.get('http://spys.one',timeout=5)
    # print(r.status_code)
    proxies2 = {'http': "socks5://109.234.38.136:1080"}
    r=requests.get('http://www.baidu.com', proxies=proxies2, timeout=10)
    print(r.status_code)
print('thread %s is running...' % threading.current_thread().name)
t = threading.Thread(target=loop1, name='LoopThread')
t2 = threading.Thread(target=loop2, name='LoopThread')
t.start()
t2.start()
t.join()
t2.join()
print('thread %s ended.' % threading.current_thread().name)