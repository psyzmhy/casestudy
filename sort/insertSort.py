# --coding:utf-8
"""
插入排序是构建有序序列，对于未排序序列，从已排序序列中从后向前扫描，找到相应位置插入
插入排序采用的是in place排序
"""
class Solution:
    def insert_sort(self,list):
        for i in range(1,len(list)):
            current=list[i]
            preIndex=i-1
            while(preIndex >= 0 and list[preIndex] > current):
                list[preIndex + 1]=list[preIndex]
                preIndex=preIndex - 1
                print(preIndex)
            list[preIndex + 1]=current
        return list

solution=Solution()
list=[1,3,5,7,9]
print(solution.insert_sort(list))