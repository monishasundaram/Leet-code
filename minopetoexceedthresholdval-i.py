class Solution(object):
    def minOperations(self, nums, k):
        count = 0
        for i in nums:
            if i<k:
                count += 1
        return count
