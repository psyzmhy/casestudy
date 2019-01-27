# -*- coding: utf-8 -*-
# @Time :2019-01-27 13:11
# @Author: mahone.ma
"""
文件功能注释
计数排序不是基于比较的排序算法，其核心在于将输入的数据转化为键存储在额外开辟的数组空间当中
作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数
找出带排序的数组中最大和最小的元素，统计出现的次数，存入和累加，然后反向填充目标数组
计数排序是一种稳定的排序算法，其排序速度快于任何排序算法。当K不是很大并且序列比较集中时，是一个很有效的排序算法
"""

class Solution():
    def counting_sort(self,list,max_value):
        index = 0
        list_len = len(list)
        bucket_len = len(list) - 1
        value_list = [0] * (max_value + 1)

        for x in list:
            value_list[x] += 1

        for i in range(len(value_list)):
            while(value_list[i] > 0):
                list[index] = i
                index += 1
                value_list[i] -= 1
        return list

solution = Solution()
list = [20,3,6,7,9]
print(solution.counting_sort(list,20))