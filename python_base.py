# _*_ coding: utf-8 _*_
import os
from fractions import Fraction

# dir(obj) #用来查询一个类或者对象所有属性
# help(obj.func) #了解模块、类型、对象、方法、属性的详细信息
# help(os.path)
# help(list)

# 测试类型的方法，type和instance，推荐使用isinstance.
# type不会把子类当作父类类型，isinstance会把子类作为父类类型
L=[1,2]
if type(L)==list:
    print("1 is List")
if isinstance(L,list):
    print("2 is list")

class A():
    pass

class B(A):
    pass

print(type(A)==A)
print(type(B())==A)
print(isinstance(A,A))
print(isinstance(B(),A))

# python数据类型，分为哈希类型和不可哈希类型
# 哈希类型，不可改变的变量类型，可用hash函数查看其哈希值，可以用来作为字典的键值
# 数字类型：int，float，decimal,Fraction,complex
# 字符串类型：str，bytes
# 元组：tuple
# 不可变集合：frozenset
# 布尔类型：True，False
# 不可哈希类型，可变类型，list，dict和set，他们不可以用来作为字典的键值

print(Fraction("1/3"))
print(Fraction(1,3))
print(complex(1,2))

#数字的表达式操作符
# yield 5                  生成器生成
# lambda args:expression   生成匿名函数
# x if y else z            三元表达式
# x and y, x or y, not x   逻辑与，逻辑或，逻辑非
# x is in y, x is not in y  成员对象测试
# x is y, x is not y        对象实体测试
# x < y, x<=y,x>y,x>=y,x==y,x!=y
# 1< a <3                   大小比较
# x ^ y, x | y, x & y      位异或，位或，位与
# x<< y, x>>y              x左移，右移y位
# +，-，*，/，//，%，**      运算符，加减乘除，返回商的整数部分，取余，取幂
# x[i],x[i:j:k]            索引，分片
# int(3.0),float(5)        强制类型转换

#斐波那契数列
# def fab1(max):
#     n,a,b=0,0,1
#     while(n<max):
#         print(b)
#         a,b=b,a+b
#         n=n+1
# fab1(5)
#
# def fab2(max):
#     n,a,b=0,0,1
#     L=[]
#     while(n<max):
#         L.append(b)
#         a,b=b,a+b
#         n=n+1
#     return L
#
# for x in fab2(5):
#     print(x)

# def fab3(max):
#     n,a,b=0,0,1
#     while(n<max):
#         yield b
#         a,b=b,a+b
#         n=n+1
#
# for x in fab3(5):
#     print(x)
#
# a=lambda x,y,z:x+y+z
# print(a(1,2,3))
# print(a(3,4,5))
# print(1 if False else 10)


#python2和python3区别
#1。print语句变成print函数
#2。python 2 有ascii str（）类型，python 3 有unicode(utf-8)字符串以及一个字节类：byte和bytearrays
#3。python3 除法不是取整数，而是取浮点数，如果取整需要用//，
#4。捕获异常的语法由except exc，var 改为except exc as var。
#4。1 在2。x时代，所有类型的对象都是直接抛出，在3。x时代，只有继承自BaseException的对象才能抛出
#4。2 2。x raise语句使用逗号将抛出对象类型和参数分开，3。x取消了这种写法
#4。3 3。x让异常更专一




str="我爱北京天安门"
print(str)

#用bit_length计算所占的位数
a= 1
print(a.bit_length())
b = 1024
print(b.bit_length())

#repr和str的区别，str是显示成适合人读取的格式，repr是转化成供解释器读取的格式
a="hello\n"
print(repr(a))
print(a)

#集合set
"""
set是一个无序不重复的元素集，基本功能包括消除重复元素和关系测试
set支持union，intersection，difference，symmetric_difference()
set支持x in set，len(set),for x in set
set不记录元素位置和插入点，因此不记录indexing，slicing等操作
"""
s=set([1,3,5,10])
t=set("hello")
print(s | t)
print(s.union(t))
print(s - t)
print(s.difference(t))
print(s & t)
print(s.intersection(t))
print(s ^ t)
print(s.symmetric_difference(t))

#集合frozenset，不可变对象
"""
set是可变对象，不存在Hash值，不可以作为字典的key值
frozenset是不可变对象，存在Hash值，可以作为字典的key值
frozenset对象没有add，remove方式，但是有union，difference等方法
"""

#bool类型

# print(type(False))
# print(isinstance(True,int))

#动态类型简介
"""
变量名通过引用指向对象，
python中的类型属于对象，而不是变量。每个对象都包含头部信息，比如类型标志符
"""
#对于可变对象，尽量不要使用共享引用
L=[1]
M=[1]
print(L is M)

L=M=[1,2,3]
print(L is M)

L=M=[1,2]
L=L+[3,4]
print(M)
L += [3,4]
print(M)

#常用字符串常量和表达式
s=" "
print(s)
s="spam's"
print(s)
s1="s\np\ta\x00m"
print(s1)
s2=r"\temp"
print(s2)
print(s1+s2)
print(s1*3)
print(len(s1))
print("a %s parrot" % "kind")
print("a {1} {0} is parrot".format("kind","red"))

for x in s:print(x)
print(".".join(["a","b","c"]))

#内置str处理函数
str1="abcdbdfh"
# print(str1.upper())
# print(str1.lower())
# print(str1.swapcase())
# print(str1.capitalize())
# print(str1.title())
# print(str1.rjust(20))
# print(str1.ljust(20))
# print(str1.center(20))
# print(str1.zfill(20))
# print(str1.find("b",0,10))
# print(str1.rfind("b"))
# print(str1.count("b"))
# #上述所有都可以用index代替，不同的index会抛出异常，find返回-1
# print(str1.replace("b","s"))
# print(str1.strip(""))    #删除空白字符
# print(str1.strip("a"))   #删除开头结尾处的a字符
# print(str1.lstrip("ab"))
# print(str1.rstrip("fh"))
# print(str1.startswith("a"))
# print(str1.endswith("end"))

print(str1.isalnum())
print(str1.isalpha())
print(str1.isdigit())
print(str1.islower())
print(str1.isupper())

#---三重引号编写多行字符串块
mantra="""
abcded
adbaab
cdefs
"""
print(mantra)

#索引和分片
#类型转换
print(bin(13))
print(oct(13))
print(hex(13))

#另类字符串链接
name="wang""hong"
print(name)
name="wang" \
    "hong"
print(name)
















































