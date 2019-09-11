import xlwt #写入Excel表中
import requets
import time
from lxml import etree

all_info_list = []
def get_info(url):
    html  = requests.get(url)
    selector = etree.HTML(html.text)
    infos = selector.xpath('//ul[@class="all-img-list cf"]/li')
    for info in infos:
        title = info.xpath('.div[2]/h4/a/text()')[0]
        time.sleep(2)

if __name__ == '__main__':
    urls = ['http://a.qidian.com/?page={}'.format.(str(i)) for i in range(1,29655)]
    for url in urls:
        get_info(url)
    header = ['title',]
    book = xlwt.Workbook(encoding = 'utf-8')
    sheet = book.add_sheet('Sheet1')
    for h in range(len(header)):
        sheet.write(0,h,header[h])
    i=1
    for list in all_info_list:
        j=0
        for data in list:
            sheet.write(i,j,data)
            j+=1
        i+=1
book.save('xiaoshuo.xls') 
sum=0
for i in range(1,100)
    sum=sum+i