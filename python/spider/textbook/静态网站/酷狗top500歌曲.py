import Requests
from bs4 import BeautifulSoup
import time

#使用requests进行网页的获取、
#使用bs4进行网页的解析
#使用bs4的select方法进行定位

headers = {
    'user-agent' :' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
def get_info(url):
    wb_data = Requests.get(url,headers = headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    
    ranks = soup.select('span.pc_temp_num')
    titles = soup.select('div.pc_temp_songlist> ul > li> a ')
    times = soup.select('span.pc_temp_tips_r > span ')
    for rank in ranks:
        data ={
            'rank':rank.get_text().strip(),
            'singer':title.get_text().split('-')[0],
            'song':title.get_text().split('-')[1],
            'time':time.get_text().strip()
        }
        print(data)
    
if __name__ == '__main__':
    urls = ['https://www.kugou.com/yy/rank/home/{}-8888.html'.format(str(i)) for i in rang(1,24)]
    for url in urls:
        get_info(url)
        time.sleep(2)
