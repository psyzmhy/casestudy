#-*- coding: utf-8 -*-
#@Time :2019-01-26 10:56
#@Author: mahone.ma
"""
文件功能注释
归并排序是简历在归并操作上的一种有效的排序算法，该算法采用分而治之的方法，将已有序的子序列合并得到完全有序的序列
先让每个子序列有序，若将两个有序表合并成一个有序表，叫做2-路归并
归并排序是一种稳定的排序方法，和选择排序一样，归并排序性能不受输入数据的影响，但是表现要比选择排序要好，代价是额外的内存空间
"""
class Solution():
    def merge_sort(self,list):
        self.len=len(list)
        if(self.len < 2):
            return list
        middle=self.len//2
        left=list[0:middle]
        right=list[middle:self.len]
        return self.merge(self.merge_sort(left),self.merge_sort(right))

    def merge(self,left,right):
        result=[]
        while(len(left)>0 and len(right)>0):
            if(left[0]<right[0]):
                result.append(left[0])
                left.remove(left[0])
            else:
                result.append(right[0])
                right.remove(right[0])

        while(len(left)>0):
            result.append(left[0])
            left.remove(left[0])

        while(len(right)>0):
            result.append(right[0])
            right.remove(right[0])

        return result

solution=Solution()
list=[12,3,6,7,9]
print(solution.merge_sort(list))
