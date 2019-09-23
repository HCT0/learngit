'''
    验证登录,返回文件列表,获取用户要读取的文件,返回文件内容.
    日志的内容：文件的大小,最近的修改,登录时间
    用例：
        输入的用户不存在
        输入的格式不正确
        输入正确
'''
import time
dic = {'admin':'123456'}
if __name__ == '__main__':
    print("welcome to the log center!")
    time.sleep(1)
    #进行输入的判定
    while(1)
        user =input("请输入要登陆的用户:")
        pwd = input("请输入密码:")
        for i in user:
            if i  not in range(0,10):
                if i not in range("A","Z"):
                    if i not in range("a","z"):
                        print("输入错误字符！请重新执行输入！")
                    else:
                        break;
    if(dic[user] != '' and pwd ==dic[admin]):
        print("welcome to admin center")
    f = open('log.txt','a+')
    print("最后一次修改文件的时间是:")
    print("")
    print("最近登录的用户为:")
    print("")
    
    f.write()
    f.write(user)
    f.close()

    print(user,pwd)
