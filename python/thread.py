'''
    使用多线程实现倒计时效果
'''
import datetime
from multiprocessing import Process

def calculate_time(year,month,day):
    date1 = datetime.datetime(year,month,day)
    
    a = datetime.date.today()
    date2 = datetime.datetime(a.year,a.month,a.day)
    all=(date1-date2).days
    return all

def print_time():
    print("今天的日期:")
    a = datetime.date.today()
    print(a.year,"年",a.month,"月",a.day,"日")
    print("距离：")

def gaokao():
    gaokao = calculate_time(2020,6,6)
    print("2020高考还有：" ,gaokao,"天")

def dongjing():
    dongjing = calculate_time(2020,7,24)
    print("东京奥运会还有：",dongjing,"天")

def beijin():
    beijin= calculate_time(2022,2,4)
    print("北京冬奥会还有：",beijin,"天")

def kata():
    kata= calculate_time(2022,11,21)
    print("卡塔尔世界杯还有：",kata,"天")


if __name__ == '__main__':
    print_time_o = Process(target = print_time)
    print_time_o.start()
    gaokao_o = Process(target = gaokao)
    gaokao_o.start()
    dongjing_o = Process(target = dongjing)
    dongjing_o.start()
    
    beijin_o = Process(target = beijin)
    beijin_o.start()
    
    kata_o = Process(target = kata)
    kata_o.start()

  