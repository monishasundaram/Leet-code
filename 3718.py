class Solution(object):
    def missingMultiple(self, nums, k):
        arr = []

        for i in range(len(nums)):
            arr.append((i + 1) * k)

        for i in range(len(arr)):
            if arr[i] not in nums:
                return arr[i]

        return (len(nums) + 1) * k
