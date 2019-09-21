import requests
#使用requests进行数据的爬取
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
res = requests.get('http://bj.xiaozhu.com/',headers=headers)
print(res.text)