class Solution(object):
    def canAliceWin(self, nums):
        sum1 = 0
        sum2 = 0
        for val in nums:
            if(val < 10):
                sum1 += val
            else:
                sum2 += val
        return (sum1 != sum2)