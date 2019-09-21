'''
titie xpath://*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/div[1]/a
introduce xpath ://*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/p[1]

point xpath://*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/div[2]/span[2]\

best comment xpath://*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/p[2]/span

'''

form lxml import etree 
import requests
import csv # 用来存储内容的库

#打开一个文件路径
fp =open ('','wt',newline='',encoding ='utf-8')
writer = csv.writer(fp)
#构建文件和格式
writer.writerow(('title'))

urls = ['http://book.douban.com/top250?start={}'.format(str(i)) for i in range(0,250,25)]
#创建浏览器头，模拟
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
#通过循环将纳入每一个url
for url in urls:
    #获取网页
    html = requests.get(url,headers = headers)
    #解析网页
    selector = etree.HTML(html.text)
    #通过xpath进行数据清洗
    title = selector.Xpath('//*[@id="content"]/div/div[1]/div/table[1]/tbody/tr/td[2]/div[1]/a')
    #写入到csv文件当中
    writer.writerow((title))

fp.close()