class Solution(object):
    def minElement(self, nums):
        num = 36
        for n in nums:
            num = min(num,n-9*((n//10)+(n//100)+(n//1000)+(n//10000)))
        
        return num