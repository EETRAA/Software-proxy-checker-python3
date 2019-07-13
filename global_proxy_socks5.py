import requests
import socks
import socket

# socks.set_default_proxy(proxy_type=socks.SOCKS5,addr="166.62.83.128",port=12534,rdns=True,username='',password='')

# socket.socket = socks.socksocket


# r=requests.get('https://www.google.com',timeout=5)
# r=requests.get('http://spys.one',timeout=5)
r=requests.get('https://www.baidu.com',timeout=5)

print(r.status_code)
# print(r.text)#html file
