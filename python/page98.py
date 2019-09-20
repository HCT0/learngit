import requests
import json
from bs4 import Beautifulsoup
headers ={
    ' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
url_path = 'https://www.pexels.com/search/'
word = input('请输入你要下载的图片')
#调用斯必克的翻译api,可以对输入的中文进行翻译
url_tra ='http://howto speak.org:443/api/e2c?user_key=dfcacb6404295f9ed9e430f67b641a8e&notrans=0&text='+word
english_data =requests.get(url_tra)
#将数据解析为json数据
js_data = json.loads(englisn_data)
#从json格式当中获取数据
content = js_data['english']
#结合翻译的英文，以及对应的url格式，构造新的uel路径，给下面使用
url = url_path + content +'/'
#使用ruquests,从而获取到需要的图片的页面
wb_data = requests.get(url,headers = headers)
soup = Beautifulsoup(wb_data.txt,'lxml')
#获取这个页面的图片的url
imgs =soup.select('article > a >img')
list = []
#将获取到的url存储到列表当中
for img in imgs :
    photo =img .get('src')
    list.append(photo)
#定义存储图片的地址  
path =''
#逐个的调用url,获取图片
for item in list:
    data = requests.get(item,headers = headers )
    #使用item来打开文件
    fp = open(path +item .split('?')[0][-10:],'wb')
    fp.writte(data.content)
    fp.close()