#-*- coding: utf-8 -*-
#@Time :2019-01-25 07:14
#@Author: mahone.ma
"""
希尔排序是第一个突破n²的排序算法，又叫做缩小增量排序
选择一个增量序列，按增量序列个数k，对序列进行k趟排序
每趟排序，根据对应的增量，将待排序列分割成为若干长度为m的自序列，分别对各子表进行插入排序，仅增量为1时，整个序列作为一个表来处理
希尔排序的核心在于间隔序列的设定，既可以提前设定好间隔序列，也可以动态的定义间隔序列
"""

class Solution():
    def shell_sort(self,list):
        gap = 1
        while(gap < (len(list) // 3)):
            gap = gap * 3 + 1
        print(gap)
        while(gap >= 1):
            for i in range(gap,len(list)):
                temp = list[i]
                j = i-gap
                while( j >= 0 and list[j] > temp):
                    list[ j + gap]=list[ j ]
                    j = j - gap
                list[j + gap] = temp
            gap = gap // 3
            print(gap)
        return list

solution=Solution()
list=[10,3,8,7,9]
print(solution.shell_sort(list))


