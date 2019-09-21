import requests 
from lxml import etree
import pymongo
from multiprocessing import Pool
#连接本地的mangodb数据库
client = = pymongo.MongoClient('localhost',27017)
mydb = client['mydb']
jianshu_shouye = mydb['jianshu_shouye']

def get_jianshu_info(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="note-list"]/li')

    for info in infos:
        try:
            author =info.xpath('div/div[1]/div/a/text()')[0]
            rewards = info.xpath('div/div[2]/span[2]/text()')
            if len(rewards)==0:
                reward = "无"
            else:
                reward =rewards[0].strip()
            data ={
                'author':author,
                'reward':reward,
            }
            jianshu_shouye.insert_one(data)
        except IndexError:
            pass
if __name__ == '__main__':
    #构建网站url大全
    urls =['http://www.jianshu.com/c/bDHhpK?order_by=commented_at&page={}'.format(str(i)) for i in range(1,10001)]
    #创建一个四进程的进程
    pool = Pool(processed=4)
    #使用map调用函数
    pool.map(get_jianshu_info,urls)