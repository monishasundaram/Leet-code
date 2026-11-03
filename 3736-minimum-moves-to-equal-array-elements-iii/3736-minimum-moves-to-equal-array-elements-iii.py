class Solution(object):
    def minMoves(self, nums):
        m = max(nums)
        return sum([m-i for i in nums])