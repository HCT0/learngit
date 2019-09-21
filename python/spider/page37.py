#多页数据的爬取,主要是找到页与页之间的规律
#导入库
from bs4 import BeautifulSoup
import requests
import time

#定义网站的头部
headers = {
   ' User-Agent ' :'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

#定义一个判断男女的类
def judgement_sex(class_name):
    if class_name == ['member_ico1']: #member是网页的设定的判断条件
        return '女'
    else:
        return '男'

#获取该页面的用户的详细页的url,并且通过循环，不断的进入每一个用户的详细页
def get_links(url):
    #进行连接
    wb_data = requests.get(url,headers=headers)
    #使用bs4的实例对象，网页数据的获取的对数据进行解析
    soup = BeautifulSoup(wb_data.text,'lxml')
    #使用bs4的select方法，获取这个页面的所有用户的详细页面入口数组
    links = soup.select('#page_list> ul > li >a')
    #循环进入一页
    for link in links:
        href = link.get("href")#get的使用
        #调用get_info函数不断的进入，然后实现详细信息的获取
        get_info(href)

#获取页面当中的信息:地址、性别、图片的img等等
def get_info(url):
    #调用requests库,实现对指定网站的连接
    wb_data = requests.get(url,headers= headers )
    #调用bs4库,实现对获取到的数据的解析，
    soup = BeautifulSoup(wb_data.text,'lxml')
    #调用bs4的select 方法，实现对获取到的网页源码的清洗,获取到需要的数据
    titles = soup.select('div.pho_info > h4')
    prices = soup.select('#pricePart >div.day_1 > span')
    addresses = soup.select('span.pr5')
    imgs = soup.select('#floatRightBox >div.js_box.clearfix > div.member_pic > a > img')
    names = soup.select('#floatRightBox > div.js_box.clearfix > div_w240 > h6 > a')
    sexs = soup.select('#floatRightBox >div.js_box.clearfix > div_member_pic > div')
    #将从一个网页获取到的数据传输到数组当中,然后使用列表的方式进行输出
    for title,address,price,img,name,sex in zip(titles,addresses,prices,imgs,names,sexs):
            data = {
                'title':title.get_text().strip(),
                'address':address.get_text().strip(),
                'price':price.get_text().strip(),
                'img':img.get("sec"),
                'name':name.get_text(),
                'sex':judgment_sex(sex.ge("class"))
            }
            #对列表的内容进行输出
            print(data)

    #作为在本文件执行的的判断,只能在本文件才执行,简称 主函数
    #通过循环的获取进入不同的url,，进入去的页
    if __name__ == '__main__':
        #创造出一个urls数组,通过规律来进行对url的组装
        urls = ['http://bj.xiaozhu.com/serach-duanzufang-p{}-0/'.format(number)for number in range(1,14)]
        #通过循环每一个url的内容的爬取
        for single_url in urls:
            get_links(single_url)#调用get_links函数，分别传递获取到的url
            time.sleep(2)#调用time的sleep函数
