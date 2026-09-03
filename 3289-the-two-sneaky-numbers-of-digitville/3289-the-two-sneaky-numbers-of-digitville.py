class Solution(object):
    def getSneakyNumbers(self, nums):
        arr = []
        for i in range(len(nums)):
            count = 0
            for j in range(len(nums)):
                if(nums[i]==nums[j]):
                    
                    count+=1
            if count == 2 and nums[i] not in arr:
                arr.append(nums[i])
        return arr