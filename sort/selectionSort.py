"""
选择排序
首先从威排序序列中选择最大小元素，放在排序序列位置，然后再从剩下的未排序序列寻找
依次类推
"""

class Solution():
    def selectionSort(self,list):
        minValue=0
        for i in range(len(list)):
            minValue=i
            for j in range(len(list)-i-1):
                if(list[i+j+1]<list[minValue]):
                    minValue=i+j+1
            temp=list[minValue]
            list[minValue]=list[i]
            list[i]=temp
        return list

solution=Solution()
list=[10,3,5,7,9]
print(solution.selectionSort(list))

