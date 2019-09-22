'''
题目： p39
简要：求出一个长为n的数组中重复出现了的数字。
用例：
    1、没有重复的数字
    2、输出无效的数字
    3、有一个或者多个重复的数字
解题思路：
    因为n长度的数组的下标和n-1的数字符合，可以作为判断的条件
    将i位置的数值m和m位置的数值x比较，判断是否相等，如果不相等，则交换数值，如果相等，则输出m，并且i++；
    出现重复则是作为判断的条件
'''
#执行输入操作
n = int(input("请输入数组的长度:"))
a=list(range(0,n))
print("请分别输入每一个数字")
for i in range(1,n+1):
    while(1):  
        x =int(input("请输入数字:"))
        if(x < 0 or x > n-1 ):
            print("输入的数字不符合格式,请重新输入")
        else:
            a[i-1] = x
            break;
print("输入正常")
#进行运算
site = 0
first = a[site]
while(1):
    if(a[first] == first):
        site+=1
        if(site >= n-1): #判断条件二
            break 
    else:
        if(a[a[first]] == a[first]): #判断条件一
            print("重复的数字有")
            print(a[first])
            if(site >= n-1): #判断条件二
                break 
            site+=1
        else:
            swap=a[a[first]]
            a[first] = a[a[first]]
            a[first] = swap
print(a)
            