'''
    使用多线程实现倒计时效果
'''
import time
import datetime
from multiproessing import Process

def calculate_time(year,month,day):
    date1 = datetime.datetime(year,month,day)
    a = datetime.date.today()
    
    date2 = datetime.datetime(a.yearr,a.month,a.day)
    all=(data1-data1).days
    return all

def print_time():
    print("今天的日期:")
    a = datetime.date.today()
    print(a.year,"年",a.month,"月",a.day,"日")
    print("\n")
    print("距离：",'\n')

def gaokao():
    gaokao = calculate_time(2020,6,6)
    print("距离2020高考还有：" ,gaokao,"天")

def dongjing():
    dongjin = calculate_time(2020,7,24)
    print("距离东京奥运会还有：",dongjing,"天")

def beijin():
    beijin= calculate_time(2022,2,4)
    print("距离北京冬奥会还有：",beijin,"天")

def kata():
    kata= calculate_time(2022,11,21)
    print("卡塔尔世界杯还有：",kata,"天")


if __name__ == '__main__':
    print_time = Process(target = print_time)
    print_time.start()
    gaokao = Process(target = gaokao)
    gaokao.start()
    dongjing = Process(target = dongjing)
    dongjing.start()
    
    beijin = Process(target = beijin)
    beijin.start()
    
    kata = Process(target = kata)
    kata.start()

    print_time.join()
    gaokao.join()
    dongjing.join()
    beijin.join()
    kata.join()
