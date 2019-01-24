"""
冒泡排序：
比较相邻的元素，如果第一个比第二个大，就交换他们两个
对每一对相邻元素做同样的工作，从开始第一对到结尾最后一对，这样在最后的元素应该就是最大的数
针对所有元素重复以上步骤，除了最后一个
重复步骤1～3，直到排序完成
"""


class Solution:
    def bubbleSort(self,list):
        for i in range(len(list)):
            for j in range(len(list)-i-1):
                if list[i]>list[i+j+1]:
                    temp=list[i]
                    list[i]=list[i+j+1]
                    list[i+j+1]=temp
        return list

solution=Solution()
list=[10,3,9,7,5]
print(solution.bubbleSort(list))