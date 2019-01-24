# # _*_ coding: utf-8 _*_
# import os
# import sys
# from fractions import Fraction
#
# # dir(obj) #用来查询一个类或者对象所有属性
# # help(obj.func) #了解模块、类型、对象、方法、属性的详细信息
# # help(os.path)
# # help(list)
#
# # 测试类型的方法，type和instance，推荐使用isinstance.
# # type不会把子类当作父类类型，isinstance会把子类作为父类类型
# L=[1,2]
# if type(L)==list:
#     print("1 is List")
# if isinstance(L,list):
#     print("2 is list")
#
# class A():
#     pass
#
# class B(A):
#     pass
#
# print(type(A)==A)
# print(type(B())==A)
# print(isinstance(A,A))
# print(isinstance(B(),A))
#
# # python数据类型，分为哈希类型和不可哈希类型
# # 哈希类型，不可改变的变量类型，可用hash函数查看其哈希值，可以用来作为字典的键值
# # 数字类型：int，float，decimal,Fraction,complex
# # 字符串类型：str，bytes
# # 元组：tuple
# # 不可变集合：frozenset
# # 布尔类型：True，False
# # 不可哈希类型，可变类型，list，dict和set，他们不可以用来作为字典的键值
#
# print(Fraction("1/3"))
# print(Fraction(1,3))
# print(complex(1,2))
#
# #数字的表达式操作符
# # yield 5                  生成器生成
# # lambda args:expression   生成匿名函数
# # x if y else z            三元表达式
# # x and y, x or y, not x   逻辑与，逻辑或，逻辑非
# # x is in y, x is not in y  成员对象测试
# # x is y, x is not y        对象实体测试
# # x < y, x<=y,x>y,x>=y,x==y,x!=y
# # 1< a <3                   大小比较
# # x ^ y, x | y, x & y      位异或，位或，位与
# # x<< y, x>>y              x左移，右移y位
# # +，-，*，/，//，%，**      运算符，加减乘除，返回商的整数部分，取余，取幂
# # x[i],x[i:j:k]            索引，分片
# # int(3.0),float(5)        强制类型转换
#
# #斐波那契数列
# # def fab1(max):
# #     n,a,b=0,0,1
# #     while(n<max):
# #         print(b)
# #         a,b=b,a+b
# #         n=n+1
# # fab1(5)
# #
# # def fab2(max):
# #     n,a,b=0,0,1
# #     L=[]
# #     while(n<max):
# #         L.append(b)
# #         a,b=b,a+b
# #         n=n+1
# #     return L
# #
# # for x in fab2(5):
# #     print(x)
#
# # def fab3(max):
# #     n,a,b=0,0,1
# #     while(n<max):
# #         yield b
# #         a,b=b,a+b
# #         n=n+1
# #
# # for x in fab3(5):
# #     print(x)
# #
# # a=lambda x,y,z:x+y+z
# # print(a(1,2,3))
# # print(a(3,4,5))
# # print(1 if False else 10)
#
#
# #python2和python3区别
# #1。print语句变成print函数
# #2。python 2 有ascii str（）类型，python 3 有unicode(utf-8)字符串以及一个字节类：byte和bytearrays
# #3。python3 除法不是取整数，而是取浮点数，如果取整需要用//，
# #4。捕获异常的语法由except exc，var 改为except exc as var。
# #4。1 在2。x时代，所有类型的对象都是直接抛出，在3。x时代，只有继承自BaseException的对象才能抛出
# #4。2 2。x raise语句使用逗号将抛出对象类型和参数分开，3。x取消了这种写法
# #4。3 3。x让异常更专一
#
#
#
#
# str="我爱北京天安门"
# print(str)
#
# #用bit_length计算所占的位数
# a= 1
# print(a.bit_length())
# b = 1024
# print(b.bit_length())
#
# #repr和str的区别，str是显示成适合人读取的格式，repr是转化成供解释器读取的格式
# a="hello\n"
# print(repr(a))
# print(a)
#
# #集合set
# """
# set是一个无序不重复的元素集，基本功能包括消除重复元素和关系测试
# set支持union，intersection，difference，symmetric_difference()
# set支持x in set，len(set),for x in set
# set不记录元素位置和插入点，因此不记录indexing，slicing等操作
# """
# s=set([1,3,5,10])
# t=set("hello")
# print(s | t)
# print(s.union(t))
# print(s - t)
# print(s.difference(t))
# print(s & t)
# print(s.intersection(t))
# print(s ^ t)
# print(s.symmetric_difference(t))
#
# #集合frozenset，不可变对象
# """
# set是可变对象，不存在Hash值，不可以作为字典的key值
# frozenset是不可变对象，存在Hash值，可以作为字典的key值
# frozenset对象没有add，remove方式，但是有union，difference等方法
# """
#
# #bool类型
#
# # print(type(False))
# # print(isinstance(True,int))
#
# #动态类型简介
# """
# 变量名通过引用指向对象，
# python中的类型属于对象，而不是变量。每个对象都包含头部信息，比如类型标志符
# """
# #对于可变对象，尽量不要使用共享引用
# L=[1]
# M=[1]
# print(L is M)
#
# L=M=[1,2,3]
# print(L is M)
#
# L=M=[1,2]
# L=L+[3,4]
# print(M)
# L += [3,4]
# print(M)
#
# #常用字符串常量和表达式
# s=" "
# print(s)
# s="spam's"
# print(s)
# s1="s\np\ta\x00m"
# print(s1)
# s2=r"\temp"
# print(s2)
# print(s1+s2)
# print(s1*3)
# print(len(s1))
# print("a %s parrot" % "kind")
# print("a {1} {0} is parrot".format("kind","red"))
#
# for x in s:print(x)
# print(".".join(["a","b","c"]))
#
# #内置str处理函数
# str1="abcdbdfh"
# # print(str1.upper())
# # print(str1.lower())
# # print(str1.swapcase())       #切换大小写
# # print(str1.capitalize())     #句子首字母大写
# # print(str1.title())          #句子每个单词首字母大写
# # print(str1.rjust(20))       #右对齐
# # print(str1.ljust(20))       #左对齐
# # print(str1.center(20))中心对齐
# # print(str1.zfill(20))         #左边填0
# # print(str1.find("b",0,10))
# # print(str1.rfind("b"))         #寻找字母
# # print(str1.count("b"))
# # #上述所有都可以用index代替，不同的index会抛出异常，find返回-1
# # print(str1.replace("b","s"))
# # print(str1.strip(""))    #删除空白字符
# # print(str1.strip("a"))   #删除开头结尾处的a字符
# # print(str1.lstrip("ab"))
# # print(str1.rstrip("fh"))
# # print(str1.startswith("a"))  #判断是否由a开始
# # print(str1.endswith("end"))
#
# # print(str1.isalnum())
# # print(str1.isalpha())
# # print(str1.isdigit())
# # print(str1.islower())
# # print(str1.isupper())
#
# #---三重引号编写多行字符串块
# mantra="""
# abcded
# adbaab
# cdefs
# """
# print(mantra)
#
# #索引和分片
# #类型转换
# print(bin(13))
# print(oct(13))
# print(hex(13))
#
# #另类字符串链接
# name="wang""hong"
# print(name)
# name="wang" \
#     "hong"
# print(name)
#
# #python中的字符串格式化调用方法
# #普通调用
# print("{0} and {1} and {2}".format("blue","read","yellow"))     #基于位置的调用
# print(("{motto} and {0}").format("blue",motto="red"))
#
# #基于key的调用
# # print("{config[spam]},{sys.platform}".format(sys=sys,config={'spam':'laptop'}))
# # print("{1[spam]},{0.platform}".format(sys,config={"spam:desk"}))
#
# #常用列表常量和初始化
# L=[[1,2],"spam"]   #嵌套列表
# L=list("range")    #列表初始化
# L=list(range(0,4))   #列表初始化
# list(map(ord,"spam"))  #列表解析
# len(L)                 #计算列表长度
# L.count("1")         #计算某个元素的个数
# L.append("3")        #在列表尾添加某个元素
# # L.extend(iterable)   #在列表里添加一个序列
# L.insert(0,"2")      #向列表的指定位置添加数据
# # print(L.index("1"))  #返回列表中value的第一个索引
# print(L)
# print(L.pop(3))      #删除index处的元素，默认为删除并返回最后一个元素
# L.remove(0)   #删除列表中的value值，只删除第一次出现的value值
# print(L)
# L.reverse()
# print(L)      #翻转列表
# # L.sort(cmp=None,key=None,reverse=False)  #列表排序
a=[]
a+=[1]
print(a)   #在原有列表进行操作，a的id不发生改变
a=[]
a=a+[1]
print(a)   #建立一个新的列表，a的id发生改变

