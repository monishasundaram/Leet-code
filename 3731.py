class Solution(object):
    def findMissingElements(self, nums):
        nums1 = sorted(nums)
        ans = []

        for i in range(nums1[0], nums1[-1] + 1):
            if i not in nums1:
                ans.append(i)

        return ans
