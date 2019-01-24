#-*- coding: utf-8 -*-
#@Time :2019-01-25 07:14
#@Author: mahone.ma

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


