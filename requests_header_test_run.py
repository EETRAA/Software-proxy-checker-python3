import requests
proxies = {'https':'socks5://109.234.38.136:1080'}
# headers={
# 'Host': 'www.google.com',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0',
# 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
# 'Accept-Language': 'en-US,en;q=0.5',
# 'Accept-Encoding': 'gzip, deflate, br',
# 'Connection': 'keep-alive',
# 'Upgrade-Insecure-Requests': '1'
# }
r=requests.get('https://www.baidu.com', proxies=proxies, timeout=5)#, headers=headers
print(r.status_code)