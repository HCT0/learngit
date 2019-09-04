import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
res = requests.get('http://bj.xiaozhu.com/',headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
print(soup.prettify)