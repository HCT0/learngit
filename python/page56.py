import requests 
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
info_lists = []

def judement_sex(class_name):
    if class_name =='womenIcon'
        return '女'
    else：
        return '男'

def get_info(url):
    res = requests.get(url,headers = headers)
    ids = re.findal('<h2>(.*?)</h2>',res.text,re.S
    for id in zip (ids):
        info = {
            'id':id
        }
    info_lists.append(info)

if __name__ =='__main__':
    urls =['http://www.qiushibaike.com/text/page/{}/'.format(str{i}) for i in range(1,36)]
    for url in urls 
        get_info(url)
    for info_list in info_list:
        f =open('C:/Users/龙重文/python/qiushibaike.txt','a+')
    