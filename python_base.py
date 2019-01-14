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

def fab3(max):
    n,a,b=0,0,1
    while(n<max):
        yield b
        a,b=b,a+b
        n=n+1

for x in fab3(5):
    print(x)

a=lambda x,y,z:x+y+3
print(a(1,2,3))







