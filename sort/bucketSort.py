# -*- coding: utf-8 -*-
# @Time :2019-01-29 21:29
# @Author: mahone.ma
"""
文件功能注释

代码算法逻辑：
寻找最大值和最小值
根据最大值和最小值以及桶的单个长度，计算桶的个数
创建桶的第一层数组并为数组初始化
利用映射函数将数据分配到各个桶中，使用append方法
对诶个桶进行排序，使用插入排序
将排序之后的桶合并到大的数组当中

概念：桶排序是计数排序的升级版，他利用了函数的映射关系，搞笑与否的关键就在于这个映射函数的确定
假设输入数据均服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序

桶排序最好情况下使用线性时间n,桶排序的时间复杂读，取决于对各个桶之间数据进行排序的时间复杂度
"""

import insertSort

class Solution():
    def bucket_sort(self,list):
        insertSolution=insertSort.Solution()
        length=len(list)
        newList=[]
        if len(list)<2:
            return list

        minValue=list[0]
        maxValue=list[0]
        for i in range(length):
            if list[i]<minValue:
                minValue=list[i]
            elif list[i]>maxValue:
                maxValue=list[i]

        bucketSize=5              #桶的大小固定一个常量
        bucketCount=((maxValue-minValue)//bucketSize)+1

        bucketList= [[0 for col in range(bucketSize)] for row in range(bucketCount)]
        for i in range(length):
            bucketList[(list[i] - minValue) // bucketSize].append(list[i])

        for i in range(len(bucketList)):
            insertSolution.insert_sort(bucketList[i])
            for j in range(len(bucketList[i])):
                if bucketList[i][j] != 0:
                    newList.append(bucketList[i][j])

        return newList,bucketCount


solution = Solution()
list = [10,3,8,7,9,100,85,12,31,35,102]
print(solution.bucket_sort(list))

