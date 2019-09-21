import requests
#这个是正则表达式的库
import re
import time

headers ={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
#打开指定的文件
f =open('C:/Users/龙重文/learngit/python/doupo.txt','a+')
#一个实现爬取内容的类
def get_info(url):
    res = requests.get(url,headers = headers)
    if res.status_cpde == 200:
        #. 爬取任意一个字符，*和？爬取0个或者1或者无限个
        #findall是以列表的形式来返回获取的数据
        contents = re.findall('<p>(.*?)</p>',res.content.decode('utf-8'),re.s)
        for content in contents:
            #写入文件
            f.write(content+'\n') 
    else:
        pass
if __name__ == '__main__':
    urls =['http://www.doupoxs.com.doupocangqiong/{}.html'.format(str(i)) for i in range(2,1665)]
    for url in urls:
        get_info(url)
        time.sleep(2)
f.close()
