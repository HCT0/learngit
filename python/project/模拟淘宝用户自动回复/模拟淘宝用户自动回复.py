'''
    运行程序,返回输入的提示,要用户自己输入,返回不同的结果
    用例：
        1 输入错误的不符合要求的文字
        2 同时输入多个符合的要求的文字
        3 输入提示的文字
'''
import time
if __name__ == '__main__':
    print("你好,这里是淘宝自动回复,请按提示内容进行操作！")
    print("1 物流查询！")
    print("2 要求退款！")
    print("3 钱款去向！")
    while(1)
        data = int(input("请输入对应功能的数字:"))
        if(data<1 or data>3):
            print("输入错误,请重新输入")
        else:
            print("请稍等,文件快马加鞭读取中")
            time.sleep(5)#休息5秒,不让电脑炸了 
    #创建要打开的文件的名字
    name=data+".txt"
    f=open(name,'a+')
    #输出指定文件的内容
    print(f.read())
    f.close()
     