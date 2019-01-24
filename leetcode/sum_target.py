

class Solution:
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if (nums[i]+nums[i+j+1])==target:
                    return i,i+j+1

nums=[4,3,4]
target=6
solution=Solution()
print(solution.twoSum(nums,target))