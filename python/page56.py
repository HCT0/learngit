import requests 
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
info_lists = []

def judement_sex(class_name):
    if class_name =='womenIcon':
        return '女'
    else:
        return '男'

def get_info(url):
    res = requests.get(url,headers = headers)
    ids = re.findall('<h2>(.*?)</h2>',res.text,re.S)
    for id in zip (ids):
        info = {
            'id':id,
        }
    info_lists.append(info)

if __name__ =='__main__':
    #format
    #循环
    #列表
    urls =['http://www.qiushibaike.com/text/page/{}/'.format(str(i)) for i in range(1,36)]
    for url in urls :
        get_info(url)
    for info_list  in info_lists:
        f =open('C:/Users/龙重文/learngit/python/qiushibaike.txt','a+')
        f.write(info_list['id']+'\n')
        f.close()

    """
        浏览器中select和xpath的使用
        git在VScode的使用
        
    """
    
                                                                                                                                                                                                                                                                                                                                                                                                                  