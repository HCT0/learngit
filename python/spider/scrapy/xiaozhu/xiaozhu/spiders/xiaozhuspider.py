import scrapy
from xiaozhu.items import XiaozhuItem

class xiaozhu(scrapy.Spider):
    name='xiaozhu'
    start_urls = ['http://bj.xiaozhu.com/fangzi/5040372114.html']

    def parse(self,response):
        item = XiaozhuItem()
        selector = Selector(response)
        title = selector.xpath('/html/body/div[3]/div[1]/div[1]/h4/em/text()')
        item['title'] = title

        
    