#用切片来删除某一段
a=[1,2,3,4,5,6,7]
a[1:4]=[]
print(a)
a=[1,2,3,4,5,6,7]
del a[::2]  #删除偶数位
print(a)

# #排序相关知识
# #排序基础：sorted和list.sort都可以用来排序，不过前者更直接，对所有可迭代序列都有效，而后者只被定义在list中且原来的list会被改变
# #key函数：key参数可以用来指定一个函数，此函数在每个元素比较之前调用，此函数只有一个参数且返回一个值来进行比较
# L="welcome to china".split()
# L.sort(key=str.lower)
# print(L)
#
# #用参数reverse来表示升序和降序排序
# L.sort(reverse=False)
# print(L)
#
# L.sort(reverse=True)
# print(L)
# #排序的稳定性和复杂排序，排序被保证为稳定的，意思是说多个元素如果有相同的key，则排序前后他们的先后顺序不变
# #cmp函数，在python3.0中被删除了


# #list.append和list.extend区别
# #list.append是将一个元素加到列表末尾，list.extend是将一个序列合并到列表末尾
# list_x=[1,2,3]
# list_y=[4,5,6]
# list_x.append(list_y)
# print(list_x)
# list_x.extend(list_y)
# print(list_x)
#
# #map与lambda
# # 求一个数的平方的方法
# list_x=[1,2,3,4,5]
# a = 1
# def f1(x):
#     return a*x*x

