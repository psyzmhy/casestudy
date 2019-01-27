# -*- coding: utf-8 -*-
# @Time :2019-01-26 14:26
# @Author: mahone.ma
"""
文件功能注释
快速排序的基本思想：通过一趟排序将待排记录分割成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，则可以分别排序
从数列中挑出一个元素，从后往前找出比他小的，替换。从前往后再找出比他大的，再次替换。
"""

class Solution():
    def quick_sort(self,list):
        self.list=list
        self.sort(0,len(self.list) - 1)
        return self.list

    def sort(self,left,right):
        if(left >= right):
            return
        i = left
        j = right
        key = self.list[i]

        while(i < j):
            while(i < j and key <= self.list[j]):
                j = j - 1

            self.list[i] = self.list[j]

            while(i < j and key >= self.list[i]):
                i = i + 1

            self.list[j] = self.list[i]

        self.list[i] = key
        self.sort(left,i-1)
        self.sort(i+1,right)

solution = Solution()
list = [1, 30, 8,10,11,12,13]
print(solution.quick_sort(list))