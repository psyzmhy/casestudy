# -*- coding: utf-8 -*-
# @Time :2019-01-30 07:32
# @Author: mahone.ma
"""
LSD：最低位有限
最低位和最高位就是指的个十百千这些位
先找到个位，根据个位放到相应桶里，
然后再找到10位，根据十位放到相应桶里，
依次循环往前，直到找到最高位。

找位数的时候，用最高比例和次高比例去取余和取整既可以得到
取道位数，然后放到桶里
然后再依次从桶里弹出来
"""
class Solution():
    def radix_sort(self,list,maxDigit):   #maxDigit 是数字的最大位数
        mod=10
        dev=1
        counter= [[0 for col in range(1)] for row in range(10)]
        for i in range(maxDigit):
            for j in range(len(list)):
                bucket=(list[j]%mod)//dev
                counter[bucket].append(list[j])

            print(counter)
            pos=0
            for j in range(len(counter)):
                while len(counter[j]) != 0 and pos < len(list):
                    if counter[j][0] != 0:
                        list[pos]=counter[j][0]
                        pos+=1
                    del counter[j][0]

            dev= dev * 10
            mod= mod * 10
        return list

solution = Solution()
list = [10,3,8,7,9,100,85,12,31,35,102]
print(solution.radix_sort(list,3))

