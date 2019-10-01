import requests
from lxml import etree
import re
import time

#使用requests进行网页的获取
#使用lxml进行网页的整理
#采用Xpath的方式进行定位
#采用正则的方式进行定位

headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
        }

urls = ['https://movie.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
print(urls)
for url in urls:
    print(url)
    time.sleep(1)
    html_data = requests.get(url,headers = headers)
    #print(html_data.text) 
    #print(html_data)
    #整理获取到的数据
    html = etree.HTML(html_data.text)
    #print(html)
    #转换为html格式 
    #result = etree.tostring(html)
    #print(result)
    
    #使用xpath进行定位
    
    titles = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a/span[1]/text()')
    points = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[2]/text()')
    comments = html.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[2]/div/span[4]/text()')
    
    #使用re进行定位
    #print(html_data.text)
    '''
    titles = re.findall('<span class="title">(.{0,10})</span>',html_data.text)
    points = re.findall('<span class="rating_num" property="v:average">(.*)</span>',html_data.text)
    comments = re.findall('<span>(\d.*)</span>',html_data.text)
    '''
    for title,point,comment in zip(titles,points,comments):
        #print(title,point,comment)
        fp = open('doubanmovie.txt','a+',encoding='utf-8')
        fp.write(title)
        fp.write('\t')
        fp.write(point)
        fp.write('\t')
        fp.write(comment)
        fp.write('\n')
        fp.close()

