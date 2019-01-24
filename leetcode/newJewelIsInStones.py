
class Solution:
    def numJewelsIsInStones(self,J,S):
        nums=0
        for stone in S:
            if stone in J:
                nums=nums+1
        return nums

J="a"
S="aAAbbbba"
solution=Solution()
print(solution.numJewelsIsInStones(J,S))
