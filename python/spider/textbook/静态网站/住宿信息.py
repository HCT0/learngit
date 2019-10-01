from bs4 import BeautifulSoup
import requests

#使用requests进行网页的获取、
#使用bs4进行网页的解析
#使用bs4的select方法进行需要信息的定位


#定义网站的头部
headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
urls = ['http://bj.xiaozhu.com/serach-duanzufang-p{}-0/'.format(number)for number in range(1,14)]
for url in urls:
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')

    links = soup.select('#page_list> ul > li >a')
    '''a = isinstance(links,list)
    b = isinstance(links,dict)
    print("test",a)
    print("test",b)
    '''
    for link in links:
        href = link.get("href")
        wb_data2 = requests.get(href,headers= headers )
        soup2 = BeautifulSoup(wb_data2.text,'lxml')
        addresses = soup2.select('span.pr5')
        for address in addresses:
            print(address)