from lxml import etree
import requests
import pymong
import re
import json
from multiprocesses import Pool
client = pymongo.MongoClient('localhost',27017)
mybd =client['mydb']

sevenday = mydb['sevenday']

header = {
    'User-agent':'' User-Agent ' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
def  get_url(url):
    html = requests.get(url,headers = header)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class='note-list']/li')
    for info in infos:
        article_url_part = info.xpath('div/a/@href')[0]
        get_info(article_url_part)
def get_info(url):
    article_url= 'http://www.jianshu.com.' + url
    html = requests.get(article_url,headers = header)
    selector = etree.HTML(html.text)
    author = selector.xpath('//span[@class="name"]/a/text()')[0]
    article =  selector.xpath('//h1[@class="title"]/text()')[0]

    gain_url = 'htpp://www.jianshu.com/notes/{}/rewards?count=20'.format(id)
    wb_data = json.loads(wb_data.text)
    gian = json_data['reward_count']

    incluede_list = []
    incuede_urls =['http://www.jiansh.com/notes/{}/included_collections?page={}'.format(is,str(i) for i in range(1,10))]
    for include_url in include_urls:
        html = requests.get(include_url,headers = header)
        json_data = json.loads(html.text)
        inluceds = json_data['collections']
        if len(include ) == 0:
            pass 
        else:
            for include in cludes:
                include_title = include['title']
            info = {
                'author':author,               
            }
            sevenday_list.insert_onr(info)

    if __name__ == '__main__':
        urls = ['http://www.jianshu.com/treanding/weekly?page={}'.format(str(i)) for i in range(0,11)]
        pool = Pool(processes = 4)
        pool.map(get_url,urls)