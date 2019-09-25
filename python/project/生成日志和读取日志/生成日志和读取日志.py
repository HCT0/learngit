'''
    先创建二十个文件对象,每一个文件的名字均为 name+i,日志的内容为文件的名字。创建四个线程，每一个线程对应的
    处理五个任务。并且要在操作中加入锁

    用例：(不同的情况)
        1   文件的数字和字母式交替的,或者是缺少其中一项 name1,name,1,
        2   文件没有及时的关闭,无法读取f.close()
        3   读取文件内容错误
        
'''
import threading
#创建文件读取操作的函数
def operation(i):
    #创建一个锁
    print("test1")
    for n in range((i-1)*5+1,i*5+1):
        name = "name"+ (str)(n) +".txt"
        f = open(name,'a+')
        string = f.read()
        f.close()
        fp = open('one.txt','a+')
        fp.write(string)
        fp.close()
   
    print("test2")

if __name__ == '__main__':

#进行日志文件的写入
    text = list(range(20))#创建一个存储二十个文档对象的列表

for i in range(1,21):
    name = "name"+ (str)(i) + ".txt"
    text[i-1] = open(name,'a+')
    text[i-1].write(name)
    text[i-1].close()
#创建四个线程
Threads = [threading.Thread(target = operation,args=[i,]) for i in range(1,5)]
#运行线程
for t in Threads:
    t.start()
for i in Threads:
    t.join()


#进行日志文件的读取