# # 第一种方法，C/C++编程思想
# y = []
# for i in range(len(list_x)):
#     y.append(f1(list_x[i]))
# print(y)
#
# #第二种方法，python基本编程思想
#
# y=[]
# for x in list_x:
#     y.append(f1(x))
# print(y)

# #第三种方法，python map编程思想
# print(list(map(f1,list_x)))
#
# #第四种方法，python+map+lambda编程思想
# print(list(map(lambda x:x*x,list_x)))
#
# #map的进阶用法
# #map的输入元素的列表的关系是一一对应的,list和map一一对应使用
# test_x= [1,2,3]
# test_y=[1,2,3,4,5]
# test_z=[1,2,3,4,5,6,7]
# print(list(map(lambda x,y,z:x+y+z,test_x,test_y,test_z)))
#
# #map的判断语句
# print(list(map(lambda x:x>2,test_x)))

#常用字典常量和操作
D={}
D=dict.fromkeys(["s","q"],8)    #创建字典
print(D)
D1=dict(s=9,q=8)
print(D)                        #创建字典
D=dict([("s",9),("q",8)])
print(D)                        #创建字典
D=dict(zip(["name","age","city"],["tom",12]))    #将字典的key和值合并在一起，将两个列表合并到一起
print(D)
print(D.keys())                    #字典的键
print(D.values())                  #字典的值
print(D.items())#字典的键值对

#D.get(key,default)                #获取字典的某个键值，当键不存在的时候返回默认值
print(D.get("name","shanghai"))

D.update(D1)                       #合并字典D1的内容到D里，如果存在相同的键值D1的内容会覆盖D的
print(D)

#D.pop(key,default)
print(D.pop("city","none"))           #删除字典中key的键值对，如果没有则返回default的值
print(D)

#D.pop(item)                         #删除字典中随机的一个键值对，如果字典已空，返回keyerror异常
print(D.popitem())
print(D)

#del(D(key))                        删除字典中的键值对
#del(D)                             删除字典
#if key in D  if key not in D       判断字典中key是否存在

if "name" in D:                     #测试字典键是否存在
    print(True)
if "name" not in D:
    print(False)

#字典注意事项，1/对于字典新索引数值会增加一项，2/字典值不一定是字符串，也可以是任何不可变的对象
#不可变对象，调用对象自身的任何方法，也不会改变自身的任何内容，这些方法会创建新的对象并返回
#字符串，tuple，整数都是不可变对象，dict，set，list都是可变对象

#字典解析
D={k:8 for k in ["s","d"]}
print(D)
D={k:v for(k,v) in zip(["name","age"],["tom",10])}
print(D)

#元组和列表的唯一区别是列表是可变对象，元组是不可变对象
a=[1,2,3]  #a[0]=2,OK
a=(1,2,3)  #a[0]=2,Error
a=[(1,2)]  #a[0,1]=2,Error
a=([1,2])  #a[0,1]=2,OK

#--元组的特殊语法：逗号和圆括号
D=(12)             #D=12
D=(12,)            #D=(12,)

#文件基本操作
# output=open("file.txt","rw")     #打开输出文件，用于写
# input=open("file.txt","r")       #打开输入文件，用于读
# fp=read([size])                  #size为读取的长度，以byte为单位
# fp=readline([size])              #读一行，如果定义了size，返回的只是一行的一部分
# fp=readlines([size])             #返回文件的每一行，作为一个list.size代表的是读取的总长度
# fp.readable()                    #文件是否可读
# fp.write(str)                    #向文件中写入
# fp.writelines(seq)               #把seq内容一次行写入，多行写入
# fp.writable()                    #文件是否可写
# fp.close()                       #关闭文件
# fp.flush()                       #将缓存当中的内容写入硬盘
# for line in open("data/data.txt"):
#     print(line)                   #适用于读取大的文件

with open("data/data.txt") as file:
    print(file.readline())        #使用with语句，可以保证文件关闭

# with open("data/data.txt") as file:
#     print(file.readlines())       #一次性读入文件所有语句

"""
with语句的作用：在读文件和写文件的时候，如果用open就必须用close来关闭文件。
但是在文件出现IOerror的时候，就没有办法及时关闭。这个时候在读写文件的时候，就需要用try，except
with语句解决了这个问题，使用with语句不用考虑到自己去关闭文件
读一般有四种方法：
read()读取较小的文件
read(size)读取较大文件中一部分
readline()读取一行
readlines()读取所有行
"""

#其他
#python中的真假定义：1。不为0则为真，否则为假 2。不为空则为真，否则为假

"""
语法和语句部分
语法和语句部分
语法和语句部分
"""

#赋值语句的形式
























































